#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 20:32:56
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-22 14:11:45
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 20:32:56'

import ctypes
from TopoMapping import ParMapper
from Run_log import Sys_logger
from Graph import TaskGraph

TOPOMAPPING=1
TREEMATCH=2
MPIPP=3
ParMapper_TgFT = (".APHiD",".TOPO")
ParMapper_NgFT = (".txt",)

TreeMatch_TgFT = (".mat",".MPIPP")
TreeMatch_NgFT = (".tgt",".xml")

MPIPP_TgFT = (".mat",".MPIPP")
MPIPP_NgFT = (".tgt",".txt",".xml")

def Load_task_graph_APHiD(filepath):
	try:
		with open(filepath,'r') as tgf:
			taskgraph=ParMapper.TaskGraph()
			#taskgraph.readgraphfile0(tgf,task_size)
			taskgraph.readgraphfile1(tgf)
			TaskGraph.GenerateHeatMap(matrix=taskgraph.TGmatrix,outpath='./Graph/taskgraph.html')
			return taskgraph
	except Exception as e:
		Sys_logger.debug(str(e))
		Sys_logger.info("task graph read error")
		return None
	finally:
		pass
	
def Load_task_graph_TOPO(filepath):
	return Load_task_graph_APHiD(filepath)

def Load_task_graph_MAT(filepath):
	matrix=[]
	try:
		with open(filepath,'r') as tgf:
			for fline in tgf:
				matrix.append(fline.strip().split())
		TaskGraph.GenerateHeatMap(matrix=matrix,outpath='./Graph/taskgraph.html')
		return matrix
	except Exception as e:
		Sys_logger.debug(str(e))
		Sys_logger.info("task graph read error")
		return None
	finally:
		pass

def Load_net_graph_txt(filepath,ct,node,core):
	try:
		#----------------------------------------------temp data
		net_node=node
		net_core=core
		net_ct=ct
		with open(filepath,'r') as ngf:
			netgraph=ParMapper.NetGraph(ngf,net_ct,net_node,net_core)
			return netgraph
	except Exception as e:
		Sys_logger.debug(str(e))
		Sys_logger.info("net graph read error")
		return None
	finally:
		pass

def Load_net_graph_tgt(filepath):
	try:
		node_num=1
		with open(filepath,'r') as ngf:
			for fline in ngf:
				flines=fline.strip().split()
				if flines[0] != 'tleaf':
					Sys_logger.info("net graph read error : tleaf not find!")
					return None
				maxindex=int(flines[1])
				for node in [int(flines[i]) for i in range(2,maxindex*2+2,2)]:
					node_num=node_num*node
				return node_num
	except Exception as e:
		Sys_logger.debug(str(e))
		Sys_logger.info("net graph %s read error"%filepath)
		return None
	finally:
		pass
def Load_result_ST(filepath):
	try:
		result_S=[]
		with open(filepath,'r') as ref:
			for fline in ref:
				result_S.append(int(fline))
		return result_S
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass


def Algorithm_run_TopoMapping(Tgfile,Ngfile,task_size,net_ct,net_node,net_core,configures=[]):
	#tasklists=ParMapper.TaskList(Tg)
	result_S=ParMapper.main(Tgfile,Ngfile,task_size,net_ct,net_node,net_core)
	#result_S=ParMapper.ParMapper(Tg,Ng,tasklists.T,process=4,strategy=ParMapper.default_compare,compare_alf=ParMapper.COMPARE_ALF,cost_function_mode=ParMapper.COST_FUNCTION_MODE)
	#print("result_S:"+str(ParMapper.S2ST(result_S)))
	return ParMapper.S2ST(result_S)

def Algorithm_run_MPIPP(Tgfile,Ngfile,nfile_type,ct,node,core):
	mpippll = ctypes.cdll.LoadLibrary
	mpipplib = mpippll("./MapMPIPP/MPIPP_C2PY.so")
	if nfile_type == '.tgt':
		file_type = 1
	elif nfile_type == '.txt':
		file_type = 0
	elif nfile_type == '.xml':
		file_type = 2
	try:
		arch_filename=str(Ngfile)
		com_filename=str(Tgfile)
		ct=int(ct)
		node=int(node)
		core=int(core)
		mpipplib.MPIPP_MAPPING(arch_filename,file_type,com_filename,ct,node,core)
		return Load_result_ST("./MPIPP_Result.ST")
	except Exception as e:
		Sys_logger.debug(str(e))
		Sys_logger.info("MPIPP_MAPPING run error!")
		raise
	finally:
		pass


def Result_print(result):
	print("result_S:"+str(ParMapper.S2ST(result)))
def Result2Str(result):
	return str(result)


if __name__ == '__main__':  
	ll = ctypes.cdll.LoadLibrary   
	lib = ll("./MapMPIPP/MPIPP_C2PY.so")    
	# lib.Table99(9)
	# lib.Fabocci();
	# Test=lib.Max_value(9,4)
	# print Test
	# lib.printhello()
	# print '***finish***' 
	#void MPIPP_MAPPING(char *arch_filename, int file_type, char *com_filename, int ct, int node, int core)
	arch_filename="./examples/netgraph/TimeCostDataFile_128-7-20.txt"
	arch_filename="./examples/netgraph/128.tgt"
	file_type=1
	com_filename="./examples/taskgraph/128.mat"
	ct=128
	node=7
	core=20
	try:
		lib.MPIPP_MAPPING(arch_filename,file_type,com_filename,ct,node,core)
	except Exception as e:
		print e
		raise
	else:
		pass
	finally:
		print "-----finally------------"
	
	print "----finish-----"