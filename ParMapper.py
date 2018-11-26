#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2018-11-20 18:34:53
# @Last Modified by:   kingofwolf
# @Last Modified time: 2018-11-26 17:52:12
# @Email:	wangshengling@buaa.edu.cn
'Info: a Python file '
__author__ = 'Wang'

from collections import Iterable
from multiprocessing import Pool
from GreedMap import GreedMap
import sys, getopt
import logging
logging.basicConfig(level=logging.INFO,
					format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename='ParMapper.log',
					filemode='w')
logger=logging.getLogger()

class TaskGraph(object):
	"""docstring for TaskGraph"""
	def __init__(self, IOstream, size):
		super(TaskGraph, self).__init__()
		TGlist=[0 for i in range(self.__locat(size-1,size-1)+1)]	#initial TGlist
		TGadj_matrix=[[] for i in range(size)]
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
						TGadj_matrix[m].append(n)
			except Exception as e:
				raise
			finally:
				pass
		self.__TGadj_matrix=TGadj_matrix
		self.__TGmatrix=tuple(TGlist)
		logger.info("TaskGraph initial done:size %d"%self.__size)
		logger.debug("TaskGraph:\n"+str(self))

	def getweight(self,i,j):
		if isinstance(i,int)&isinstance(j,int):
			if (i>=0) & (i<self.__size) & (j>=0) & (j<self.__size):
				return self.__TGmatrix[self.__locat(i,j)]
			else:
				return 0
		else:
			raise ValueError("i,j is out of exception")
	def getadj(self,i):
		if (i>=0) & (i<self.__size) :
			return tuple(self.__TGadj_matrix[i])
		else:
			return ()

	def __locat(self,i,j):
		if i>=j:
			return int(((i+1)*i)/2+j)
		else:
			return int(((j+1)*j)/2+i)
	def __str__(self):
		matrix_str=""
		for i in range(self.__size):
			for j in range(self.__size):
				matrix_str+=str(self.getweight(i,j))+" "
			matrix_str+="\n"
		return matrix_str

	@property
	def size(self):
		return self.__size

	def getlist(self):
		return [i for i in range(self.__size)]

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
		logger.info("NetGraph initial done: node_size:%d,core_size:%d"%(self.__node_size,self.__core_size))
		logger.debug("NetGraph:\n"+str(self))

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

	def __str__(self):
		netstr=""
		for line in self.__NGmatrix:
			netstr+=str(line)+"\n"
		return netstr

	@property
	def node_size(self):
		return self.__node_size
	@property
	def core_size(self):
		return self.__core_size

class TaskList(object):
	"""docstring for TaskList"""
	def __init__(self,TG,*,files=[]):
		super(TaskList, self).__init__()
		self.__T=[]
		self.__T.append(self.OO(TG))
		self.__T.append(self.BFS(TG))
		self.__T.append(self.BFS_DFS(TG))
		#self.__T.append(self.GPART(TG))
		self.FileAnalysis(TG,files)
		logger.info("Task initial done")
		logger.debug("Task_orders:\n"+str(self))


	def OO(self,TG):
		Tlist=[i for i in range(TG.size)]
		return tuple(Tlist)
	def BFS(self,TG):
		Tlist=[]
		for base in TG.getlist():
			for ext in TG.getadj(base):
				if ext in Tlist:
					continue
				else:
					Tlist.append(ext)
		return tuple(Tlist)
	def BFS_DFS(self,TG):
		Tlist=[]
		searched=[]
		def DFS(nextT):
			for ext in TG.getadj(nextT):	#BFS
				if ext in searched:
					continue
				else:
					searched.append(ext)
					DFS(ext)
					Tlist.append(ext)		#DFS
		searched.append(0)
		DFS(0)
		Tlist.append(0)
		return tuple(Tlist)
	def GPART(self,TG):
		Tlist=[]
		pass
		return tuple(Tlist)

	def FileAnalysis(self,TG,files):
		for f in files:
			if isinstance(f,Iterable) & ('read' in dir(f)):
				try:
					Tlist=tuple(map(int,f.read().strip().split()))
					if TG.getlist()==sorted(Tlist):
						self.__T.append(Tlist)
					else:
						print('list:',Tlist,' is not available')

				except Exception as e:
					raise
				finally:
					pass

	def __str__(self):
		Tstr="task_order:"
		for t in self.__T:
			for i in t:
				Tstr+=str(i)+" "
			Tstr+="\ntask_order:"
		return Tstr
	@property
	def T(self):
		return self.__T

