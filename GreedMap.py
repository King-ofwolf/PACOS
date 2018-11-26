#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: King-ofwolf
# @Date:   2018-11-21 21:51:13
# @Last Modified by:   kingofwolf
# @Last Modified time: 2018-11-26 18:56:50
# @Email:	wangshengling@buaa.edu.cn
'Info: a Python file '
__author__ = 'Wang'

from functools import partial
from random import randint
def closest_free_node(Gn,S,pnode):
	#find the closest nodes with pnode
	nodes=[]
	mindistance=float("inf")
	for i in range(Gn.node_size):
		if i==pnode:
			continue
		else:
			freecores=get_node_free_cores(Gn,S,i)
			distance=Gn.getnodedistance(pnode,i)
			if (len(freecores)==0)|(distance>mindistance):
				continue
			else:
				if distance==mindistance:
					nodes.append(i)
				else:
					mindistance=distance
					nodes=[i]
	return nodes

def get_node_free_cores(Gn,S,pnode):
	cores=Gn.getnodecore(pnode)
	freecores=[]
	for i in cores:
		if S[i]==-1:
			freecores.append(i)
	return freecores
	
def GreedMap(Gt,Gn,T,packNodeFirst,cost_function):
	#initiallize
	S=[-1 for i in range(Gn.node_size*Gn.core_size)]
	node_last=Gn.getnodeoder(0)
	#loop
	for t in T:
		K=[i for i in Gn.getnodecore(node_last) if S[i]==-1]	#if core i in node_last is free(-1) then add to K
		if packNodeFirst & (len(K)!=0):	#if packNodeFirst is True and node_last has free cores(K)
			pass
		else:
			#for every node in closest_free_nodes get free cores
			K=[]
			cores=[]
			for pnode in closest_free_node(Gn,S,node_last):
				for pcore in get_node_free_cores(Gn,S,pnode):
					cores.append(pcore)	
			if cores==[]:
				print("no free cores")
				return S
			#for every usable core, caculate cost and choose the mincost cores add to K
			cores_cost=[]
			for pcore in cores:
				S_temp=S[:]
				S_temp[pcore]=t 	#try to map task t to pcore
				cores_cost.append((pcore,cost_function(Gt,Gn,S_temp,t)))
			cores_cost_sorted=sorted(cores_cost,key=lambda x:x[1])	#sorted by cores cost 
			mincost=cores_cost_sorted[0][1]		#first core is the lowest cost core
			for pcore_cost in cores_cost_sorted:
				if pcore_cost[1]==mincost:		#with the same cost of the first core, add it to K
					K.append(pcore_cost[0])
				else:
					break
		pcore=K[randint(0,len(K)-1)]	#choose a random core from K as p
		S[pcore]=t 		#map t to p
		#print("set t:%d to S[%d]"%(t,pcore))
		node_last=Gn.getnodeoder(pcore)		#last used node is p's node
	return S
	
