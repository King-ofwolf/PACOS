#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-20 16:15:11
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-21 09:52:32
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-20 16:15:11'

import random
from pyecharts import HeatMap

def GenerateHeatMap(matrix,outpath="./taskgraph.html"):
	matrix_len=len(matrix)
	x_axis = [str(i) for i in range(matrix_len)]
	y_axis = [str(i) for i in range(matrix_len)]
	data = [[i,j,matrix[i][j]] for i in range(matrix_len) for j in range(matrix_len)]
	matrix_min=0
	matrix_max=0
	for line in matrix:
		for item in line:
			if item > matrix_max:
				matrix_max = item



	heatmap = HeatMap(title = "Task communication Graph")
	heatmap.add("Task communication Graph",
		x_axis,y_axis,data,
		lable_pos='bottom',
		lable_color='#000000',
		is_visualmap=True,
		visual_text_color="#000000",
		visual_orient="vertical",
		visual_range=[matrix_min,matrix_max],
		visual_range_text=['low','high'],
		visual_range_color=['#FFFFFF','#555555','#000000'],
		visual_top = 1,
		visual_pos = 'right',	#right
		is_toolbox_show=False)
	heatmap.render(outpath)


if __name__ == '__main__':
	matrix = [[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0],
	[1,2,3,4,5,6,7,8,9,0]]
	GenerateHeatMap(matrix)