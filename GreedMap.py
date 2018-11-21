#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: King-ofwolf
# @Date:   2018-11-21 21:51:13
# @Last Modified by:   King-ofwolf
# @Last Modified time: 2018-11-22 00:09:40
# @Email:	wangshengling@buaa.edu.cn
'Info: a Python file '
__author__ = 'Wang'

from functools import partial

def GreedMap(Gt,Nt,T,packNodeFirst,cost_function):
	#initiallize
	S=[-1 for i in range(Nt.node_size*Nt.core_size)]
	node_last=0
	#loop
	for t in T:
		K=[i for i in Nt.getnodecore(node_last) if S[i]==-1]	#if core i in node_last is free(-1) then add to K
		if packNodeFirst & (len(K)!=0):	#if packNodeFirst is True and node_last has free cores(K)
			pass
		else:
			#for every node in closest_free_nodes get free cores
			for pnode in closest_free_node(Nt,S,node_last):
				for pcore in get_node_free_cores(Nt,S,pnode):
					cores.append(pcore)	
			#for every usable core, caculate cost and choose the mincost cores add to K
			for pcore in cores:
				S_temp=S[:]
				S_temp[pcore]=t 	#try to map task t to pcore
				


def closest_free_node(Nt,S,pnode):
	nodes=[]
	mindistance=Nt.getnodedistance(pnode,0)
	mindistance=mindistance==0?Nt.getnodedistance(pnode,1):mindistance
	for i in range(Nt.node_size):
		if i==pnode:
			continue
		else:
			freecores=get_node_free_cores(Nt,S,pnode)
			distance=Nt.getnodedistance(pnode,i)
			if (len(freecores)==0)|(distance>mindistance):
				continue
			else:
				if distance==mindistance:
					nodes.append(i)
				else:
					nodes=[i]
	return nodes

def get_node_free_cores(Nt,S,pnode):
	cores=Nt.getnodecore(pnode)
	freecores=[]
	for i in cores:
		if S[i]==-1:
			freecores.append(i)
	return freecores