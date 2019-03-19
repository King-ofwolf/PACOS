#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 15:25:06
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-17 19:11:56
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 15:25:06'

import sys
import os
from PySide import QtGui
from PySide import QtCore
from Layout import Language
from Layout import Opration_gui
from Layout import MsgBox_gui
from Layout import ConfigBox_gui
from Run_log import Sys_logger

import Algorithm_manage

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

class ConfigBox_Window(QtGui.QWidget):
	"""docstring for ConfigBox_Window"""
	def __init__(self,parent):
		super(ConfigBox_Window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self.center()
		self.button_binding()
		self._opt1=0
		self._opt2=0
		self._opt3=0
		self._opt4=0
		self._opt5=0
		self._windows=0

	def paint_UI(self):
		self.qt_ui=ConfigBox_gui.Ui_Form()
		self.qt_ui.setupUi(self)
		self.qt_ui.lineEdit_in_1.setValidator(QtGui.QIntValidator())
		self.qt_ui.lineEdit_in_2.setValidator(QtGui.QIntValidator())
		self.qt_ui.lineEdit_in_3.setValidator(QtGui.QIntValidator())
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def button_binding(self):
		self.qt_ui.pushButton_cancel.clicked.connect(self.cancelclose)
		self.qt_ui.pushButton_ensure.clicked.connect(self.ensureclose)
	
	def changewindow(self,wtype):
		self._windows=wtype

	def getopt(self):
		return [self._opt1,self._opt2,self._opt3,self._opt4,self._opt5]

	@QtCore.Slot()
	def Configwindow_show(self):
		self.qt_ui.lineEdit_in_1.setText(str(self._opt1))
		self.qt_ui.lineEdit_in_2.setText(str(self._opt2))
		self.qt_ui.lineEdit_in_3.setText(str(self._opt3))
		self.qt_ui.lineEdit_in_4.setText(str(self._opt4))
		self.qt_ui.lineEdit_in_5.setText(str(self._opt5))
		if self._windows == 0:
			self.qt_ui.label_cf_4.setVisible(False)
			self.qt_ui.label_cf_5.setVisible(False)
			self.qt_ui.lineEdit_in_4.setVisible(False)
			self.qt_ui.lineEdit_in_5.setVisible(False)
		elif self._windows == 1:
			self.qt_ui.label_cf_1.setText(Language.STR_TOTAL_TASK_NUM)
			self.qt_ui.label_cf_2.setVisible(False)
			self.qt_ui.label_cf_3.setVisible(False)
			self.qt_ui.label_cf_4.setVisible(False)
			self.qt_ui.label_cf_5.setVisible(False)
			self.qt_ui.lineEdit_in_2.setVisible(False)
			self.qt_ui.lineEdit_in_3.setVisible(False)
			self.qt_ui.lineEdit_in_4.setVisible(False)
			self.qt_ui.lineEdit_in_5.setVisible(False)

		self.parent.setVisible(False)
		self.show()
		Sys_logger.info("Configwindow show with type %d"%(self._windows))

	@QtCore.Slot()
	def ensureclose(self):
		self._opt1=int(self.qt_ui.lineEdit_in_1.text())
		self._opt2=int(self.qt_ui.lineEdit_in_2.text())
		self._opt3=int(self.qt_ui.lineEdit_in_3.text())
		self.close()
		self.parent.setVisible(True)
		Sys_logger.info("Configwindow ensure close with option %d %d %d"%(self._opt1,self._opt2,self._opt3))
	@QtCore.Slot()
	def cancelclose(self):
		self.close()
		self.parent.setVisible(True)
		Sys_logger.info("Configwindow cancel close")		

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
		self._last_filepath=self._lineEdit.text()
		if os.path.isabs(self._last_filepath):
			return self._last_filepath
		else :
			return os.path.join(os.getcwd(),self._last_filepath)
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
		self.retmodule=None
		self.parent=parent

	def file_exist(self, filepath):
		if os.path.exists(filepath) & os.path.isfile(filepath) & os.access(filepath,os.R_OK):
			return True
		else:
			return False

	def get_file_type(self):
		if self.order == 1:
			self.filetype=self.parent.qt_ui.comboBox_tgfiletype.currentText()
		elif self.order == 2:
			self.filetype=self.parent.qt_ui.comboBox_ngfiletype.currentText()
		elif self.order == 3:
			self.filetype='.'
		if self.filetype == '':
			msgwindow.msg="no file type selected!"
		Sys_logger.info("comboBox %d get file type %s"%(self.order,str(self.filetype)))

	@QtCore.Slot()
	def file_analysis(self):
		if not self.file_exist(self._lineEdit.text()):
			self._textEdit.setText("Wrong")
			msgwindow.msg="file not exists!"
		else:
			self.get_file_type()
			if self.order == 1:
				if self.filetype == '.APHiD':
					task_size=self.parent.Config_Setter1.getopt()[0]
					self.retmodule=Algorithm_manage.Load_task_graph_APHiD(self._lineEdit.text())
					if self.retmodule != None:
						if self.retmodule.size != task_size :
							msgwindow.msg="Task number in Task file is %d, but you set it as %d."%(self.retmodule.size,task_size)
							retmodule=None
				elif self.filetype == '.mat':
					pass#------------------------------------
			elif self.order == 2:
				if self.filetype == '.txt':
					[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
					self.retmodule=Algorithm_manage.Load_net_graph_txt(self._lineEdit.text(),net_ct,net_node,net_core)
				elif self.filetype == '.tgf':
					pass#--------------------------------------
				elif self.filetype == '.xml':
					pass#----------------------------------
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
		self.tgfile=File1
		self.ngfile=File2
		self.algotype=algotype
		self.configures=configures.last_filepath
		self.parent=parent

	@QtCore.Slot()
	def Algorithm_run(self):
		self.parent.set_waiting()
		try:
			task_size=self.parent.Config_Setter1.getopt()[0]
			[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
			self.result=Algorithm_manage.Algorithm_run_TopoMapping(self.tgfile.last_filepath,self.ngfile.last_filepath,task_size,net_ct,net_node,net_core)
			msgwindow.msg=Algorithm_manage.Result2Str(self.result)
		except Exception as e:
			Sys_logger.debug(str(e))
			msgwindow.msg=Language.STR_CACULATE_FAILD
		else:
			pass
		finally:
			pass
		self.parent.set_active()
		#Algorithm_manage.Result_print(self.result)

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
		self.qt_ui.pushButton_exefile_1.setEnabled(False)
		self.qt_ui.pushButton_exefile_2.setEnabled(False)
		self.qt_ui.label_7.setVisible(False)
		self.qt_ui.lineEdit_filein_3.setVisible(False)
		self.qt_ui.pushButton_openfile_3.setVisible(False)
		self.qt_ui.pushButton_exefile_3.setVisible(False)
		self.qt_ui.label_8.setVisible(False)
		self.qt_ui.textEdit_exestate_3.setVisible(False)

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

		#file path line edit changed -> button enable
		#self.qt_ui.lineEdit_filein_1.textChanged.connect(lambda:self.qt_ui.pushButton_exefile_1.setEnabled(True))
		#self.qt_ui.lineEdit_filein_2.textChanged.connect(lambda:self.qt_ui.pushButton_exefile_2.setEnabled(True))

		#Config settings
		self.Config_Setter1=ConfigBox_Window(self)
		self.Config_Setter1.changewindow(1)
		self.qt_ui.pushButton_cf_set1.clicked.connect(self.Config_Setter1.Configwindow_show)
		self.qt_ui.pushButton_cf_set1.released.connect(lambda:self.qt_ui.pushButton_exefile_1.setEnabled(True))

		self.Config_Setter2=ConfigBox_Window(self)
		self.qt_ui.pushButton_cf_set2.clicked.connect(self.Config_Setter2.Configwindow_show)
		self.qt_ui.pushButton_cf_set2.released.connect(lambda:self.qt_ui.pushButton_exefile_2.setEnabled(True))

		#file analysis
		self.File_Analysis1=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_1,self.qt_ui.textEdit_exestate_1,1)
		self.qt_ui.pushButton_exefile_1.clicked.connect(self.File_Analysis1.file_analysis)

		self.File_Analysis2=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_2,self.qt_ui.textEdit_exestate_2,2)
		self.qt_ui.pushButton_exefile_2.clicked.connect(self.File_Analysis2.file_analysis)

		self.File_Analysis3=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_3,self.qt_ui.textEdit_exestate_3,3)
		self.qt_ui.pushButton_exefile_3.clicked.connect(self.File_Analysis3.file_analysis)

		#algorithm caculate
		self.Caculate_begin=Algorithm_begin(self,self.File_Browser1,self.File_Browser2,Algorithm_manage.TOPOMAPPING,self.File_Browser3)
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