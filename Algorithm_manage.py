#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 20:32:56
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-10 22:01:45
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 20:32:56'


from TopoMapping import ParMapper

PARMAPPER=1
TREEMATCH=2
	

def Load_task_graph(filepath,filetype,algotype):
	if algotype==PARMAPPER:
		try:
			with open(filepath,'r') as tgf:
				taskgraph=ParMapper.TaskGraph()
				#taskgraph.readgraphfile0(tgf,task_size)
				taskgraph.readgraphfile1(tgf)
				return taskgraph
		except Exception as e:
			print("task graph read error")
			return None
		finally:
			pass


def Load_net_graph(filepath,filetype,algotype):
	if algotype==PARMAPPER:
		try:
			#----------------------------------------------temp data
			net_node=7
			net_core=20
			net_ct=128
			with open(filepath,'r') as ngf:
				netgraph=ParMapper.NetGraph(ngf,net_ct,net_node,net_core)
				return netgraph
		except Exception as e:
			print("net graph read error")
			raise
			#return None
		finally:
			pass

def Algorithm_run(Tg,Ng,configures,algotype):
	if algotype==PARMAPPER:
		tasklists=ParMapper.TaskList(Tg)
		result_S=ParMapper.ParMapper(Tg,Ng,tasklists.T,process=4,strategy=ParMapper.default_compare,compare_alf=ParMapper.COMPARE_ALF,cost_function_mode=ParMapper.COST_FUNCTION_MODE)
		#print("result_S:"+str(ParMapper.S2ST(result_S)))
		return result_S

def Result_print(result):
	print("result_S:"+str(ParMapper.S2ST(result)))
def Result2Str(result):
	return str(ParMapper.S2ST(result))