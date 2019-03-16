#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 15:25:06
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-13 14:52:50
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 15:25:06'

import sys
import os
from PySide import QtGui
from PySide import QtCore
from Layout import Opration_gui
from Layout import MsgBox_gui
from Layout import Config_Box
import Algorithm_manage

import logging
logging.basicConfig(level=logging.INFO,
					format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename='System.log',
					filemode='w')
Sys_logger=logging.getLogger()

global msgwindow

class MsgBox_Window(QtGui.QWidget):
	"""docstring for MsgBox_Window"""
	def __init__(self,parent):
		super(MsgBox_Window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self.center()
		self.button_binding()
		self._msg="message info"

	def paint_UI(self):
		self.qt_ui=MsgBox_gui.Ui_Dialog()
		self.qt_ui.setupUi(self)
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def button_binding(self):
		self.qt_ui.pushButton.clicked.connect(self.topclose)

	@property
	def msg(self):
		return self._msg
	@msg.setter
	def msg(self,msgstr):
		self._msg=msgstr
		self.qt_ui.textBrowser.setText(msgstr)
		self.parent.setVisible(False)
		self.show()
		#self.activateWindow()
	@QtCore.Slot()
	def topclose(self):
		self.close()
		self.parent.setVisible(True)
		

class Open_File_Browser(QtCore.QObject):
	"""A window to let user to choose a file from path and return the file path"""
	setFilepath=QtCore.Signal(str)
	def __init__(self,parent,lineEdit):
		super(Open_File_Browser, self).__init__()
		self._last_filepath=str('')
		self._lineEdit = lineEdit
		self.setFilepath.connect(self.setlineEdit)
		self.parent=parent

	#save the file path which user choose
	@property
	def last_filepath(self):
		return self._last_filepath
	@last_filepath.setter
	def last_filepath(self,new_filepath):
		self._last_filepath=new_filepath
		self.setFilepath.emit(new_filepath) #once the file path changed, changed the lineEdit
	
	@QtCore.Slot(str)
	def setlineEdit(self,new_filepath):
		self._lineEdit.setText(new_filepath)

	@QtCore.Slot()
	def opendialog(self):
		filename = QtGui.QFileDialog.getOpenFileName(self._lineEdit,"Open file","./")
		if filename[0] != '':
			self.last_filepath=filename[0]

class Open_File_Analysis(QtCore.QObject):
	"""docstring for Open_File_Analysis"""
	def __init__(self,parent,lineEdit,textEdit,order):
		super(Open_File_Analysis, self).__init__()
		self._lineEdit=lineEdit
		self._textEdit=textEdit
		self.order=order
		self.filetype=''
		self.retype=0
		self.retmodule=None
		self.parent=parent

	def file_exist(self, filepath):
		if os.path.exists(filepath) & os.path.isfile(filepath) & os.access(filepath,os.R_OK):
			return True
		else:
			return False

	def get_file_type(self):
		if self.order == 1:
			self.filetype=self.parent.comboBox_tgfiletype.currentText()
		else self.order == 2:
			self.filetype=self.parent.comboBox_ngfiletype.currentText()
		else self.order == 3:
			self.filetype='.'
		if self.filetype == '':
			msgwindow.msg="no file type selected!"

	@QtCore.Slot()
	def file_analysis(self):
		if not self.file_exist(self._lineEdit.text()):
			self._textEdit.setText("Wrong")
			msgwindow.msg="file not exists!"
		else:
			self.retype=Algorithm_manage.PARMAPPER
			if self.order == 1:
				self.retmodule=Algorithm_manage.Load_task_graph(self._lineEdit.text(),1,self.retype)
			elif self.order == 2:
				self.retmodule=Algorithm_manage.Load_net_graph(self._lineEdit.text(),1,self.retype)
			else:
				self.retmodule=None
			if self.retmodule==None:
				self._textEdit.setText("Wrong")
				msgwindow.msg="Load failed!"
			else:
				self._textEdit.setText("Done")

class Algorithm_begin(QtCore.QObject):
	"""docstring for Algorithm_begin"""
	def __init__(self, parent, File1, File2, algotype, configures):
		super(Algorithm_begin, self).__init__()
		self.File1=File1
		self.File2=File2
		self.Tg=None
		self.Ng=None
		self.algotype=algotype
		self.configures=configures
		self.parent=parent

	@QtCore.Slot()
	def Algorithm_run(self):
		self.Tg=self.File1.retmodule
		self.Ng=self.File2.retmodule
		self.parent.set_waiting()
		self.result=Algorithm_manage.Algorithm_run(self.Tg,self.Ng,self.configures,self.algotype)
		self.parent.set_active()
		Algorithm_manage.Result_print(self.result)
		msgwindow.msg=Algorithm_manage.Result2Str(self.result)

class Main_Window(QtGui.QWidget):
	"""docstring for Main_Window"""
	def __init__(self):
		super(Main_Window, self).__init__()
		self.paint_UI()
		self.button_binding()
		self.show()
		
	def paint_UI(self):
		self.qt_ui=Opration_gui.Ui_Form()
		self.qt_ui.setupUi(self)

	def button_binding(self):
		#open button in line 1 bind to file browser and line edit 1
		self.File_Browser1=Open_File_Browser(self,self.qt_ui.lineEdit_filein_1)
		self.qt_ui.pushButton_openfile_1.clicked.connect(self.File_Browser1.opendialog)
		#open button in line 2 bind to file browser and line edit 2
		self.File_Browser2=Open_File_Browser(self,self.qt_ui.lineEdit_filein_2)
		self.qt_ui.pushButton_openfile_2.clicked.connect(self.File_Browser2.opendialog)
		#open button in line 3 bind to file browser and line edit 3
		self.File_Browser3=Open_File_Browser(self,self.qt_ui.lineEdit_filein_3)
		self.qt_ui.pushButton_openfile_3.clicked.connect(self.File_Browser3.opendialog)

		#file analysis
		self.File_Analysis1=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_1,self.qt_ui.textEdit_exestate_1,1)
		self.qt_ui.pushButton_exefile_1.clicked.connect(self.File_Analysis1.file_analysis)

		self.File_Analysis2=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_2,self.qt_ui.textEdit_exestate_2,2)
		self.qt_ui.pushButton_exefile_2.clicked.connect(self.File_Analysis2.file_analysis)

		self.File_Analysis3=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_3,self.qt_ui.textEdit_exestate_3,3)
		self.qt_ui.pushButton_exefile_3.clicked.connect(self.File_Analysis3.file_analysis)

		self.Caculate_begin=Algorithm_begin(self,self.File_Analysis1,self.File_Analysis2,Algorithm_manage.PARMAPPER,self.File_Analysis3)
		self.qt_ui.pushButton_caculate.clicked.connect(self.Caculate_begin.Algorithm_run)

	def set_waiting(self):
		self.setCursor(QtCore.Qt.WaitCursor)
		self.setEnabled(False)

	def set_active(self):
		self.setCursor(QtCore.Qt.ArrowCursor)
		self.setEnabled(True)

if __name__ == '__main__':
	global msgwindow
	app=QtGui.QApplication(sys.argv)
	mainwindow=Main_Window()
	msgwindow=MsgBox_Window(mainwindow)
	app.exec_()