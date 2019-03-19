#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 20:32:56
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-17 21:27:09
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 20:32:56'

import ctypes
from TopoMapping import ParMapper
from Run_log import Sys_logger

TOPOMAPPING=1
TREEMATCH=2
MPIPP=3
ParMapper_TgFT = (".APHiD",".TOPO")
ParMapper_NgFT = (".txt",)

TreeMatch_TgFT = (".mat",".MPIPP")
TreeMatch_NgFT = (".tgf",".xml")

MPIPP_TgFT = (".mat",".MPIPP")
MPIPP_NgFT = (".tgf",".txt",".xml")

def Load_task_graph_APHiD(filepath):
	try:
		with open(filepath,'r') as tgf:
			taskgraph=ParMapper.TaskGraph()
			#taskgraph.readgraphfile0(tgf,task_size)
			taskgraph.readgraphfile1(tgf)
			return taskgraph
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
		raise
		#return None
	finally:
		pass

def Algorithm_run_TopoMapping(Tgfile,Ngfile,task_size,net_ct,net_node,net_core,configures=[]):
	#tasklists=ParMapper.TaskList(Tg)
	result_S=ParMapper.main(Tgfile,Ngfile,task_size,net_ct,net_node,net_core)
	#result_S=ParMapper.ParMapper(Tg,Ng,tasklists.T,process=4,strategy=ParMapper.default_compare,compare_alf=ParMapper.COMPARE_ALF,cost_function_mode=ParMapper.COST_FUNCTION_MODE)
	#print("result_S:"+str(ParMapper.S2ST(result_S)))
	return result_S

def Result_print(result):
	print("result_S:"+str(ParMapper.S2ST(result)))
def Result2Str(result):
	return str(ParMapper.S2ST(result))


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