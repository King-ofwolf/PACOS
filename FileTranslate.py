#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-14 16:13:29
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-16 20:58:35
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-14 16:13:29'

import os
import getopt
import sys


class TgFiles(object):
	"""docstring for TgFiles"""
	def __init__(self, dirpath):
		super(TgFiles, self).__init__()
		self._files=[]
		self._number=0
		self.getfiles(dirpath)
		self._index=-1

	def getfiles(self,dirpath):
		if not os.path.exists(dirpath):
			return []
		virtualfiles=os.listdir(dirpath)
		for file in virtualfiles:
			file=os.path.join(os.getcwd(),dirpath,file)
			if os.path.isfile(file):
				if 'Process' in os.path.basename(file):
					self._files.append(file)
					self._number+=1

	@property
	def files(self):
		return self._files
	@property
	def number(self):
		return self._number

class TgMatrix(object):
	"""docstring for TgMatrix"""
	def __init__(self, number):
		super(TgMatrix, self).__init__()
		self._Tnum = number
		self._commMatrix=[[0 for j in range(number)] for i in range(number)]
		self._rateMatrix=[[0 for j in range(number)] for i in range(number)]

	def commadd(self,x,y,comm):
		if (x>=self._Tnum) | (y>=self._Tnum):
			print "Task number",x,y,"are out of index with max number ",self._Tnum
			sys.exit(0)
		self._commMatrix[x][y]+=comm
		self._rateMatrix[x][y]+=1

	def analysis_file(self,file_path):
		if os.path.exists(file_path) & os.path.isfile(file_path) & os.access(file_path,os.R_OK):
			pass
		else :
			print "input file path",file_path,"is not an enable file"
			return None
		try:
			with open(file_path,'r') as infile:
				for line in infile:
					(m,n,k)=line.strip().split()
					(m,n,k)=(int(m),int(n),int(k))
					self.commadd(m,n,k)
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass

	def genrate_nedges(self):
		nedges=0
		for i in self._commMatrix:
			for j in i:
				if j != 0:
					nedges+=1
		return nedges

	def print_file_mat(self,file_path='./'):
		if os.path.exists(file_path) & os.path.isdir(file_path) & os.access(file_path,os.W_OK):
			file_path+="ProcessCommTrace_"+str(self._Tnum)+".mat"
		else:
			print "output file path",file_path,"is not an enable dir"
			return None

		try:
			with open(file_path,'w') as matfile:
				for i in range(self._Tnum):
					for j in range(self._Tnum):
						matfile.write(str(self._commMatrix[i][j])+" ")
					matfile.write("\n")
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass

	def print_file_APHiD(self,file_path='./'):
		if os.path.exists(file_path) & os.path.isdir(file_path) & os.access(file_path,os.W_OK):
			file_path+="ProcessCommTrace_"+str(self._Tnum)+".APHiD"
		else:
			print "output file path",file_path,"is not an enable dir"
			return None

		try:
			with open(file_path,'w') as aphidfile:
				aphidfile.write(str(self._Tnum)+" "+str(self.genrate_nedges())+" 001\n")
				for i in range(self._Tnum):
					for j in range(self._Tnum):
						temp=self._commMatrix[i][j]
						if temp != 0:
							aphidfile.write(str(j)+" "+str(temp)+" ")
					aphidfile.write("\n")
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass

	def print_file_rat(self,file_path='./'):
		if os.path.exists(file_path) & os.path.isdir(file_path) & os.access(file_path,os.W_OK):
			file_path+="ProcessCommTrace_"+str(self._Tnum)+".rat"
		else:
			print "output file path",file_path,"is not an enable dir"
			return None

		try:
			with open(file_path,'w') as ratfile:
				for i in range(self._Tnum):
					for j in range(self._Tnum):
						ratfile.write(str(self._rateMatrix[i][j])+" ")
					ratfile.write("\n")
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass
		
	
def helpmsg():
	print "example: python FileTranslate.py -n 128 -o ./test/ --path ./examples/taskgraph/128/ -MTA"
	print "usage: python FileTranslate.py [option] ... [arg] ..."
	print "Options and arguments:"
	print "-h\t: print this help message"
	print "-n arg\t: the <arg> is the number of the task communication files, default is 128"
	print "-o arg\t: the <arg> is the direction path of the output files, default is ./"
	print "--path arg\t: the <arg> is the direction path of the task communication files, default is ./"
	print "-M\t: genrate communication quantity matrix file which type is .mat"
	print "-T\t: genrate communication rate matrix file which type is .rat"
	print "-A\t: genrate communication quantity matrix file which type is .APHiD"
		


if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hMTAn:o:",["debug","path="])
	except Exception as e:
		print e
		helpmsg()
		sys.exit()
	else:
		pass
	finally:
		pass
	
	file_path = "./"
	file_num = 128
	file_out = "./"
	fmt=[False,False,False]

	for op, value in opts:
		if op == '--path':
			if os.path.exists(value) & os.path.isdir(value):
				file_path=value
			else :
				print value,"is not exist or not a dir path!"
				sys.exit(0)
		elif op == '-h':
			helpmsg()
			sys.exit()
		elif op == '-n':
			file_num=int(value)
		elif op == '-o':
			file_out=value
		elif op == '-M':
			fmt[0]=True
		elif op == '-T':
			fmt[1]=True
		elif op == '-A':
			fmt[2]=True
		else:
			print "unknow option",op
			helpmsg()
			sys.exit()
	if opts == []:
		helpmsg()
		sys.exit()

	tgfiles=TgFiles(file_path)
	if tgfiles.number != file_num:
		print "the file number you command is",file_num,",but the file in",file_path,"has",tgfiles.number,"Process files(file name with 'Process')."
		sys.exit(0)
	tgmatrix=TgMatrix(file_num)
	for infile in tgfiles.files:
		tgmatrix.analysis_file(infile)
	if fmt[0]:	
		tgmatrix.print_file_mat(file_out)
	if fmt[1]:
		tgmatrix.print_file_rat(file_out)
	if fmt[2]:
		tgmatrix.print_file_APHiD(file_out)



