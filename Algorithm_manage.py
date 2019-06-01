#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 20:32:56
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-05-28 11:20:23
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 20:32:56'

import ctypes
import os
import time
import datetime
import json
import codecs
from Algorithm.TopoMapping import ParMapper
from Run_log import Sys_logger
from Graph import TaskGraph
from Graph import MapGraph
from Graph import NetGraph
import FileTranslate

ALGORITHM_INFO=["Unknow",]
with open(os.path.join('./Algorithm','algorithm.json'), "r") as f:
	j = json.load(f,encoding="utf-8")
	ALGORITHM_INFO.append(j["TopoMapping"]["info"])
	ALGORITHM_INFO.append(j["TreeMatch"]["info"])
	ALGORITHM_INFO.append(j["MPIPP"]["info"])

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


def Load_net_graph(filepath,filetype,opts):
	filepath=str(filepath)
	filetype=str(filetype)
	net_ct=int(opts[0])
	net_node=int(opts[1])
	net_core=int(opts[2])
	if filetype == '.txt':
		retmodule=Load_net_graph_txt(filepath,net_ct,net_node,net_core)
	elif filetype == '.tgt':
		retmodule=Load_net_graph_tgt(filepath)
	elif filetype == '.xml':
		retmodule=Load_net_graph_xml(filepath)

	return retmodule

def Load_task_graph(filepath,filetype,opts):
	filepath=str(filepath)
	filetype=str(filetype)
	task_size=int(opts[0])
	detail=None
	retmodule=None
	if (filetype == '.APHiD') | (filetype == '.TOPO'):
		retmodule=Load_task_graph_APHiD(filepath)
		if retmodule != None:
			if retmodule.size != task_size or task_size==0:
				detail="Task number in Task file is %d, but you set it as %d."%(retmodule.size,task_size)
				retmodule=None
	elif (filetype == '.mat') | (filetype == '.MPIPP'):
		retmodule=Load_task_graph_MAT(filepath)
		if retmodule != None:
			if len(retmodule) != task_size or task_size==0:
				detail="Task number in Task file is %d, but you set it as %d."%(len(retmodule),task_size)
				retmodule=None
	elif filetype == 'Dir':
		retmodule=Load_task_graph_Dir(filepath,task_size)

	return retmodule,detail

def Load_option(filepath):
	if '.bind' in str(filepath):
		retmodule=True
	return retmodule

def Load_task_graph_Dir(filepath,filenum):
	file_out=os.path.join(filepath,"result_file")
	fmt=[1,1,1,1,1,1]
	if not os.path.exists(filepath) or filenum==0:
		return None
	if not os.path.exists(file_out):
		os.mkdir(file_out)

	result=FileTranslate.main(filepath,filenum,file_out,fmt)
	if result==0:
		os.removedirs(file_out)
		return None
	return file_out

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

def net_graph_topo_2_matrix(netgraph):
	lines_net=str(netgraph).replace(" ","").replace("(","").replace(")","")
	net_matrix=[]
	for lines in lines_net.split("\n"):
		if not lines == "":
			net_matrix.append(map(int,lines.split(",")))
	return net_matrix

def Load_net_graph_txt(filepath,ct,node,core):
	try:
		#----------------------------------------------temp data
		net_node=node
		net_core=core
		net_ct=ct
		with open(filepath,'r') as ngf:
			netgraph=ParMapper.NetGraph(ngf,net_ct,net_node,net_core)
			NetGraph.GenerateHeatMap(net_graph_topo_2_matrix(netgraph),outpath='./Graph/netgraph.html')
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
		Net=['tleaf',]
		with open(filepath,'r') as ngf:
			for fline in ngf:
				flines=fline.strip().split()
				if flines[0] != 'tleaf':
					Sys_logger.info("net graph read error : tleaf not find!")
					return None
				maxindex=int(flines[1])
				Net.append(maxindex)
				for node in [int(flines[i]) for i in range(2,maxindex*2+2,2)]:
					node_num=node_num*node
					Net.append(node)
				return node_num,Net
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
	Tgfile=str(Tgfile)
	Ngfile=str(Ngfile)
	if not os.path.exists(Tgfile) or not os.path.exists(Ngfile):
		raise Exception("file not exists")
	if algotype == TOPOMAPPING:
		if "configures" in kw:
			result,runtime,cputime,Net=Algorithm_run_TopoMapping(Tgfile,Ngfile,kw["task_size"],kw["net_ct"],kw["net_node"],kw["net_core"],kw["configures"])
		else:
			result,runtime,cputime,Net=Algorithm_run_TopoMapping(Tgfile,Ngfile,kw["task_size"],kw["net_ct"],kw["net_node"],kw["net_core"])
	elif algotype == MPIPP:
		result,runtime,cputime,Net=Algorithm_run_MPIPP(Tgfile,Ngfile,kw["nfile_type"],kw["ct"],kw["node"],kw["core"])
	elif algotype == TREEMATCH:
		bind_file = kw["bind_file"] if "bind_file" in kw else ''
		optimization = kw["optimization"] if "optimization" in kw else True
		metric = kw["metric"] if "metric" in kw else 1
		result,runtime,cputime,Net=Algorithm_run_TREEMATCH(Tgfile,Ngfile,kw["nfile_type"],bind_file,optimization,metric)

	MapGraph.GenerateScatter(ST=result,outpath="./Graph/mapgraph.html")
	MapGraph.GenerateTree(ST=result,Net=Net,outpath="./Graph/treegraph.html")
	return result,runtime,cputime

