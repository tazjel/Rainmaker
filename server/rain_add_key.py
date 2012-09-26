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

import os
import argparse
import _ssh

def parser_init():
    parser = argparse.ArgumentParser(version='0.2012.09.10',add_help=True)
    parser.add_argument('--user', action="store")
    parser.add_argument('pub_key', action="store")
    return parser

parser = parser_init()
args = parser.parse_args()

if not os.path.isfile(args.pub_key):
    RuntimeError("pubkey file not found: %s" % args.pub_key)

f = open(args.pub_key,'r')
k=f.readline()
f.close()

try:
    _ssh.add_key(k, args.user)
except RuntimeError as e:
    print e.message

