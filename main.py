# -*- coding: utf-8 -*-
# @Project : Mosaic Coordinate_GUI
# @File : main
# @IDE：PyCharm
# @Author : KT15
# @Time : 2023-04-27 16:06

import os
import sys
from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QEventLoop
from UI.main_window import *
from Coordinate import *
from UI.Task_status import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.plainTextEdit = None
		self.setupUi(self)
		self.setWindowTitle('GIS-Mosaic Coordinate       By ZhangLei 2023')  # main_window的名字

		#给界面左上角添加图标
		icon = QIcon()
		icon.addPixmap(QPixmap("./favicon.ico"), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)

		self.Task_accomplished = Task_status_windows()

		self.pushButton.clicked.connect(self.open_file)

		self.pushButton_2.clicked.connect(self.save_file)

		self.pushButton_3.clicked.connect(self.file_path)

		self.pushButton_4.clicked.connect(self.RGB)

	def open_file(self):  # 打开tif文件并获取显示路径
		global open_file_path
		self.fname, self.ftype = QFileDialog.getOpenFileName(self, '选择影像文件', 'C:/',
															 "影像文件类型 (*.tif )")  # str
		self.lineEdit.setText(self.fname)  # 将获取到的文件路径显示在lineEdit中
		self.lineEdit.setStyleSheet("color:black")
		open_file_path = self.fname

	def save_file(self):  # 保存shp文件并获取显示路径
		global save_file_path
		self.save_file_path = QFileDialog.getSaveFileName(self, '保存路径', 'C:/', "保存类型 (*.shp )")
		self.lineEdit_2.setText(self.save_file_path[0])
		self.lineEdit_2.setStyleSheet("color:black")
		save_file_path = self.save_file_path[0]

	# print(save_file_path)

	def RGB(self):
		global rgb
		if self.lineEdit_3.text() != '':
			# 在上面的if下再增加一个条件：如果lineEdit_3输入的格式为%,%,%,则执行下面的代码，否则提示输入正确的格式
			# rgb_values = self.lineEdit_3.text().split(";")
			for value in self.lineEdit_3.text().split(";"):
				values = value.split(",")
				if len(values) != 3 or '' in values:
					self.lineEdit_3.setText(
						'请按照上面的提示，输入正确RGB格式，每组RGB值包含3个0-255之间的整数，用英文逗号隔开!')
					self.lineEdit_3.setStyleSheet("color:red")
					break

				else:
					self.rgb = self.lineEdit_3.text()
					rgb_tuple = []
					for value in self.lineEdit_3.text().split(";"):
						rgb_tuple.append(tuple(map(int, value.split(","))))
					self.rgb = tuple(rgb_tuple)
					rgb = self.rgb
		else:
			self.lineEdit_3.setText('不能为空，请输入任意一组RGB值!')
			self.lineEdit_3.setStyleSheet("color:red")

	def file_path(self):  # 传递选择的tif文件路径和保存的shp文件路径
		if self.lineEdit.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '':
			# 阻塞按钮信号，防止多次点击而崩溃
			# self.pushButton_3.blockSignals(True)
			if self.lineEdit.text() == '':
				self.lineEdit.setText('请选择.TIFF文件!')
				self.lineEdit.setStyleSheet("color:red")
			if self.lineEdit_2.text() == '':
				self.lineEdit_2.setText('请选择保存路径!')
				self.lineEdit_2.setStyleSheet("color:red")
			if self.lineEdit_3.text() == '':
				self.lineEdit_3.setText('不能为空，请输入任意一组RGB值!')
				self.lineEdit_3.setStyleSheet("color:red")

		elif self.lineEdit.text() == '请选择.TIFF文件!' and self.lineEdit_2.text() == '请选择保存路径!' and self.lineEdit_3.text() == '不能为空，请输入任意一组RGB值!' or self.lineEdit_3.text() == '请按照上面的提示，输入正确RGB格式，每组RGB值包含3个0-255之间的整数，用英文逗号隔开!':
			pass

		else:
			MosaicCoordinate.TIF_files(open_file_path)
			MosaicCoordinate.Rgb_csv(rgb)
			MosaicCoordinate.Save_csv(save_file_path)
			self.start_progress()

	def start_progress(self):  # 置灰按钮状态
		# self.pushButton.setEnabled(False)
		# self.pushButton_2.setEnabled(False)
		# self.pushButton_3.setEnabled(False)
		# self.pushButton_4.setEnabled(False)
		self.Task_status()

	def Task_status(self):
		count = 0
		while not os.path.exists(save_file_path):
			count += 1
		if os.path.exists(save_file_path):
			self.Task_accomplished.show()


# def update_progress(self):  #恢复按钮状态
# 	self.pushButton.setEnabled(True)
# 	self.pushButton_2.setEnabled(True)
# 	self.pushButton_3.setEnabled(True)
# 	self.pushButton_4.setEnabled(True)


class Task_status_windows(QDialog, Ui_Dialog):
	def __init__(self):
		super(Task_status_windows, self).__init__()
		self.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = MyMainWindow()

	main.show()
	sys.exit(app.exec_())
