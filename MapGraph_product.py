#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2018-11-20 18:35:41
# @Last Modified by:   kingofwolf
# @Last Modified time: 2018-11-21 15:50:01
# @Email:	wangshengling@buaa.edu.cn
'Info: a Python file '
__author__ = 'Wang'

class Test(object):
	"""docstring for Test"""
	def __init__(self, arg):
		super(Test, self).__init__()
		print('hello:',arg)
		self.__printmy()
	def __printmy(self):
		print('hello')

if __name__ == '__main__':
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

