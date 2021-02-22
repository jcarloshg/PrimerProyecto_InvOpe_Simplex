# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("#btn_aceptar_1 {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"#btn_aceptar_1:hover {\n"
"    background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"#btn_aceptar_1:pressed {\n"
"    background-color: rgb(200, 200, 200);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 1, 1, 1)
        self.btn_aceptar_1 = QtWidgets.QPushButton(self.page)
        self.btn_aceptar_1.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_aceptar_1.setFont(font)
        self.btn_aceptar_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_aceptar_1.setObjectName("btn_aceptar_1")
        self.gridLayout.addWidget(self.btn_aceptar_1, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.spinVariables = QtWidgets.QSpinBox(self.page)
        self.spinVariables.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.spinVariables.setFont(font)
        self.spinVariables.setMinimum(1)
        self.spinVariables.setMaximum(20)
        self.spinVariables.setObjectName("spinVariables")
        self.gridLayout.addWidget(self.spinVariables, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.spinRestricciones = QtWidgets.QSpinBox(self.page)
        self.spinRestricciones.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.spinRestricciones.setFont(font)
        self.spinRestricciones.setMinimum(1)
        self.spinRestricciones.setMaximum(20)
        self.spinRestricciones.setObjectName("spinRestricciones")
        self.gridLayout.addWidget(self.spinRestricciones, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 2, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 2, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Simplex</p></body></html>"))
        self.btn_aceptar_1.setText(_translate("MainWindow", "Aceptar"))
        self.label.setText(_translate("MainWindow", "Número de variables"))
        self.spinVariables.setPrefix(_translate("MainWindow", " "))
        self.label_2.setText(_translate("MainWindow", "Número de restricciones"))
        self.spinRestricciones.setPrefix(_translate("MainWindow", " "))