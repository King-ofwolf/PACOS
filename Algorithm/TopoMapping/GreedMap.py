#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: King-ofwolf
# @Date:   2018-11-21 21:51:13
# @Last Modified by:   King-ofwolf
# @Last Modified time: 2018-12-03 17:43:40
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
	S=[-1 for i in range(Gn.ct_size)]
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
			node_cores=[]
			closest_free_nodes=closest_free_node(Gn,S,node_last)
			for pnode in closest_free_nodes:
				for pcore in get_node_free_cores(Gn,S,pnode):
					cores.append(pcore)	
				if cores!=[]:
					node_cores.append(tuple(cores))
					cores=[]
			if closest_free_nodes==[] and not packNodeFirst:	#if not pack node first and no closest free node, the node will be node last use
				for pcore in get_node_free_cores(Gn,S,node_last):
					cores.append(pcore)
				if cores!=[]:
					node_cores.append(tuple(cores))
					cores=[]
			if node_cores==[]:
				print("no free cores:%d"%t)
				return S
			#for every usable core, caculate cost and choose the mincost cores add to K
			node_cost=[]
			for pnode in node_cores:
				pcore=pnode[0]
				S_temp=S[:]
				S_temp[pcore]=t 	#try to map task t to pcore
				node_cost.append(cost_function(Gt,Gn,S_temp,t))
			node_cost_sorted=sorted(node_cost)	#sorted by cores cost 
			mincost=node_cost_sorted[0]		#first core is the lowest cost core
			for p in range(len(node_cost_sorted)):
				if node_cost_sorted[p]==mincost:	#with the same cost of the first core, add it to K
					K.extend(node_cores[p])
				else:
					break
			# for pnode_cost in node_cost_sorted:
			# 	if pnode_cost==mincost:		
			# 		K.append(pcore_cost[0])
			# 	else:
			# 		break
		pcore=K[randint(0,len(K)-1)]	#choose a random core from K as p
		S[pcore]=t 		#map t to p
		#print("set t:%d to S[%d]"%(t,pcore))
		node_last=Gn.getnodeoder(pcore)		#last used node is p's node
	return S
	
