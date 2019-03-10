#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-03 08:52:43
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-03 16:31:48
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-03 08:52:43'

from PySide import QtGui
from PySide import QtCore

class Open_File_Browser(QtCore.QObject):
	"""docstring for Open_File_Browser"""
	setFilepath=QtCore.Signal(str)
	def __init__(self,lineEdit):
		super(Open_File_Browser, self).__init__()
		self._last_filepath=str('')
		self._lineEdit = lineEdit
		self.setFilepath.connect(self.setlineEdit)


	@property
	def last_filepath(self):
		return self._last_filepath
	@last_filepath.setter
	def last_filepath(self,new_filepath):
		self._last_filepath=new_filepath
		self.setFilepath.emit(new_filepath)
	
	@QtCore.Slot(str)
	def setlineEdit(self,new_filepath):
		self._lineEdit.setText(new_filepath)

	@QtCore.Slot()
	def opendialog(self):
		filename = QtGui.QFileDialog.getOpenFileName(self._lineEdit,"Open file","/home")
		if filename[0] != '':
			self.last_filepath=filename[0]

