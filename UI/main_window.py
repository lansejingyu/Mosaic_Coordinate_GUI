# -*- coding: utf-8 -*-

# MainWindow implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setFixedSize(900, 538)
		self.widget = QtWidgets.QWidget(MainWindow)
		self.widget.setGeometry(QtCore.QRect(10, 20, 881, 81))
		self.widget.setObjectName("widget")
		self.label = QtWidgets.QLabel(self.widget)
		self.label.setGeometry(QtCore.QRect(10, 10, 301, 16))
		self.label.setObjectName("label")
		self.widget1 = QtWidgets.QWidget(self.widget)
		self.widget1.setGeometry(QtCore.QRect(11, 50, 861, 25))
		self.widget1.setObjectName("widget1")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_10.setObjectName("horizontalLayout_10")
		self.horizontalLayout.addLayout(self.horizontalLayout_10)
		self.label_2 = QtWidgets.QLabel(self.widget1)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout.addWidget(self.label_2)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.horizontalLayout.addLayout(self.horizontalLayout_4)
		self.lineEdit = QtWidgets.QLineEdit(self.widget1)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
		self.horizontalLayout.addWidget(self.lineEdit)
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.horizontalLayout.addLayout(self.horizontalLayout_5)
		self.pushButton = QtWidgets.QPushButton(self.widget1)
		self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.horizontalLayout.addLayout(self.horizontalLayout_6)
		self.widget_2 = QtWidgets.QWidget(MainWindow)
		self.widget_2.setGeometry(QtCore.QRect(10, 130, 881, 181))
		self.widget_2.setObjectName("widget_2")
		self.label_3 = QtWidgets.QLabel(self.widget_2)
		self.label_3.setGeometry(QtCore.QRect(10, 10, 211, 16))
		self.label_3.setObjectName("label_3")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
		self.lineEdit_3.setGeometry(QtCore.QRect(10, 110, 781, 60))
		self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.lineEdit_3.setDragEnabled(False)
		self.lineEdit_3.setReadOnly(False)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.label_6 = QtWidgets.QLabel(self.widget_2)
		self.label_6.setGeometry(QtCore.QRect(10, 40, 801, 16))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self.widget_2)
		self.label_7.setGeometry(QtCore.QRect(10, 70, 601, 16))
		self.label_7.setObjectName("label_7")
		self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
		self.pushButton_4.setGeometry(QtCore.QRect(800, 110, 75, 60))
		self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.pushButton_4.setStyleSheet("background-color: rgb(170, 255, 255);\n"
										"font: 18pt \"Adobe Devanagari\";")
		self.pushButton_4.setObjectName("pushButton_4")
		self.widget_3 = QtWidgets.QWidget(MainWindow)
		self.widget_3.setGeometry(QtCore.QRect(10, 320, 881, 91))
		self.widget_3.setObjectName("widget_3")
		self.label_4 = QtWidgets.QLabel(self.widget_3)
		self.label_4.setGeometry(QtCore.QRect(10, 10, 500, 16))
		self.label_4.setObjectName("label_4")
		self.widget2 = QtWidgets.QWidget(self.widget_3)
		self.widget2.setGeometry(QtCore.QRect(11, 51, 861, 25))
		self.widget2.setObjectName("widget2")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_11.setObjectName("horizontalLayout_11")
		self.horizontalLayout_2.addLayout(self.horizontalLayout_11)
		self.label_5 = QtWidgets.QLabel(self.widget2)
		self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout_2.addWidget(self.label_5)
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
		self.lineEdit_2 = QtWidgets.QLineEdit(self.widget2)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
		self.horizontalLayout_2.addWidget(self.lineEdit_2)
		self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
		self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
		self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 255);")
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_2.addWidget(self.pushButton_2)
		self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_9.setObjectName("horizontalLayout_9")
		self.horizontalLayout_2.addLayout(self.horizontalLayout_9)
		self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
		self.pushButton_3.setGeometry(QtCore.QRect(380, 430, 100, 80))
		self.pushButton_3.setStyleSheet("background-color: rgb(170, 255, 255);\n"
										"font: 18pt \"Adobe Devanagari\";")
		self.pushButton_3.setObjectName("pushButton_3")

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow",
									  "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Step01:选择需要查找马赛克的.TIFF文件</span></p></body></html>"))
		self.label_2.setText(_translate("MainWindow",
										"<html><head/><body><p><span style=\" font-size:11pt;\">文件路径：</span></p></body></html>"))
		self.pushButton.setText(_translate("MainWindow", "选择文件"))
		self.label_3.setText(_translate("Form",
										"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Step02：设置马赛克RGB数值</span></p></body></html>"))
		self.label_6.setText(_translate("Form",
										"<html><head/><body><p><span style=\" font-size:11pt;\">输入多个RGB值时，每一组RGB值之间用英文分号“;”隔开，如：255,255,255;0,0,0，输入完后，请点击“设置”按钮。</span></p></body></html>"))
		self.label_7.setText(_translate("Form",
										"<html><head/><body><p><span style=\" font-size:11pt;\">默认RGB值有:255,255,255;0,0,0;128,128,128</span></p></body></html>"))
		self.pushButton_4.setText(_translate("MainWindow", "设置"))
		self.label_4.setText(_translate("MainWindow",
										"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Syep03：设置马赛克坐标文件结果导出存储路径,Shapefil格式。</span></p></body></html>"))
		self.label_5.setText(_translate("MainWindow",
										"<html><head/><body><p><span style=\" font-size:11pt;\">结果存储路径：</span></p></body></html>"))
		self.pushButton_2.setText(_translate("MainWindow", "选择路径"))
		self.pushButton_3.setText(_translate("MainWindow", "开始执行"))
