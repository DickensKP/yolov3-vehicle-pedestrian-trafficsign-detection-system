# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '副车辆.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class fucheliang(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1060, 862)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 1011, 771))
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        palette = QtGui.QPalette()
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(38, 32, 107))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        self.label.setStyleSheet("background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(38, 32, 107, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-left-radius:40px;\n"
"border-bottom-left-radius:40px;\n"
"\n"
"border-bottom-right-radius:40px;\n"
"\n"
"border-top-right-radius:40px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton2_3 = QtWidgets.QPushButton(Form)
        self.pushButton2_3.setGeometry(QtCore.QRect(940, 750, 61, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton2_3.setFont(font)
        self.pushButton2_3.setStyleSheet("QPushButton{\n"
"        \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 63, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius:15px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 12, 83, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:7px;\n"
"padding-left:7px;\n"
"}")
        self.pushButton2_3.setObjectName("pushButton2_3")
        self.pushButton2_5 = QtWidgets.QPushButton(Form)
        self.pushButton2_5.setGeometry(QtCore.QRect(90, 700, 121, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton2_5.setFont(font)
        self.pushButton2_5.setStyleSheet("QPushButton{\n"
"        \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 63, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius:15px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 12, 83, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:7px;\n"
"padding-left:7px;\n"
"}")
        self.pushButton2_5.setObjectName("pushButton2_5")
        self.pushButton2_6 = QtWidgets.QPushButton(Form)
        self.pushButton2_6.setGeometry(QtCore.QRect(90, 750, 121, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton2_6.setFont(font)
        self.pushButton2_6.setStyleSheet("QPushButton{\n"
"        \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 63, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius:15px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 12, 83, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:7px;\n"
"padding-left:7px;\n"
"}")
        self.pushButton2_6.setObjectName("pushButton2_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 730, 691, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton2_4 = QtWidgets.QPushButton(Form)
        self.pushButton2_4.setGeometry(QtCore.QRect(20, 750, 61, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton2_4.setFont(font)
        self.pushButton2_4.setStyleSheet("QPushButton{\n"
"        \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 63, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius:15px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 12, 83, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:7px;\n"
"padding-left:7px;\n"
"}")
        self.pushButton2_4.setObjectName("pushButton2_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 971, 621))
        self.label_2.setStyleSheet("\n"
"border-top-left-radius:40px;\n"
"border-bottom-left-radius:40px;\n"
"\n"
"border-bottom-right-radius:40px;\n"
"\n"
"border-top-right-radius:40px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton2_9 = QtWidgets.QPushButton(Form)
        self.pushButton2_9.setGeometry(QtCore.QRect(940, 700, 61, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton2_9.setFont(font)
        self.pushButton2_9.setStyleSheet("QPushButton{\n"
"        \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 63, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius:15px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 12, 83, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:7px;\n"
"padding-left:7px;\n"
"}")
        self.pushButton2_9.setObjectName("pushButton2_9")
        self.pushButton2_12 = QtWidgets.QPushButton(Form)
        self.pushButton2_12.setGeometry(QtCore.QRect(20, 700, 61, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton2_12.setFont(font)
        self.pushButton2_12.setStyleSheet("QPushButton{\n"
"        \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 63, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius:15px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 12, 83, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:7px;\n"
"padding-left:7px;\n"
"}")
        self.pushButton2_12.setObjectName("pushButton2_12")

        self.retranslateUi(Form)
        self.pushButton2_3.clicked.connect(Form.close)
        self.pushButton2_9.clicked.connect(self.label_2.clear)
        self.pushButton2_9.clicked.connect(self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton2_3.setText(_translate("Form", "返回"))
        self.pushButton2_5.setText(_translate("Form", "选择图片"))
        self.pushButton2_6.setText(_translate("Form", "选择视频"))
        self.pushButton2_4.setText(_translate("Form", "处理"))
        self.pushButton2_9.setText(_translate("Form", "清空"))
        self.pushButton2_12.setText(_translate("Form", "处理"))
import resource_rc
