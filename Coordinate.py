# -*- coding: utf-8 -*-
# @Project : GIS-Mosaic
# @File : 123
# @IDE：PyCharm
# @Author : KT15
# @Time : 2023-04-20 17:08

from main import *
import rasterio.sample, rasterio.vrt, rasterio._features
from osgeo import gdal
import numpy as np
import csv
import pandas as pd
import pyproj
from decimal import Decimal
import geopandas
import os
import shutil


# 行y，列x都从0开始

class MosaicCoordinate(object):
	def __init__(self):
		pass

	def TIF_files(path):
		global dataset
		global dataset_rasterio
		global data2
		global col
		global row
		File_Path = path
		print("TIF路径:", File_Path)
		dataset = gdal.Open(File_Path)
		dataset_rasterio = rasterio.open(File_Path)

		col = dataset.RasterXSize
		row = dataset.RasterYSize
		# print(col, row)
		area = dataset.ReadAsArray(0, 0, col, row)
		data = np.reshape(area, (-1, col * row))

		data2 = data.T  # type(data2) = numpy.ndarray
		print(data2)

	# ----------------------------------保存用户输入的RGB值到csv文件----------------------------------
	def Rgb_csv(rgb):
		global RGB_data
		# 保存用户输入的RGB值到csv文件
		with open('./Mosaic RGB.csv', mode='a', newline='') as file:
			writer = csv.writer(file)
			for row in rgb:
				writer.writerow(row)

		# with open('./Mosaic RGB.csv', mode='r') as file:  #读取目标RGB值csv文件
		# 	reader = csv.reader(file)
		# 	data = [row for row in reader]
		# 	print(data)

		# 读取目标RGB值csv文件
		RGB_data = np.loadtxt(r"./Mosaic RGB.csv", delimiter=',', dtype=int)
		print("目标RGB：", RGB_data)

		MosaicCoordinate.Find_coordinate()

	# ----------------------------------查找目标RGB值在TIF中的坐标----------------------------------
	@staticmethod
	def Find_coordinate():
		target_coordinate = []
		for i in range(RGB_data.shape[0]):
			f = np.where((data2 == RGB_data[i]).all(axis=1))
			if f[0].size == 0:
				continue
			target_coordinate.append(f)

		# 将查找结果保存为csv文件
		headers = ['lon', 'lat']
		with open("./Mosaic Coordinate.csv", 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(headers)
			for i in range(len(target_coordinate)):
				for j in range(len(target_coordinate[i][0])):
					if target_coordinate[i][0][j] / col < 1:
						ya = 0
						xa = target_coordinate[i][0][j]
						CenterCoordinates = dataset_rasterio.xy(ya, xa)
						print("结果1:",CenterCoordinates)
						writer.writerow(CenterCoordinates)

					else:
						ya = int(target_coordinate[i][0][j] / col)
						xa = target_coordinate[i][0][j] - col * ya
						CenterCoordinates = dataset_rasterio.xy(ya, xa)
						print("结果2:",CenterCoordinates)
						writer.writerow(CenterCoordinates)

	# ----------------------------------将结果Mosaic Coordinate.csv转为SHP文件----------------------------------
	def Save_csv(path):
		Save_path = path
		print("保存路径:", path)

		while True:
			print("开始获取文件大小")
			file_size = os.path.getsize('./Mosaic Coordinate.csv')  # 获取马赛克坐标csv文件大小
			if file_size == 0:
				print("文件大小<<<<<0")
				continue
			else:
				print("文件大小>>>>>0")
				break

		print("开始读取马赛克坐标csv文件")
		target_csv = geopandas.read_file('./Mosaic Coordinate.csv', encoding='utf-8')  # 读取马赛克坐标csv文件
		print("开始转shp")
		target_csv[['lon', 'lat']] = target_csv[['lon', 'lat']].apply(pd.to_numeric)
		gdf = geopandas.GeoDataFrame(target_csv, geometry=geopandas.points_from_xy(target_csv.lon, target_csv.lat))
		gdf.crs = pyproj.CRS.from_user_input('EPSG:4326')  # 给输出的shp增加投影信息,默认4326
		gdf.to_file(Save_path, driver='ESRI Shapefile', encoding='utf-8')
		print("shp保存成功！")

		# 判断Shapefile文件是否在Save_path路径下存在，如果存在，删除Mosaic Coordinate.csv文件，如果不存在，继续循环等待，直到文件存在，再删除Mosaic Coordinate.csv文件
		while True:
			if os.path.exists(Save_path):
				os.remove('./Mosaic Coordinate.csv')
				print("删除Mosaic Coordinate.csv文件成功！")

				# 打开 CSV 文件并读取所有行
				with open('./Mosaic RGB.csv', mode='r') as file:
					reader = csv.reader(file)
					rows = list(reader)

				# 删除第三行之后的所有数据
				rows = rows[:3]  # 保留前三行数据

				#删除所有数据
				# rows = rows[:0]

				# 重新写入 CSV 文件
				with open('./Mosaic RGB.csv', mode='w', newline='') as file:
					writer = csv.writer(file)
					writer.writerows(rows)
					print("删除Mosaic RGB.csv文件中的数据成功！")

				break
			else:
				continue
