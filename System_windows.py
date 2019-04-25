#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 15:25:06
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-04-14 19:25:10
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 15:25:06'

import sys
import os
import subprocess
import traceback
import json
import functools
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit
from Layout import Language
from Layout import Opration_gui
from Layout import MsgBox_gui
from Layout import ConfigBox_gui
from Layout import Graph_gui
from Layout import ResultBox_gui
from Layout import MainWindow_gui
from Run_log import Sys_logger,LOG_DEBUG,LOG_INFO

import Algorithm_manage

global msgwindow
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot

class MsgBox_Window(QtGui.QWidget):
	"""A message window that can hold a String type of message to show in a private window when _msg changed to the message"""
	def __init__(self,parent):
		super(MsgBox_Window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self.center()
		self.button_binding()
		self._msg="message info"
		self._exception=None

	def paint_UI(self):
		self.qt_ui=MsgBox_gui.Ui_Dialog()
		self.qt_ui.setupUi(self)
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def button_binding(self):
		#ok button binding with close the window
		self.qt_ui.pushButton.clicked.connect(self.topclose)

	@property
	def msg(self):
		return self._msg
	#_msg's setter, whenever the _msg changed, close the parent window and show message window with that message
	@msg.setter
	def msg(self,msgstr):
		self._msg=msgstr
		if self._exception!=None:
			msgstr+="\nDetails:\n"+str(traceback.format_exc())
		self.qt_ui.textBrowser.setText(msgstr)
		self.parent.setVisible(False)
		self.show()
		#self.activateWindow()
	# a slot that can be bind to close the window and show the parent window
	@QtCore.Slot()
	def topclose(self):
		self.close()
		self._init()
		self.parent.setVisible(True)

	def _init(self):
		self._msg="message info"
		self._exception=None
	@property
	def exception(self):
		return self._exception
	@exception.setter
	def exception(self,msgexception):
		self._exception=msgexception
	

class ConfigBox_Window(QtGui.QWidget):
	"""ConfigBox Window"""
	def __init__(self,parent):
		super(ConfigBox_Window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self.center()
		self.button_binding()
		self._options=[0,0,0,0,0]
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
		return self._options

	def setopt(self,options):
		self._options=options[0:5]

	def set_option_visible(self,options):
		self.qt_ui.label_cf_1.setVisible(options[0])
		self.qt_ui.label_cf_2.setVisible(options[1])
		self.qt_ui.label_cf_3.setVisible(options[2])
		self.qt_ui.label_cf_4.setVisible(options[3])
		self.qt_ui.label_cf_5.setVisible(options[4])
		self.qt_ui.lineEdit_in_1.setVisible(options[0])
		self.qt_ui.lineEdit_in_2.setVisible(options[1])
		self.qt_ui.lineEdit_in_3.setVisible(options[2])
		self.qt_ui.lineEdit_in_4.setVisible(options[3])
		self.qt_ui.lineEdit_in_5.setVisible(options[4])

	@QtCore.Slot()
	def Configwindow_show(self):
		self.qt_ui.lineEdit_in_1.setText(str(self._options[0]))
		self.qt_ui.lineEdit_in_2.setText(str(self._options[1]))
		self.qt_ui.lineEdit_in_3.setText(str(self._options[2]))
		self.qt_ui.lineEdit_in_4.setText(str(self._options[3]))
		self.qt_ui.lineEdit_in_5.setText(str(self._options[4]))
		if self._windows == 0:	#net of .txt config window
			self.set_option_visible([True,True,True,False,False])
		elif self._windows == 1:	#task config window
			self.qt_ui.label_cf_1.setText(Language.STR_TOTAL_TASK_NUM)
			self.set_option_visible([True,False,False,False,False])
		elif self._windows == 2:	#net of .tgt config window
			self.set_option_visible([True,False,False,False,False])

		self.parent.setVisible(False)
		self.show()
		Sys_logger.info("Configwindow show with type %d"%(self._windows))

	@QtCore.Slot()
	def ensureclose(self):
		self._options[0]=int(self.qt_ui.lineEdit_in_1.text())
		self._options[1]=int(self.qt_ui.lineEdit_in_2.text())
		self._options[2]=int(self.qt_ui.lineEdit_in_3.text())
		self.close()
		self.parent.setVisible(True)
		Sys_logger.info("Configwindow ensure close with option %d %d %d"%(self._options[0],self._options[1],self._options[2]))
	@QtCore.Slot()
	def cancelclose(self):
		self.close()
		self.parent.setVisible(True)
		Sys_logger.info("Configwindow cancel close")		

class Open_File_Browser(QtCore.QObject):
	"""A window to let user to choose a file from path and return the file path"""
	# a signal that whenever the _last_filepath changed, the _lineEdit will be changed too
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
		if filename != '':
			self.last_filepath=filename

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
			self._textEdit.setTextColor(QtGui.QColor("red"))
			self._textEdit.setText("Wrong")
			msgwindow.msg="file not exists!"
		else:
			self.get_file_type()
			task_size=self.parent.Config_Setter1.getopt()[0]
			if self.order == 1:#file analysis of task graph
				if (self.filetype == '.APHiD') | (self.filetype == '.TOPO'):
					self.retmodule=Algorithm_manage.Load_task_graph_APHiD(self._lineEdit.text())
					if self.retmodule != None:
						if self.retmodule.size != task_size :
							msgwindow.msg="Task number in Task file is %d, but you set it as %d."%(self.retmodule.size,task_size)
							retmodule=None
				elif (self.filetype == '.mat') | (self.filetype == '.MPIPP'):
					self.retmodule=Algorithm_manage.Load_task_graph_MAT(self._lineEdit.text())
					if self.retmodule != None:
						if len(self.retmodule) != task_size:
							msgwindow.msg="Task number in Task file is %d, but you set it as %d."%(len(self.retmodule),task_size)
							retmodule=None
			elif self.order == 2:#file analysis of net graph
				if self.filetype == '.txt':
					[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
					self.retmodule=Algorithm_manage.Load_net_graph_txt(self._lineEdit.text(),net_ct,net_node,net_core)
				elif self.filetype == '.tgt':
					self.retmodule=Algorithm_manage.Load_net_graph_tgt(self._lineEdit.text())
				elif self.filetype == '.xml':
					self.retmodule=Algorithm_manage.Load_net_graph_xml(self._lineEdit.text())
			elif self.order == 3:
				if '.bind' in str(self._lineEdit.text()):
					self.retmodule=True
			else:
				self.retmodule=None

			if self.retmodule==None:
				self._textEdit.setTextColor(QtGui.QColor("red"))
				self._textEdit.setText("Wrong")
				msgwindow.msg="Load failed!"
			else:
				self._textEdit.setTextColor(QtGui.QColor("green"))
				self._textEdit.setText("Done")

class GraphBox_Window(QtGui.QWidget):
	"""docstring for GraphBox_Window"""
	def __init__(self, parent, graphpath='./Graph/taskgraph.html'):
		super(GraphBox_Window, self).__init__()
		self.parent=parent
		self.graphpath=graphpath
		self.paint_UI()
		self.button_binding()
		self.center()

	def paint_UI(self):
		self.qt_ui=Graph_gui.Ui_Dialog()
		self.qt_ui.setupUi(self)
		self.webview=QtWebKit.QWebView(self.qt_ui.QFrame_graph)

	def button_binding(self):
		self.qt_ui.pushButton.clicked.connect(self.openBrowser)	

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	@QtCore.Slot()
	def graphshow(self):
		self.weburl=QtCore.QUrl(self.graphpath)
		self.webview.load(self.weburl)
		self.parent.setVisible(False)
		self.show()

	def closeEvent(self,event):
		self.parent.setVisible(True)
		event.accept()

	@QtCore.Slot()
	def openBrowser(self):
		#open html file with internet browser according to system type 
		if os.name == 'posix':
			subprocess.call(["xdg-open",self.graphpath])
		elif sys.platform == 'nt':
			os.startfile(self.graphpath)
		else:
			msgwindow.msg="We can not open Internet Browser on your system!"

class ResultBox_window(QtGui.QWidget):
	"""docstring for ResultBox_window"""
	def __init__(self,parent,graphpath='./Graph/mapgraph.html'):
		super(ResultBox_window, self).__init__()
		self.parent=parent
		self.graphpath=graphpath
		self.paint_UI()
		self.center()

	def paint_UI(self):
		self.qt_ui=ResultBox_gui.Ui_Dialog()
		self.qt_ui.setupUi(self)
		self.webview=QtWebKit.QWebView(self.qt_ui.tab)

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	@QtCore.Slot()
	def resultshow(self):
		self.parent.setVisible(False)
		self.show()
		
	def closeEvent(self,event):
		self.parent.setVisible(True)
		event.accept()

	def setResult(self,Slist,ct=1024):
		self.qt_ui.listWidget.clear()
		#data tab
		item = QtGui.QListWidgetItem()
		item.setText(Language.STR_RESULT_MAP)
		self.qt_ui.listWidget.addItem(item)
		count=0
		for s in Slist:
			item = QtGui.QListWidgetItem()
			tempstr="%d\t%d"%(count,s)
			count+=1
			item.setText(tempstr)
			self.qt_ui.listWidget.addItem(item)

		#map tab
		self.weburl=QtCore.QUrl(self.graphpath)
		self.webview.load(self.weburl)

	def setAlgorithmmsg(self,algotype,tasknum,corenum,caculate_time):
		self.qt_ui.label_algorithm.setText(Algorithm_manage.ALGORITHM_NAME[algotype])
		self.qt_ui.label_tasknum.setText(str(tasknum))
		self.qt_ui.label_corenum.setText(str(corenum))
		self.qt_ui.label_caculatetime.setText(str(caculate_time))

	#translate the result net to task into task to net (S to ST)
	def ResultTranslate(self,Slist,ct):
		count=0
		Stemp=[-1 for i in range(ct)]
		for s in Slist:
			Stemp[s]=count
			count+=1
		return Stemp

class Algorithm_begin(QtCore.QObject):
	"""docstring for Algorithm_begin"""
	def __init__(self, parent, algotype, configures):
		super(Algorithm_begin, self).__init__()
		self.algotype=algotype
		self.configures=configures
		self.parent=parent

	def Algorithm_choose(self):
		if self.parent.qt_ui.radioButton_algorithm_1.isChecked():
			self.algotype=Algorithm_manage.TOPOMAPPING
		elif self.parent.qt_ui.radioButton_algorithm_2.isChecked():
			self.algotype=Algorithm_manage.MPIPP
		elif self.parent.qt_ui.radioButton_algorithm_3.isChecked():
			self.algotype=Algorithm_manage.TREEMATCH

	@QtCore.Slot()
	def Algorithm_run(self):
		self.parent.set_waiting()
		alg_tgfile=str(self.parent.qt_ui.lineEdit_filein_1.text())
		alg_ngfile=str(self.parent.qt_ui.lineEdit_filein_2.text())
		alg_cgfile=str(self.parent.qt_ui.lineEdit_filein_3.text())	#algorithm config file
		try:
			task_size=self.parent.Config_Setter1.getopt()[0]
			[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
			self.Algorithm_choose()

			if self.algotype == Algorithm_manage.TOPOMAPPING:
				self.result=Algorithm_manage.Algorithm_run(Algorithm_manage.TOPOMAPPING,alg_tgfile,alg_ngfile,task_size=task_size,net_ct=net_ct,net_node=net_node,net_core=net_core)
			elif self.algotype == Algorithm_manage.MPIPP:
				ngfile_type = self.parent.qt_ui.comboBox_ngfiletype.currentText()
				self.result=Algorithm_manage.Algorithm_run(Algorithm_manage.MPIPP,alg_tgfile,alg_ngfile,nfile_type=ngfile_type,ct=net_ct,node=net_node,core=net_core)
			elif self.algotype == Algorithm_manage.TREEMATCH:
				ngfile_type = self.parent.qt_ui.comboBox_ngfiletype.currentText()
				bind_choose = self.parent.qt_ui.radioButton_config_op2.isChecked()
				bind_file = alg_cgfile if bind_choose else ''
				optimization = not self.parent.qt_ui.radioButton_config_op3.isChecked()
				metric=self.parent.qt_ui.comboBox_metric.currentIndex()+1
				self.result=Algorithm_manage.Algorithm_run(Algorithm_manage.TREEMATCH,alg_tgfile,alg_ngfile,nfile_type=ngfile_type,bind_file=bind_file,optimization=optimization,metric=metric)

			self.parent.Result_Show.setResult(self.result,net_ct)
			self.parent.Result_Show.setAlgorithmmsg(self.algotype,task_size,net_ct,0)
			self.parent.Result_Show.resultshow()
		except Exception as e:
			Sys_logger.debug(str(e))
			msgwindow.exception=e
			msgwindow.msg=Language.STR_CACULATE_FAILD
		else:
			pass
		finally:
			pass
		self.parent.set_active()
		#Algorithm_manage.Result_print(self.result)

class Window_Menu(QtGui.QMainWindow):
	"""docstring for Window_Menu"""
	def __init__(self, parent):
		super(Window_Menu, self).__init__()
		self.parent = parent
		self.option_file='./examples/examples.json'
		self.paint_UI()

	def paint_UI(self):
		self.qt_ui=MainWindow_gui.Ui_MainWindow()
		self.qt_ui.setupUi(self.parent)
		self.add_example()

	def add_example(self):
		self.actions=[]
		self.option_dics=[]
		with open(self.option_file) as opf:
			examples_dic=json.load(opf)
		for algo in examples_dic:
			sub_menu=QtGui.QMenu(self.qt_ui.menu_example)
			sub_menu.setTitle(algo)
			self.qt_ui.menu_example.addAction(sub_menu.menuAction())
			for exam in examples_dic[algo]:
				actionOption=QtGui.QAction(self.parent)
				actionOption.setText(exam)
				actionOption.triggered.connect(functools.partial(self.set_example,options_dic=examples_dic[algo][exam],algo=algo))
				#actionOption.triggered.connect(lambda x:self.set_example(examples_dic[algo][exam]))
				sub_menu.addAction(actionOption)

	def set_example(self,options_dic={},algo=""):
		if algo == "TreeMatch":
			self.parent.qt_ui.radioButton_algorithm_3.setChecked(True)
		elif algo == "MPIPP":
			self.parent.qt_ui.radioButton_algorithm_2.setChecked(True)
		elif algo == "TopoMapping":
			self.parent.qt_ui.radioButton_algorithm_1.setChecked(True)
		self.parent.qt_ui.lineEdit_filein_1.setText(options_dic['task_file'])
		self.parent.qt_ui.comboBox_tgfiletype.setCurrentIndex(self.parent.qt_ui.comboBox_tgfiletype.findText(options_dic['task_type']))
		self.parent.Config_Setter1.setopt([int(options_dic['task_num']),0,0,0,0])
		self.parent.qt_ui.lineEdit_filein_2.setText(options_dic['net_file'])
		self.parent.qt_ui.comboBox_ngfiletype.setCurrentIndex(self.parent.qt_ui.comboBox_ngfiletype.findText(options_dic['net_type']))
		self.parent.Config_Setter2.setopt([int(options_dic['net_ct']),int(options_dic['net_node']),int(options_dic['net_core']),0,0])

class Main_Window(QtGui.QMainWindow):
	"""docstring for Main_Window"""
	def __init__(self):
		super(Main_Window, self).__init__()
		self.paint_UI()
		self.option_setting()
		self.button_binding()
		self.activity_binding()
		self.show()
		
	def paint_UI(self):
		self.qt_menu=Window_Menu(self)
		self.qt_ui=Opration_gui.Ui_Form()
		self.qt_ui.setupUi(self)
		#disabled at begin
		# self.qt_ui.pushButton_exefile_1.setEnabled(False)
		# self.qt_ui.pushButton_exefile_2.setEnabled(False)
		self.qt_ui.pushButton_tg_show.setEnabled(False)
		#line3 file in layout
		self.set_line3_file_in_layout(False)

		#algorithm match button 
		self.qt_ui.pushButton_algorithm_match.setVisible(False)

		#file input infomation
		self.qt_ui.textBrowser_filein_msg.setHtml(Language.STR_FILE_INPUT_INFOMATION)

		#algorithm infomathon
		self.qt_ui.textBrowser_algorithm_msg.setHtml(Language.STR_TOPOMAPPING_INFOMATION)

		#slgorithm option setter
		self.qt_ui.radioButton_config_op2.setVisible(False)
		self.qt_ui.radioButton_config_op3.setVisible(False)
		self.qt_ui.radioButton_config_op4.setVisible(False) 
		self.qt_ui.comboBox_metric.setVisible(False)

	def set_line3_file_in_layout(self,state):
		self.qt_ui.label_7.setVisible(state)
		self.qt_ui.lineEdit_filein_3.setVisible(state)
		self.qt_ui.pushButton_openfile_3.setVisible(state)
		self.qt_ui.pushButton_exefile_3.setVisible(state)
		self.qt_ui.label_8.setVisible(state)
		self.qt_ui.textEdit_exestate_3.setVisible(state)

	def option_setting(self):
		self.qt_ui.radioButton_config_op1.setText('Debug Mode')

		self.qt_ui.radioButton_algorithm_1.setText('TopoMapping')
		self.qt_ui.radioButton_algorithm_2.setText('MPIPP')
		self.qt_ui.radioButton_algorithm_3.setText('TreeMatch')


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

		#Config settings
		self.Config_Setter1=ConfigBox_Window(self)
		self.Config_Setter1.changewindow(1)
		self.qt_ui.pushButton_cf_set1.clicked.connect(self.Config_Setter1.Configwindow_show)

		self.Config_Setter2=ConfigBox_Window(self)
		self.Config_Setter2.changewindow(0)
		self.qt_ui.pushButton_cf_set2.clicked.connect(self.Config_Setter2.Configwindow_show)

		#file analysis
		self.File_Analysis1=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_1,self.qt_ui.textEdit_exestate_1,1)
		self.qt_ui.pushButton_exefile_1.clicked.connect(self.File_Analysis1.file_analysis)

		self.File_Analysis2=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_2,self.qt_ui.textEdit_exestate_2,2)
		self.qt_ui.pushButton_exefile_2.clicked.connect(self.File_Analysis2.file_analysis)

		self.File_Analysis3=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_3,self.qt_ui.textEdit_exestate_3,3)
		self.qt_ui.pushButton_exefile_3.clicked.connect(self.File_Analysis3.file_analysis)

		#graph show
		self.Graph_Show=GraphBox_Window(self)
		self.qt_ui.pushButton_tg_show.clicked.connect(self.Graph_Show.graphshow)
		self.qt_ui.pushButton_ng_show.setEnabled(False)

		#algorithm caculate
		self.Caculate_begin=Algorithm_begin(self,Algorithm_manage.TOPOMAPPING,self.File_Browser3)
		self.qt_ui.pushButton_caculate.clicked.connect(self.Caculate_begin.Algorithm_run)

		self.Result_Show=ResultBox_window(self)



	def activity_binding(self):
		#configure setting button released => file analysis button enabled
		#self.qt_ui.pushButton_cf_set1.released.connect(lambda:self.qt_ui.pushButton_exefile_1.setEnabled(True))
		#self.qt_ui.pushButton_cf_set2.released.connect(lambda:self.qt_ui.pushButton_exefile_2.setEnabled(True))

		#file changed ==> analysis file state clear
		self.qt_ui.lineEdit_filein_1.textChanged.connect(self.qt_ui.textEdit_exestate_1.clear)
		self.qt_ui.lineEdit_filein_2.textChanged.connect(self.qt_ui.textEdit_exestate_2.clear)

		#file analysis done ==> graph show button enabled
		self.qt_ui.textEdit_exestate_1.textChanged.connect(lambda:self.qt_ui.pushButton_tg_show.setEnabled(True) if self.qt_ui.textEdit_exestate_1.toPlainText() == 'Done' else 0)

		#tgfile type == tgt/xml ==> config window changed to type 2
		self.qt_ui.comboBox_ngfiletype.currentIndexChanged.connect(self.activity_set_tgt)

		#algorithm changed ==> option setter change
		self.qt_ui.radioButton_algorithm_1.clicked.connect(self.activity_set_Algorithm_TopoMapping)
		self.qt_ui.radioButton_algorithm_2.clicked.connect(self.activity_set_Algorithm_MPIPP)
		self.qt_ui.radioButton_algorithm_3.clicked.connect(self.activity_set_Algorithm_TreeMatch)

		#TreeMatch:-b set ==> file 3 input
		self.qt_ui.radioButton_config_op2.toggled.connect(lambda x:self.set_line3_file_in_layout(x))

		#debug option checked ==> open debug mode
		self.qt_ui.radioButton_config_op1.toggled.connect(self.activity_set_Debug_Mode)

	@QtCore.Slot()
	def activity_set_tgt(self):
		if self.qt_ui.comboBox_ngfiletype.currentText() == '.tgt':
			self.Config_Setter2.changewindow(2)
		elif self.qt_ui.comboBox_ngfiletype.currentText() == '.xml':
			self.Config_Setter2.changewindow(2)
		else:
			self.Config_Setter2.changewindow(0)

	@QtCore.Slot()
	def activity_set_Algorithm_TopoMapping(self):
		self.qt_ui.radioButton_config_op2.setVisible(False)
		self.qt_ui.radioButton_config_op3.setVisible(False)
		self.qt_ui.radioButton_config_op4.setVisible(False) 
		self.qt_ui.comboBox_metric.setVisible(False)
		self.set_line3_file_in_layout(False)
	@QtCore.Slot()
	def activity_set_Algorithm_MPIPP(self):
		self.qt_ui.radioButton_config_op2.setVisible(False)
		self.qt_ui.radioButton_config_op3.setVisible(False)
		self.qt_ui.radioButton_config_op4.setVisible(False) 
		self.qt_ui.comboBox_metric.setVisible(False)
		self.set_line3_file_in_layout(False)
	@QtCore.Slot()
	def activity_set_Algorithm_TreeMatch(self):
		self.qt_ui.radioButton_config_op2.setVisible(True)
		self.qt_ui.radioButton_config_op3.setVisible(True)
		self.qt_ui.radioButton_config_op4.setVisible(True) 
		self.qt_ui.comboBox_metric.setVisible(True)
		self.qt_ui.radioButton_config_op2.setText("-b")
		self.qt_ui.radioButton_config_op2.setToolTip("binding constraint file")
		self.qt_ui.radioButton_config_op3.setText("-d")
		self.qt_ui.radioButton_config_op3.setToolTip("disable topology optimization")
		self.qt_ui.radioButton_config_op4.setText("-m")
		self.qt_ui.radioButton_config_op4.setToolTip("evaluation metric")
		if self.qt_ui.radioButton_config_op2.isChecked():
			self.set_line3_file_in_layout(True)
	@QtCore.Slot()
	def activity_set_Debug_Mode(self):
		if self.qt_ui.radioButton_config_op1.isChecked():
			Sys_logger.setLevel(LOG_DEBUG)
		else :
			Sys_logger.setLevel(LOG_INFO)

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