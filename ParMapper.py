#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2018-11-20 18:34:53
# @Last Modified by:   King-ofwolf
# @Last Modified time: 2018-11-21 22:15:58
# @Email:	wangshengling@buaa.edu.cn
'Info: a Python file '
__author__ = 'Wang'

from collections import Iterable

class TaskGraph(object):
	"""docstring for TaskGraph"""
	def __init__(self, IOstream, size):
		super(TaskGraph, self).__init__()
		TGlist=[0 for i in range(self.__locat(size-1,size-1)+1)]	#initial TGlist
		self.__size=size
		if isinstance(IOstream,Iterable)&('read' in dir(IOstream)):	#IOstream is Iterable and has 'read' function
			try:
				for lines in IOstream:	#for every lines in IOstream,
					(i,j)=lines.strip().split()
					if i=='#':
						m=int(j)
					else:
						n=int(i)
						TGlist[self.__locat(m,n)]=int(j)
			except Exception as e:
				raise
			finally:
				pass
		self.__TGmatrix=tuple(TGlist)

	def getweight(self,i,j):
		if isinstance(i,int)&isinstance(j,int):
			if (i>=0) & (i<self.__size) & (j>=0) & (j<self.__size):
				return self.__TGmatrix[self.__locat(i,j)]
			else:
				return 0
		else:
			raise ValueError("i,j is out of exception")

	def __locat(self,i,j):
		if i>=j:
			return int(((i+1)*i)/2+j)
		else:
			return int(((j+1)*j)/2+i)

	@property
	def size(self):
		return self.__size

class NetGraph(object):
	"""docstring for NetGraph"""
	def __init__(self, IOstream, node_size, core_size):
		super(NetGraph, self).__init__()
		NGlist=[]
		item=[]
		self.__node_size=node_size
		self.__core_size=core_size
		if isinstance(IOstream,Iterable) & ('read' in dir(IOstream)):
			try:
				for lines in IOstream:
					NGlist.append(tuple(map(int,lines.strip().split())))
			except Exception as e:
				raise
			finally:
				pass
		self.__NGmatrix=tuple(NGlist)

	def getnodedistance(self,i,j):
		if isinstance(i,int)&isinstance(j,int):
			if (i>=0) & (i<self.__node_size) & (j>=0) & (j<self.__node_size):
				return self.__NGmatrix[i][j]
			else:
				return 0
		else:
			raise ValueError("i,j is out of exception")

	def getnodeoder(self,coreoder):
		return int(coreoder/self.__core_size)
	def getnodecore(self,nodeoder):
		return [i for i in range(nodeoder*self.core_size,(nodeoder+1)*self.core_size)]

	@property
	def node_size(self):
		return self.__node_size
	@property
	def core_size(self):
		return self.__core_size


if __name__ == '__main__':
	with open('CloverLeaf128ProcessTopology_Volume.lgl','r') as tgf:
		taskgraph=TaskGraph(tgf,128)
		print("tgf:%d,%d:%d"%(1,2,taskgraph.getweight(1,2)))
	with open('MapGraph.txt','r') as ngf:
		netgraph=NetGraph(ngf,48,24)
		print("ngf:%d,%d:%d"%(1,2,netgraph.getnodedistance(1,2)))
	print(netgraph.getnodecore(0))
