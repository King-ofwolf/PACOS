#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-04-04 16:55:08
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-05-23 16:55:13
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-04-04 16:55:08'

from pyecharts import Scatter
from pyecharts import Tree
import json
import codecs
import os

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

def GenerateTree_json(ST,Net,outpath='./tree.json'):
	mapjson={'treedics':[]}
	treedic={'children':[],'name':''}
	mapjson['treedics'].append(treedic)
	tmp_dic_list=mapjson['treedics'] #all children nodes
	nodes=0
	depath=0
	if Net==[]:
		treedic['name']='No Graph to show'
		nodes=5
	elif Net[0] == 'tleaf':
		netdepth=Net[1]
		for nodes in Net[2:netdepth+1]:
			tmp_list=[]	#new children nodes
			for j in tmp_dic_list:
				for i in range(int(nodes)):
					tmp_dic={'children':[],'name':''}
					j['children'].append(tmp_dic)
					tmp_list.append(tmp_dic)
			tmp_dic_list=tmp_list
		nodes=Net[netdepth+1]
		clk=0
		for j in tmp_dic_list:
			for i in range(int(nodes)):
				j['name']+=str(ST.index(clk))+','
				clk+=1
			j['name']=j['name'][0:-1]
		nodes=len(tmp_dic_list)
		depath=netdepth
	elif Net[0] == 'matrix':
		tcores=Net[1]
		nodes=Net[2]
		cores=Net[3]
		depath=2
		clk=0
		for i in range(nodes):
			treedic['children'].append({'children':[],'name':''})
		for i in treedic['children']:
			for core in range(cores):
				# i['children'].append({'children':[],'name':str(ST.index(clk)),'vaule':clk})
				i['name']+=str(ST.index(clk))+','
				clk+=1
				if clk >=tcores:
					break
			i['name']=i['name'][0:-1]

	with codecs.open(outpath,"w",encoding="utf-8") as f:
		json.dump(mapjson,f,ensure_ascii=False)	
	return nodes,depath

def GenerateTree(ST,Net,outpath='./treegraph.html'):
	outpathdir=os.path.dirname(outpath)
	nodes,depath=GenerateTree_json(ST,Net,outpath=os.path.join(outpathdir,'tree.json'))

	with codecs.open(os.path.join(outpathdir,'tree.json'), "r", encoding="utf-8") as f:
		j = json.load(f)

	data=j['treedics']
	tree = Tree(width=600, height=nodes*20)
	tree.add("Topology Mapping result", data,
		tree_collapse_interval=0,
		tree_right="50%",
		tree_symbol_size=10,
		is_toolbox_show=False)
	tree.render(outpath)


if __name__ == '__main__':
	# st=[23,17,15,9,19,5,14,13,12,10,6,3,21,7,16,2,4,18,0,22,20,1,8,11,85,76,95,89,78,81,91,86,74,88,77,92,90,84,79,83,73,72,93,75,87,94,82,80,59,48,68,55,49,58,56,50,71,67,61,66,65,69,63,57,54,70,60,64,52,53,51,62,40,44,45,37,27,38,25,34,43,41,35,31,32,39,26,28,30,47,33,36,29,46,42,24,115,97,106,116,98,112,99,96,103,100,105,113,119,102,114,118,110,109,111,117,104,101,108,107,127,122,121,125,123,120,124,126]
	# GenerateScatter(st)
	st=[23,17,15,9,19,5,14,13,12,10,6,3,21,7,16,2,4,18,0,22,20,1,8,11,85,76,95,89,78,81,91,86,74,88,77,92,90,84,79,83,73,72,93,75,87,94,82,80,59,48,68,55,49,58,56,50,71,67,61,66,65,69,63,57,54,70,60,64,52,53,51,62,40,44,45,37,27,38,25,34,43,41,35,31,32,39,26,28,30,47,33,36,29,46,42,24,115,97,106,116,98,112,99,96,103,100,105,113,119,102,114,118,110,109,111,117,104,101,108,107,127,122,121,125,123,120,124,126]
	net=['tleaf',4,16,2,2,2]
	net=['matrix',128,7,20]
	# st=[i for i in range(32)]
	# net=['tleaf',4,4,2,2,2]
	GenerateTree(st,net)

