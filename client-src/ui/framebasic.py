# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './profile-basic.ui'
#
# Created: Fri Apr 27 22:56:42 2012
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
        Frame.resize(603, 421)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_22 = QtGui.QLabel(Frame)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_7.addWidget(self.label_22)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_2 = QtGui.QPushButton(Frame)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
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
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtGui.QFrame(Frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(Frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_3 = QtGui.QLineEdit(Frame)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_7 = QtGui.QLineEdit(Frame)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_7 = QtGui.QLabel(Frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spinBox = QtGui.QSpinBox(Frame)
        self.spinBox.setMinimumSize(QtCore.QSize(97, 0))
        self.spinBox.setMaximum(65535)
        self.spinBox.setProperty("value", 22)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.formLayout_3.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.line_3 = QtGui.QFrame(Frame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_6 = QtGui.QLabel(Frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(176, 0))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        self.toolButton_5 = QtGui.QToolButton(Frame)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        self.formLayout_5.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_5 = QtGui.QLabel(Frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(176, 0))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_4.addWidget(self.lineEdit_5)
        self.toolButton_4 = QtGui.QToolButton(Frame)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout_4.addWidget(self.toolButton_4)
        self.formLayout_5.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_4 = QtGui.QLabel(Frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(176, 0))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.toolButton_3 = QtGui.QToolButton(Frame)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.formLayout_5.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.pushButton_3 = QtGui.QPushButton(Frame)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        self.formLayout_5.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.formLayout_5)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(Frame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_9.addWidget(self.line_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
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
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_5 = QtGui.QPushButton(Frame)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.pushButton_7 = QtGui.QPushButton(Frame)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Frame", "Basic View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Frame", "Advanced View", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("Frame", "Name of profile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Frame", "Local sync path:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("Frame", "Path of folder to watch", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Frame", "Server address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Frame", "Server sync path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Frame", "Server ssh port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Frame", "ssh client", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setText(QtGui.QApplication.translate("Frame", "ssh", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setPlaceholderText(QtGui.QApplication.translate("Frame", "Path to ssh client executable", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_5.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Frame", "ssh private key", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setText(QtGui.QApplication.translate("Frame", "id_dsa", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setPlaceholderText(QtGui.QApplication.translate("Frame", "Path of auth key", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Frame", "Unison Path", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setText(QtGui.QApplication.translate("Frame", "unison", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setPlaceholderText(QtGui.QApplication.translate("Frame", "Path to unison executable", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("Frame", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Frame", "Test Connection", None, QtGui.QApplication.UnicodeUTF8))
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

