#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 20:32:56
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-04-14 19:24:42
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 20:32:56'

import ctypes
import os
from TopoMapping import ParMapper
from Run_log import Sys_logger
from Graph import TaskGraph
from Graph import MapGraph

TOPOMAPPING=1
TREEMATCH=2
MPIPP=3
ALGORITHM_NAME=["Unknow","TopoMapping","TreeMatch","MPIPP"]
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

def Load_task_graph_MPIPP(filepath):
	return Load_task_graph_MAT(filepath)

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

def Load_net_graph_xml(filepath):
	if '.xml' in filepath:
		return 1
	else :
		return None

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

def Algorithm_run(algotype,Tgfile,Ngfile,**kw):
	if algotype == TOPOMAPPING:
		if "configures" in kw:
			result=Algorithm_run_TopoMapping(Tgfile,Ngfile,kw["task_size"],kw["net_ct"],kw["net_node"],kw["net_core"],kw["configures"])
		else:
			result=Algorithm_run_TopoMapping(Tgfile,Ngfile,kw["task_size"],kw["net_ct"],kw["net_node"],kw["net_core"])
	elif algotype == MPIPP:
		result=Algorithm_run_MPIPP(Tgfile,Ngfile,kw["nfile_type"],kw["ct"],kw["node"],kw["core"])
	elif algotype == TREEMATCH:
		bind_file = kw["bind_file"] if "bind_file" in kw else ''
		optimization = kw["optimization"] if "optimization" in kw else True
		metric = kw["metric"] if "metric" in kw else 1
		result=Algorithm_run_TREEMATCH(Tgfile,Ngfile,kw["nfile_type"],bind_file,optimization,metric)

	MapGraph.GenerateScatter(ST=result,outpath="./Graph/mapgraph.html")
	return result

def Algorithm_run_TopoMapping(Tgfile,Ngfile,task_size,net_ct,net_node,net_core,configures=[]):
	#tasklists=ParMapper.TaskList(Tg)
	result_S=ParMapper.main(Tgfile,Ngfile,task_size,net_ct,net_node,net_core,debug_mode=False,resultfile='./TopoMapping_Result.ST')
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

def Algorithm_run_TREEMATCH(Tgfile,Ngfile,nfile_type,bind_file='',optimization=True,metric=1):
	#-t|x <Architecture file[tgt|xml]>
	#-c <Communication pattern file> 
	#[-b <binding constraint file>]
	#[-d disable topology optimization]
	#[-m evaluation metric (1: SUM_COM (default), 2: MAX_COM, 3: HOP_BYTE)]
	shell_command="./TreeMatch/mapping"
	if nfile_type == '.xml':
		shell_command+=" -x "+str(Ngfile)
	elif nfile_type == '.tgt':
		shell_command+=" -t "+str(Ngfile)
	else:
		Sys_logger.info("Ngfile type not true:%s"%(nfile_type))

	shell_command+=" -c "+str(Tgfile)

	if bind_file != '':
		shell_command+=" -b "+str(bind_file)
	if not optimization :
		shell_command+=" -d"
	if metric == 2:
		shell_command+=" -m 2"
	elif metric == 3:
		shell_command+=" -m 3"

	shell_command="echo $("+shell_command+") > ./TreeMatch_Result.ST"

	shell_state=os.system(shell_command)
	if shell_state != 0:
		Sys_logger.debug("shell command:"+shell_command+" run error with code:%d"%(shell_state))
		Sys_logger.info("TreeMatch run error!")
		raise Exception("shell command:"+shell_command+" run error with code:%d"%(shell_state))
	with open("./TreeMatch_Result.ST",'r') as rf:
		for lines in rf:
			linesplit=lines.strip().split()
			if linesplit[0] == 'TreeMatch:':
				Result=linesplit[1].split(',')
	Result = [int(i) for i in Result]
	return Result

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