def Algorithm_run_TopoMapping(Tgfile,Ngfile,task_size,net_ct,net_node,net_core,configures=[]):
	#tasklists=ParMapper.TaskList(Tg)
	timebegin=datetime.datetime.now()
	cputimebegin=time.clock()

	result_S=ParMapper.main(Tgfile,Ngfile,task_size,net_ct,net_node,net_core,debug_mode=False,resultfile='./TopoMapping_Result.ST')

	timeend=datetime.datetime.now()
	cputimeend=time.clock()

	tmp_runtime=timeend-timebegin
	runtime=float(tmp_runtime.seconds*1000000+tmp_runtime.microseconds)/1000
	cputime=(cputimeend - cputimebegin)*1000
	#result_S=ParMapper.ParMapper(Tg,Ng,tasklists.T,process=4,strategy=ParMapper.default_compare,compare_alf=ParMapper.COMPARE_ALF,cost_function_mode=ParMapper.COST_FUNCTION_MODE)
	#print("result_S:"+str(ParMapper.S2ST(result_S)))

	Net=['matrix',net_ct,net_node,net_core]
	return ParMapper.S2ST(result_S), runtime, cputime, Net

def Algorithm_run_MPIPP(Tgfile,Ngfile,nfile_type,ct,node,core):
	mpippll = ctypes.cdll.LoadLibrary
	mpipplib = mpippll("./Algorithm/MapMPIPP/MPIPP_C2PY.so")
	if nfile_type == '.tgt':
		file_type = 1
		node_num,Net=Load_net_graph_tgt(Ngfile)
	elif nfile_type == '.txt':
		file_type = 0
		Net=['matrix',ct,node,core]
	elif nfile_type == '.xml':
		file_type = 2
		Net=[]
	try:
		arch_filename=str(Ngfile)
		com_filename=str(Tgfile)
		ct=int(ct)
		node=int(node)
		core=int(core)

		timebegin=datetime.datetime.now()
		cputimebegin=time.clock()

		mpipplib.MPIPP_MAPPING(arch_filename,file_type,com_filename,ct,node,core)

		timeend=datetime.datetime.now()
		cputimeend=time.clock()

		tmp_runtime=timeend-timebegin
		runtime=float(tmp_runtime.seconds*1000000+tmp_runtime.microseconds)/1000
		cputime=(cputimeend - cputimebegin)*1000

		return Load_result_ST("./MPIPP_Result.ST"), runtime, cputime, Net
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
	shell_command="./Algorithm/TreeMatch/mapping"
	Net=[]
	if nfile_type == '.xml':
		shell_command+=" -x "+str(Ngfile)
	elif nfile_type == '.tgt':
		shell_command+=" -t "+str(Ngfile)
		node_num,Net=Load_net_graph_tgt(Ngfile)
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

	timebegin=datetime.datetime.now()
	cputimebegin=time.clock()

	shell_state=os.system(shell_command)

	timeend=datetime.datetime.now()
	cputimeend=time.clock()

	tmp_runtime=timeend-timebegin
	runtime=float(tmp_runtime.seconds*1000000+tmp_runtime.microseconds)/1000
	cputime=(cputimeend - cputimebegin)*1000

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
	return Result, runtime, cputime, Net

def Result_print(result):
	print("result_S:"+str(ParMapper.S2ST(result)))
def Result2Str(result):
	return str(result)

def Algorithm_recommend(ngfile_type,opts):
	Net_type_tree=[".tgt",".xml"]
	Net_type_adj=[".txt",]
	Net_type_other=[]
	ngfile_type=str(ngfile_type)
	first=str(opts)
	if ngfile_type in Net_type_tree:
		return TREEMATCH
	elif ngfile_type in Net_type_adj:
		if first=="performance":
			return MPIPP
		elif first=="efficiency":
			return TOPOMAPPING
	else:
		return TOPOMAPPING


if __name__ == '__main__':  
	ll = ctypes.cdll.LoadLibrary   
	lib = ll("./Algorithm/MapMPIPP/MPIPP_C2PY.so")    
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