#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-04-04 16:55:08
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-04-08 16:36:31
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-04-04 16:55:08'

from pyecharts import Scatter

def GenerateScatter(ST,outpath='./mapgraph.html'):
	taskNo = [i for i in range(len(ST))]
	netNo=ST

	x=taskNo
	y=netNo
	symbol_size=(10-len(x)/100) if len(x)<1000 else 1
	scatter = Scatter(title="Topology Mapping Scatter",subtitle="x:task No.\ny:core No.")
	scatter.add("core No.", x, y,
		symbol_size=symbol_size,
		is_toolbox_show=False,
		)
	scatter.render(outpath)

if __name__ == '__main__':
	st=[23,17,15,9,19,5,14,13,12,10,6,3,21,7,16,2,4,18,0,22,20,1,8,11,85,76,95,89,78,81,91,86,74,88,77,92,90,84,79,83,73,72,93,75,87,94,82,80,59,48,68,55,49,58,56,50,71,67,61,66,65,69,63,57,54,70,60,64,52,53,51,62,40,44,45,37,27,38,25,34,43,41,35,31,32,39,26,28,30,47,33,36,29,46,42,24,115,97,106,116,98,112,99,96,103,100,105,113,119,102,114,118,110,109,111,117,104,101,108,107,127,122,121,125,123,120,124,126]
	GenerateScatter(st)

