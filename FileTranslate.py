#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-14 16:13:29
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-27 15:32:43
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

	def print_file_MPIPP(self,file_path='./'):
		if os.path.exists(file_path) & os.path.isdir(file_path) & os.access(file_path,os.W_OK):
			file_path+="ProcessCommTrace_"+str(self._Tnum)+".MPIPP"
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

	def print_file_TOPO(self,file_path='./'):
		if os.path.exists(file_path) & os.path.isdir(file_path) & os.access(file_path,os.W_OK):
			file_path+="ProcessCommTrace_"+str(self._Tnum)+".TOPO"
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

	def print_file_matrix(self,file_path='./'):
		if os.path.exists(file_path) & os.path.isdir(file_path) & os.access(file_path,os.W_OK):
			file_path+="ProcessCommTrace_"+str(self._Tnum)+".matrix"
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
		
def Net_File_Translate(file_path,core):
	if os.path.exists(file_path) & os.path.isfile(file_path) & os.access(file_path,os.R_OK):
		pass
	else :
		print "input file path",file_path,"is not an enable file"
		return None
	try:
		net_matrix=[]
		with open(file_path,'r') as infile:
			for line in infile:
				lines=line.strip().split()
				lines_matrix=[int(float(i)*1000000) for i in lines]
				net_matrix.append(lines_matrix[::core])

		file_out_path=file_path+"-"+str(core)
		with open(file_out_path,'w') as outfile:
			for line in net_matrix[::core]:
				for item in line:
					outfile.write(str(item)+" ")
				outfile.write("\n")
				
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass

def Reuslt_File_Translate_TreeMatch(file_path):
	with open(file_path,'r') as rf:
		for lines in rf:
			linesplit=lines.strip().split()
			if linesplit[0] == 'TreeMatch:':
				Result=linesplit[1].split(',')

	file_out_path=file_path+".ST"
	with open(file_out_path,'w') as outfile:
		for i in Result:
			outfile.write(str(i)+"\n")

def Layout_File_Translate(file_ST,file_layout):
	STlist=[]
	laylist=[]
	with open(file_ST,'r') as rtf:
		for lines in rtf:
			if lines.strip() != "":
				STlist.append(lines.strip())
		
	with open(file_layout,'r') as layf:
		for lines in layf:
			if lines.strip() != "":
				laylist.append(lines.strip())

	for i in range(len(STlist)):
		STlist[i]=laylist[int(STlist[i])]

	file_out_path=file_layout+"."+os.path.basename(file_ST)
	with open(file_out_path,'w') as outfile:
		for i in STlist:
			outfile.write(str(i)+"\n")

def Get_time_from_app(file_app,file_time):
	pass


def helpmsg():
	print "example: python FileTranslate.py -n 128 -o ./test/ --path ./examples/taskgraph/128/ -A"
	print "usage: python FileTranslate.py [option] ... [arg] ..."
	print "Options and arguments:"
	print "-h\t: print this help message"
	print "-n arg\t: the <arg> is the number of the task communication files, default is 128"
	print "-o arg\t: the <arg> is the directory path of the output files, default is ./"
	print "--path arg\t: the <arg> is the direction path of the task communication files, default is ./"
	print "-M\t: genrate communication quantity matrix file which type is .mat and .MPIPP"
	print "-T\t: genrate communication rate matrix file which type is .TOPO and .APHiD"
	print "-R\t: genrate communication quantity and rate matrix file which type is .matrix and .rat"
	print "-A\t: genrate all communication quantity matrix file above"
		
def main(file_path,file_num,file_out,fmt):
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
		tgmatrix.print_file_MPIPP(file_out)
	if fmt[2]:
		tgmatrix.print_file_TOPO(file_out)
	if fmt[3]:
		tgmatrix.print_file_APHiD(file_out)
	if fmt[4]:
		tgmatrix.print_file_matrix(file_out)
	if fmt[5]:
		tgmatrix.print_file_rat(file_out)



if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hMTAn:o:",["debug","path=","net=","TR=","ST=","layout=","appfile=","timefile="])
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
	fmt=[False,False,False,False,False,False]
	file_net=""
	file_TR=""
	file_ST=""
	file_app=""

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
			fmt[1]=True
		elif op == '-T':
			fmt[2]=True
			fmt[3]=True
		elif op == '-R':
			fmt[4]=True
			fmt[5]=True
		elif op == '-A':
			fmt=[True,True,True,True,True,True]
		elif op == '--net':
			file_net=value
		elif op == '--TR':
			file_TR=value
		elif op == '--ST':
			file_ST=value
		elif op == '--layout':
			file_layout=value
		elif op == '--appfile':
			file_app=value
		elif op == '--timefile':
			file_time=value
		else:
			print "unknow option",op
			helpmsg()
			sys.exit()
	if opts == []:
		helpmsg()
		sys.exit()
	if file_net != "":
		Net_File_Translate(file_net,24)
	elif file_TR != "":
		Reuslt_File_Translate_TreeMatch(file_TR)
	elif file_ST != "":
		Layout_File_Translate(file_ST,file_layout)
	elif file_app != "":
		Get_time_from_app(file_app,file_time)
	else:
		main(file_path,file_num,file_out,fmt)
	
	



