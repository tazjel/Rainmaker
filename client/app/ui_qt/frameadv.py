# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './profile-adv.ui'
#
# Created: Fri Apr 27 22:59:14 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(543, 542)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Frame)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_22 = QtGui.QLabel(Frame)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_7.addWidget(self.label_22)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_2 = QtGui.QLineEdit(Frame)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtGui.QLabel(Frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(176, 0))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton_2 = QtGui.QToolButton(Frame)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.line_4 = QtGui.QFrame(Frame)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.line = QtGui.QFrame(Frame)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.line)
        self.label_5 = QtGui.QLabel(Frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinBox = QtGui.QSpinBox(Frame)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBox)
        self.label_4 = QtGui.QLabel(Frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.spinBox_2 = QtGui.QSpinBox(Frame)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_2)
        self.horizontalLayout_3.addLayout(self.formLayout_3)
        self.line_5 = QtGui.QFrame(Frame)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_3.addWidget(self.line_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(Frame)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(Frame)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_4 = QtGui.QCheckBox(Frame)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout.addWidget(self.checkBox_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtGui.QFrame(Frame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_12 = QtGui.QLabel(Frame)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(Frame)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(Frame)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtGui.QLabel(Frame)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtGui.QLabel(Frame)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_16)
        self.label_17 = QtGui.QLabel(Frame)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_17)
        self.label_18 = QtGui.QLabel(Frame)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_18)
        self.label_19 = QtGui.QLabel(Frame)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_19)
        self.label_20 = QtGui.QLabel(Frame)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_4.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_20)
        self.label_21 = QtGui.QLabel(Frame)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_4.setWidget(5, QtGui.QFormLayout.FieldRole, self.label_21)
        self.label_11 = QtGui.QLabel(Frame)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_24 = QtGui.QLabel(Frame)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_24)
        self.verticalLayout_3.addLayout(self.formLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_5 = QtGui.QPushButton(Frame)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_7 = QtGui.QPushButton(Frame)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.line_3 = QtGui.QFrame(Frame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_5.addWidget(self.line_3)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(Frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(Frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_9 = QtGui.QLabel(Frame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(Frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.cmd_startup = QtGui.QLineEdit(Frame)
        self.cmd_startup.setObjectName(_fromUtf8("cmd_startup"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.cmd_startup)
        self.cmd_shutdown = QtGui.QLineEdit(Frame)
        self.cmd_shutdown.setObjectName(_fromUtf8("cmd_shutdown"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.cmd_shutdown)
        self.lineEdit_5 = QtGui.QLineEdit(Frame)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_7 = QtGui.QLineEdit(Frame)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtGui.QLabel(Frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_8 = QtGui.QLineEdit(Frame)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_23 = QtGui.QLabel(Frame)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_23)
        self.cmd_periodic = QtGui.QLineEdit(Frame)
        self.cmd_periodic.setObjectName(_fromUtf8("cmd_periodic"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.cmd_periodic)
        self.lineEdit_6 = QtGui.QLineEdit(Frame)
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.comboBox = QtGui.QComboBox(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(124, 0))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(1, _fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.comboBox)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.cmd_macro = QtGui.QLineEdit(Frame)
        self.cmd_macro.setObjectName(_fromUtf8("cmd_macro"))
        self.horizontalLayout_6.addWidget(self.cmd_macro)
        self.toolButton = QtGui.QToolButton(Frame)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_6.addWidget(self.toolButton)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_25 = QtGui.QLabel(Frame)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_25)
        self.cmd_all = QtGui.QLineEdit(Frame)
        self.cmd_all.setObjectName(_fromUtf8("cmd_all"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.cmd_all)
        self.verticalLayout_5.addLayout(self.formLayout_2)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Frame", "Advanced Profile View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Frame", "Basic View", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("Frame", "Name of profile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Frame", "Root", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("Frame", "Path of folder to watch", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Frame", "Periodic (min)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Frame", "Max Threads", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Frame", "Recursive watch", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Frame", "Autostart", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Frame", "cmdall Fallback", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Frame", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Frame", "Errors:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Frame", "Conflicts:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Frame", "Events:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Frame", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Frame", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Frame", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Frame", "Not Running", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Frame", "Profile Type: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Frame", "Unison", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Frame", "Threads:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Frame", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Frame", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Frame", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Frame", "Startup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Frame", "Shutdown", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Frame", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Frame", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd_startup.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd_shutdown.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_7.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Frame", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Frame", "Modify", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_8.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Frame", "Periodic", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd_periodic.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Frame", "New Macro", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd_macro.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Frame", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Frame", "Any Event", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd_all.setPlaceholderText(QtGui.QApplication.translate("Frame", "Type Shell Command Here", None, QtGui.QApplication.UnicodeUTF8))