def Hopbytes(Gt,Gn,S):
	hopbyteslist=[]
	tasklist=[t for t in S if t!=-1]

	#caculate the hopbytes of each task in tasklist
	for t in tasklist:
		hopbytes=0
		tcore=S.index(t)
		for u in tasklist:
			if u==t:
				continue
			ucore=S.index(u)
			weight=Gt.getweight(u,t)
			distance=Gn.getnodedistance(Gn.getnodeoder(ucore),Gn.getnodeoder(tcore))
			hopbytes+=weight*distance
		hopbyteslist.append((t,hopbytes))
	return hopbyteslist

def Loads(Gt,Gn,S):
	#caculate the load of each node, because the property of fat-tree net struct
	#this only useful for fat-tree
	loadlist=[0 for pnode in range(Gn.node_size)]
	tasklist=[t for t in S if t!=-1]
	for t in tasklist:
		tnode=Gn.getnodeoder(S.index(t))
		for u in tasklist:
			if u==t:
				continue
			unode=Gn.getnodeoder(S.index(u))
			if unode==tnode:
				continue
			weight=Gt.getweight(u,t)
			loadlist[tnode]+=weight
	return loadlist

def cost_function(Gt,Gn,S,task):
	#caculate the hopbytes of each task in tasklist
	hopbyteslist=Hopbytes(Gt,Gn,S)
	hopbytes=hopbyteslist[list(map(lambda x:x[0],hopbyteslist)).index(task)][1]
	maxhopbytes=sorted(hopbyteslist,key=lambda x:x[1],reverse=True)[0][1]

	#caculate the load of each node, because the property of fat-tree net struct
	#this only useful for fat-tree
	loadlist=Loads(Gt,Gn,S)
	maxload=sorted(loadlist,reverse=True)[0]

	# the cost of S
	#?????????????????
	return hopbytes+maxload

def default_compare(Gt,Gn,Slist,a=1):
	clist=[]
	#for each S in Slist, caculate their average hopbytes and max hopbytes
	for S in Slist:
		hopbyteslist=Hopbytes(Gt,Gn,S)
		ave_hopbytes=sum([hop[1] for hop in hopbyteslist])/len(hopbyteslist)
		max_hopbytes=max([hop[1] for hop in hopbyteslist])
		clist.append((ave_hopbytes,max_hopbytes))
	ave_h0=sorted(clist,key=lambda x:x[0])[0]	#h0:sorted by average hopbytes
	sort_clist=sorted(clist,key=lambda x:x[1])	#sorted by max hopbytes
	return Slist[clist.index(sort_clist[0])]

def ParMapper(Gt,Gn,TList,process=10,strategy=default_compare):
	pool=Pool(process)
	configures=[]
	pool_result=[]
	Slist=[]
	#GreedMap(Gt,Gn,T,packNodeFirst,cost_function)
	for T in TList:
		configures.append((Gt,Gn,Tlist,True,cost_function))
		configures.append((Gt,Gn,Tlist,False,cost_function))
	for i in range(process):
		pool_result.append(pool.apply_async(GreedMap,args=configures[i%len(configures)]))
	p.close()
	p.join()
	for pr in pool_result:
		Slist.append(pr.get())
	S=strategy(Gt,Gn,Slist)
	return S

if __name__ == '__main__':
	#bash args
	opts, args = getopt.getopt(sys.argv[1:], "t:n:",["debug","tsize=", "nnode=", "ncore="])
	debug_mode=False
	#initialize 
	task_file="CloverLeaf128ProcessTopology_Volume.lgl"
	net_file="MapGraph.txt"
	task_size=128
	net_node=48
	net_core=24
	#choose option
	for op, value in opts:
		if op == "-t":
			task_file = value
		elif op == "-n":
			net_file = value
		elif op == "--debug":
			debug_mode=True
			logger.setLevel(logging.DEBUG)
		elif op == "--tsize":
			task_size = int(value)
		elif op == "--nnode":
			net_node = int(value)
		elif op == "--ncore":
			net_core = int(value)

	logger.info("task_file:%s,task_size:%d"%(task_file,task_size))
	logger.info("net_file:%s,net_node:%d,net_core:%d"%(net_file,net_node,net_core))
	#read task graph file
	try:
		with open(task_file,'r') as tgf:
			taskgraph=TaskGraph(tgf,task_size)
	except Exception as e:
		print("task graph read error")
		raise
	finally:
		pass
	#read net graph file
	try:
		with open(net_file,'r') as ngf:
			netgraph=NetGraph(ngf,net_node,net_core)
	except Exception as e:
		print("net graph read error")
		raise
	finally:
		pass
	#caculate tasklist
	tasklists=TaskList(taskgraph)

	#debug&test
	if debug_mode:
		T_test=tasklists.T[0]
		logger.debug("T_test:\n"+str(T_test))
		S_test=GreedMap(taskgraph,netgraph,T_test,True,cost_function)
		print(S_test)
	#GreedMap(Gt,Gn,T,packNodeFirst,cost_function)