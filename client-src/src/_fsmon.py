#!/usr/bin/python
"""
This file is part of Rainmaker.

    Rainmaker is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Rainmaker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Rainmaker.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys
import os
import time
import logging
import yaml

# threaded shell execution
from subprocess import PIPE, Popen
from threading import Thread
import thread
import shlex

# Excape path info from watchdog
from pipes import quote

# debug
from logging import INFO, basicConfig
# Watchdog
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileSystemEvent

# Queue imports for different python versions
try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x

#import copy

import getpass
from _conf import RainmakerConfig

class RainmakerLoggingEventHandler(FileSystemEventHandler):
    def __init__(self, log, base_path):
        self.log = log
        self.base_path = base_path

    """EventHandler"""
    def log_event(self, event):
        if event.event_type == 'moved':
            msg = "SRC=%s DEST=%s" % (self.src_file_rel(event),self.dest_file_rel(event) )  
        else:
            msg = "SRC=%s" % self.src_file_rel(event)

        self.log.info( "EVENT=%s %s" % (event.event_type, msg) )

    """ File System Events """
    def on_moved(self, event):
        self.log_event(event)

    def on_created(self, event):
        self.log_event(event)

    def on_deleted(self, event):
        self.log_event(event)

    def on_modified(self, event):
		self.log_event(event)
    
    """ Available Event properties """

    # return event file path relative to root
    def src_file_rel(self,event):
        return quote( event.src_path.replace(self.base_path+os.sep,'') )  

    def dest_file_rel(self,event):
        return quote( event.dest_path.replace(self.base_path+os.sep,'') )
     
    def event_type(self,event):
        return event.event_type



class RainmakerEventHandler(FileSystemEventHandler):
    def __init__(self, conf, profile, msg_q, name):
        self.cmd_q = Queue()
        self.threads_q = Queue()
        self.msg_q = msg_q
        self.conf = conf
        self.profile = profile
        self.log = logging.getLogger('eh_%s' % name)
        self.name = name

        # Fill out nested macros (max 5 levels deep)
        for i in range(1,5):
            found_macro = False
            for flag in self.profile['cmd_macros']:
                new_macro = self.do_macro(self.profile['cmd_macros'][flag])
                if self.profile['cmd_macros'][flag] != new_macro:
                    found_macro = True
            if not found_macro:
                break

        # Add macros to commands
        for cmd_key,cmd_val in self.profile['cmds'].items():
            # process command list
            if isinstance(cmd_val, list): 
                for idx,item in enumerate(cmd_val):
                    self.profile['cmds'][cmd_key][idx]=self.do_macro(item)
            # process single command
            else:
                self.profile['cmds'][cmd_key] = self.do_macro(cmd_val)

        self.running = True
        self.start_threads()

    def start_threads(self):
        
        for i in range( int(self.profile['max_threads']) ):
            t = Thread(target=self.cmd_worker)
            t.daemon = True
            t.start()
            self.threads_q.put( t )
    # run
    def cmd_worker(self):
        while self.running==True:
            time.sleep(1)
            try:
                cmd =  self.cmd_q.get_nowait()
            except Empty:
                continue
            self.log.info('exec cmd: %s' % cmd)
            s_cmd = shlex.split(cmd) 
            
            p = Popen(s_cmd, stdout = PIPE, stderr=PIPE)
            result = {  'stdout':p.stdout.read(),
                        'stderr':p.stderr.read(),
                        'returncode':p.returncode,
                        'cmd':cmd
                     }
            self.msg_q.put( result )
            self.log.info('finished cmd: %s' % cmd)
            #if result['stderr']:
            #    self.log.debug(result['stderr']) 

    """EventHandler"""
    def cmd_create(self, event):
        self.log.debug('event fired: %s' % event.event_type)
        #Start building command
        if self.profile['use_cmd_all'] and event.event_type != 'startup':
            cmd = self.profile['cmds']['all']
        else:
            cmd = self.profile['cmds'][event.event_type]
        
        # use base if none exists 
        if cmd == '' or cmd is None:
            self.log.warn( 'no command for event: %s' % event.event_type)
            return
        # process command list
        if isinstance(cmd, list): 
            for item in cmd:
                self.do_cmd(item,event)
        # process single command
        else:
            self.do_cmd(cmd,event)

    def do_cmd(self,cmd,event):       
        # Insert placeholder values
        cmd = self.profile.subst(cmd)
        for key in self.conf['cmd_flags']:
            flag = self.conf['cmd_flags'][key]
            if cmd.find( flag ) != -1:
                cmd = cmd.replace( flag , getattr(self, key )(event) )
        # Add command to command queue
        self.cmd_q.put(cmd)

    # scan a command for macros and substitute them
    def do_macro(self,cmd):
        if str(cmd) == '' or cmd is None:
            return ''
        for flag in self.profile['cmd_macros']:
            val = self.profile['cmd_macros'][flag]
            if cmd.find( flag ) != -1:
                cmd = cmd.replace( flag , val )
        return cmd
            
    """ Available client methods """
    def stop(self):
        self.log.info( 'stopping threads' )
        self.running = False
        while True:
            try:
                t =  self.threads_q.get_nowait()
                self.log.info('Stopping thread: %s' % t.name)
                t.join()
            except Empty:
                break
             
    def startup_cmd(self):
        event =FileSystemEvent('startup',self.profile['local_root'],True)
        self.cmd_create(event)

    """ File System Events """
    def on_moved(self, event):
        self.cmd_create(event)

    def on_created(self, event):
        self.cmd_create(event)

    def on_deleted(self, event):
        self.cmd_create(event)

    def on_modified(self, event):
		self.cmd_create(event)

    """ Available Event properties """
    def root(self,event):
        return self.profile['local_root'] 

    def src_dir_rel(self,event):
        return '' 
    
    def src_dir_full(self,event):
        return quote( event.src_path )

    # return event file path relative to root
    def src_file_rel(self,event):
        return event.src_path.replace(self.profile['local_root']+os.sep,'')  

    def src_file_full(self,event):
        return ''

    def src_file_name(self,event):
        return ''

    def src_file_type(self,event):
        return ''

    def dest_dir_rel(self,event):
        return ''

    def dest_dir_full(self,event):
        return ''

    def dest_file_rel(self,event):
        return event.dest_path.replace(self.profile['local_root']+os.sep,'')  
    
    def dest_file_full(self,event):
        return ''
    
    def dest_file_name(self,event):
        return ''

    def dest_file_type(self,event):
        return ''
    
    def event_type(self,event):
        return event.event_type

class Rainmaker():
   
    def __init__(self,config=None, auto_start=True ):
        self.log=logging.getLogger('main')
        self.event_handlers = []
        self.config = config if config else  RainmakerConfig()
        self.profiles = self.config.profiles

        self.msg_q = Queue()
        self.observer = Observer()
        self.observer.start()

        if not auto_start:
            return

        for k in self.profiles:
            if self.profiles[k]['auto_start']==True:
                self.add_watch(k)

        if not self.event_handlers:            
            self.log.warn('No running profiles')

    def add_watch(self,key):
        if not key in self.profiles:
            self.log.error('unknown profile %s' % key)

        self.log.info('Starting profile: %s' % key)
        profile = self.profiles[key]

        profile['local_root'] = os.path.abspath(os.path.expanduser(profile['local_root']))
        
        profile.subst_all()

        if not os.path.isdir(profile['local_root']):
            self.log.info('creating dir: %s' % profile['local_root'])
            os.mkdir(profile['local_root'])

        event_handler = RainmakerEventHandler( self.config, profile, self.msg_q, key )
        self.event_handlers.append( event_handler )

        rec_flag = True
        if profile.has_key('recursive'):
            rec_flag = bool(profile['recursive']) 
        self.observer.schedule( event_handler, profile['local_root'], recursive = rec_flag) 
        
        logging.info('Started profile: %s' % key)
    
        if profile['cmds']['startup'] != '':
            event_handler.startup_cmd()

    def remove_watch(self, k): 
        for eh in self.event_handlers:
            if eh.name == k:
                self.log.info('Stopping profile: %s' % k)
                self.observer.unschedule(eh)
                break 

    def messages(self):
        messages = []
        try:
            while True:
                messages.append( self.msg_q.get_nowait() )
        except Empty:
            pass

        return messages

    def shutdown(self):
        self.log.info( "Shutting down FSwatcher")
        self.observer.stop()
        self.observer.unschedule_all()
        self.observer.join()
        self.log.info("Shutting down thread and Fork pool")
        for eh in self.event_handlers:
            self.log.info('Stopping profile: %s' % eh.name)
            eh.stop()


