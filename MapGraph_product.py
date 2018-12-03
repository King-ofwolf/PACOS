#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2018-11-20 18:35:41
# @Last Modified by:   King-ofwolf
# @Last Modified time: 2018-12-03 15:35:46
# @Email:	wangshengling@buaa.edu.cn
'Info: a Python file '
__author__ = 'Wang'

def MapGraph_product():
	with open('text.txt','w') as f:
		mylist=[0 for i in range(48)]
		for k in range(24):
			for i in range(6):
				if int(k/4)==i:
					mylist[i*4:i*4+4]=(2,2,2,2)
				else:
					mylist[i*4:i*4+4]=(4,4,4,4)
			for i in range(24):
				mylist[i+24]=6
			mylist[k]=0
			print(mylist)
			for i in range(48):
				f.write(str(mylist[i])+' ')
			f.write('\n')

		for k in range(24):
			for i in range(24):
				mylist[i]=6
			for i in range(6):
				if int(k/4)==i:
					mylist[24+i*4:24+i*4+4]=(2,2,2,2)
				else:
					mylist[24+i*4:24+i*4+4]=(4,4,4,4)
			
			mylist[24+k]=0
			print(mylist)
			for i in range(48):
				f.write(str(mylist[i])+' ')
			f.write('\n')

def MapGraph_product2(IOstream,tcsize,nsize,csize,outfile):
	with open(outfile,'w') as f:
		numline=-1
		for lines in IOstream:
			numline+=1
			if numline%csize!=0:
				continue
			for i in lines.strip().split()[::csize]:
				tmp=int(i.split('.').pop())
				if tmp==1:
					tmp=0
				f.write(str(tmp)+' ')
			f.write('\n')
			

if __name__ == '__main__':
	inputfile=input("file:")
	tcsize=int(input("number of cores:"))
	nsize=int(input("number of nodes:"))
	csize=int(input("number of cores in each nodes:"))
	outfile=inputfile+'-'+str(nsize)+'-'+str(csize)+'.txt'
	with open(inputfile,'r') as f:
		MapGraph_product2(f,tcsize,nsize,csize,outfile)
