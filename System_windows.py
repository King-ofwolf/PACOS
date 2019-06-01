#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 15:25:06
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-06-01 22:52:32
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

# 将python执行的路径替换为代码根目录，确保所有文件的读取和写入都正确
SYSTEM_RUN_PATH, SYSTEM_RUN_FILE = os.path.split(os.path.abspath(sys.argv[0])) 
os.chdir(SYSTEM_RUN_PATH)

from PyQt4 import QtGui,QtCore,QtWebKit
from Layout import Language,Opration_gui,MsgBox_gui,ConfigBox_gui,Graph_gui,ResultBox_gui,MainWindow_gui
from Run_log import Sys_logger,LOG_DEBUG,LOG_INFO

import Algorithm_manage

#全局化消息提示窗口，用来在任何位置都能直接呼出提示窗口
global msgwindow
#PyQt和PySide的转换过程
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot

'''
写在前面：
本文件为系统主执行文件，其中主要为各个界面的类（*_Window），以及其中各个控件的响应事件的定义，还有各个事件的类

其中，基本所有的界面类都有以下函数，其作用都大抵相同：
	_init()	初始化变量
	paint_UI()	使用静态布局文件渲染界面
	center()	将界面调整到显示器中间
	button_binding	将按钮与事件槽绑定
	activity_binding	将事件与事件槽绑定
	activity_*()	事件槽
'''

class MsgBox_Window(QtGui.QWidget):
	"""A message window that can hold a String type of message to show in a private window when _msg changed to the message"""
	"""
	消息显示窗口，负责显示提示信息和错误信息
	_init()	初始化变量
	paint_UI()	使用静态布局文件渲染界面
	center()	将界面调整到显示器中间
	button_binding	事件绑定
	activity_*	事件槽
	"""
	def __init__(self,parent):
		super(MsgBox_Window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self.center()
		self.button_binding()
		self._init()

	def _init(self):
		self._msg="message info"
		self._exception=None
		self._detail=None

	def paint_UI(self):
		self.qt_ui=MsgBox_gui.Ui_Dialog()
		self.qt_ui.setupUi(self)
		self.qt_ui.textBrowser_detail.setVisible(False)

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def button_binding(self):
		#ok button binding with close the window
		self.qt_ui.pushButton.clicked.connect(self.topclose)

		#detail button ==> show details
		self.qt_ui.pushButton_detail.clicked.connect(self.activity_detail_show)

	@QtCore.Slot()
	def activity_detail_show(self):
		'''显示detal信息，窗口大小变大，detal按钮无效化'''
		self.qt_ui.textBrowser_detail.setVisible(True)
		self.fixsize('maxinum')
		self.qt_ui.pushButton_detail.setEnabled(False)

	def fixsize(self,flag):
		if flag == 'maxinum':
			self.setGeometry(QtCore.QRect(0, 0, 1000, 300))
		else :
			self.setGeometry(QtCore.QRect(0, 0, 400, 300))
		self.center()

	@property
	def msg(self):
		return self._msg
	#_msg's setter, whenever the _msg changed, close the parent window and show message window with that message
	@msg.setter
	def msg(self,msgstr):
		'''当msg被改变/设置的时候，都将调出信息显示界面，并显示提示/错误信息，并在detail界面显示exception/detail'''
		self._msg=msgstr
		if self._exception!=None:
			self.qt_ui.textBrowser_detail.setText(Language.QTLanguageTranslate("Details:\n"+str(traceback.format_exc())))
		elif not self._detail==None:
			self.qt_ui.textBrowser_detail.setText(Language.QTLanguageTranslate("Details:\n"+str(self._detail)))
		else:
			self.qt_ui.textBrowser_detail.setText("Details:")
		self.qt_ui.textBrowser.setText(msgstr)
		self.parent.setVisible(False)
		self.show()

	# a slot that can be bind to close the window and show the parent window
	@QtCore.Slot()
	def topclose(self):
		self.close()

	def closeEvent(self,event):
		'''窗口关闭的事件槽，所有关闭窗口的操作都会执行此函数'''
		self.parent.setVisible(True)	#显示父窗口
		self.qt_ui.textBrowser_detail.setVisible(False)	#初始化detail界面
		self.qt_ui.pushButton_detail.setEnabled(True)	#初始化detail按钮
		self._init()	#初始化所有信息变量
		self.fixsize('mininum')	#初始化窗口大小
		event.accept()	#关闭窗口


	@property
	def exception(self):
		return self._exception
	@exception.setter
	def exception(self,msgexception):
		self._exception=msgexception
	@property
	def detail(self):
		return self._detail
	@detail.setter
	def detail(self,detail):
		self._detail=detail
	
	

class ConfigBox_Window(QtGui.QWidget):
	"""ConfigBox Window"""
	"""
	配置窗口，主要用来配置输入数据的各项参数，窗口具有五个配置项目，根据需要进行显示/隐藏
	"""
	def __init__(self,parent):
		super(ConfigBox_Window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self.center()
		self.button_binding()
		self._options=[0,0,0,0,0]
		self._windows=0	#窗口类型

	def paint_UI(self):
		self.qt_ui=ConfigBox_gui.Ui_Form()
		self.qt_ui.setupUi(self)
		self.qt_ui.lineEdit_in_1.setValidator(QtGui.QIntValidator())	#设置数据可输入类型为int
		self.qt_ui.lineEdit_in_2.setValidator(QtGui.QIntValidator())
		self.qt_ui.lineEdit_in_3.setValidator(QtGui.QIntValidator())
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def button_binding(self):
		self.qt_ui.pushButton_cancel.clicked.connect(self.cancelclose)	#按下取消按钮
		self.qt_ui.pushButton_ensure.clicked.connect(self.ensureclose)	#按下确定按钮
	
	def changewindow(self,wtype):
		#改变窗口类型
		self._windows=wtype

	def getopt(self):
		#返回配置项数组
		return self._options

	def setopt(self,options):
		#设置五项配置项的初始值
		self._options=options[0:5]

	def set_option_visible(self,options):
		'''设置五项配置项为显示/隐藏'''
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
		'''显示配置窗口，并设置相应配置名称和显示/隐藏'''
		self.qt_ui.lineEdit_in_1.setText(str(self._options[0]))
		self.qt_ui.lineEdit_in_2.setText(str(self._options[1]))
		self.qt_ui.lineEdit_in_3.setText(str(self._options[2]))
		self.qt_ui.lineEdit_in_4.setText(str(self._options[3]))
		self.qt_ui.lineEdit_in_5.setText(str(self._options[4]))
		if self._windows == 0:	#net of .txt config window
			self.set_option_visible([True,True,True,False,False])
			self.setWindowTitle(Language.STR_CONFIGWINDOW_TITLE_NET)
		elif self._windows == 1:	#task config window
			self.qt_ui.label_cf_1.setText(Language.STR_TOTAL_TASK_NUM)
			self.set_option_visible([True,False,False,False,False])
			self.setWindowTitle(Language.STR_CONFIGWINDOW_TITLE_TASK)
		elif self._windows == 2:	#net of .tgt config window
			self.set_option_visible([True,False,False,False,False])
			self.setWindowTitle(Language.STR_CONFIGWINDOW_TITLE_BIND)

		self.parent.setVisible(False)
		self.show()
		Sys_logger.info("Configwindow show with type %d"%(self._windows))

	@QtCore.Slot()
	def ensureclose(self):
		'''确认事件槽，将各项输入的配置选项保存，并关闭窗口，显示父窗口'''
		self._options[0]=int(self.qt_ui.lineEdit_in_1.text())
		self._options[1]=int(self.qt_ui.lineEdit_in_2.text())
		self._options[2]=int(self.qt_ui.lineEdit_in_3.text())
		self.close()
		self.parent.setVisible(True)
		Sys_logger.info("Configwindow ensure close with option %d %d %d"%(self._options[0],self._options[1],self._options[2]))
	@QtCore.Slot()
	def cancelclose(self):
		'''取消事件槽，关闭窗口，显示父窗口'''
		self.close()
		self.parent.setVisible(True)
		Sys_logger.info("Configwindow cancel close")

	def closeEvent(self,event):
		#内置窗口关闭事件槽，所有关闭窗口的操作都会调用此函数
		self.parent.setVisible(True)
		event.accept()

class Open_File_Browser(QtCore.QObject):
	"""A window to let user to choose a file from path and return the file path"""
	"""
	打开文件浏览器，主要功能就是打开文件浏览器，并返回需要打开的文件路径
	"""
	# a signal that whenever the _last_filepath changed, the _lineEdit will be changed too
	setFilepath=QtCore.Signal(str)
	def __init__(self,parent,lineEdit):
		super(Open_File_Browser, self).__init__()
		self._last_filepath=str('')
		self._lineEdit = lineEdit
		self.setFilepath.connect(self.setlineEdit)	#setFilepath信号绑定到setlineEdit事件槽
		self.parent=parent
		self.available=True

	#save the file path which user choose
	@property
	def last_filepath(self):
		#返回文件路径的绝对路径
		self._last_filepath=self._lineEdit.text()
		if os.path.isabs(self._last_filepath):
			return self._last_filepath
		else :
			return os.path.join(os.getcwd(),self._last_filepath)
	@last_filepath.setter
	def last_filepath(self,new_filepath):
		#每当保存的文件路径更改时，都会发出setFilepath事件信号，信号值为需要改变的路径
		self._last_filepath=new_filepath
		self.setFilepath.emit(new_filepath) #once the file path changed, changed the lineEdit
	
	@QtCore.Slot(str)
	def setlineEdit(self,new_filepath):
		#改变文本框内的值
		self._lineEdit.setText(new_filepath)

	@QtCore.Slot()
	def opendialog(self):
		#打开文件浏览器changa
		filename = QtGui.QFileDialog.getOpenFileName(self._lineEdit,"Open file","./")
		if filename != '':
			self.last_filepath=filename

class Open_Folder_Browser(Open_File_Browser,QtCore.QObject):
	"""继承自文件浏览器窗口，其主要目的是为了打开文件夹，并返回文件夹的路径"""
	@QtCore.Slot()
	def opendialog(self):
		filename = QtGui.QFileDialog.getExistingDirectory(self._lineEdit,"Open folder","./")
		if filename != '':
			self.last_filepath=filename

class Open_File_Analysis(QtCore.QObject):
	"""docstring for Open_File_Analysis"""
	"""
	文件解析类，主要目的是为了和算法管理模块对接，并调用指定的函数进行文件解析
	主要有通信拓扑数据解析、网络拓扑数据解析，根据order来进行区分
	"""
	def __init__(self,parent,lineEdit,textEdit,order):
		super(Open_File_Analysis, self).__init__()
		self._lineEdit=lineEdit
		self._textEdit=textEdit
		self.order=order	#窗口的类型，1是指第一种解析方式（解析通信拓扑数据）
		self.filetype=''
		self.retmodule=None
		self.parent=parent

	def file_exist(self, filepath):
		'''判断文件/文件夹是否存在并且可读'''
		if os.path.exists(filepath) & os.path.isfile(filepath) & os.access(filepath,os.R_OK):
			return True
		elif os.path.exists(filepath) & os.path.isdir(filepath) & os.access(filepath,os.R_OK) & (self.filetype=="Dir"):
			return True
		else:
			return False

	def get_file_type(self):
		'''获取用户设置的文件类型'''
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
		'''文件解析操作事件槽，调用算法管理模块的数据读取函数进行解析，若解析失败则返回None，否则返回读取的模型以及信息'''
		self.get_file_type()	#获取文件类型
		#检测文件是否存在
		if not self.file_exist(self._lineEdit.text()):
			self._textEdit.setTextColor(QtGui.QColor("red"))
			self._textEdit.setText("Wrong")
			msgwindow.msg="file not exists!"
		else:
			#尝试进行解析，若解析异常则弹出信息提示界面
			try:
				if self.order == 1:#file analysis of task graph
					task_size=self.parent.Config_Setter1.getopt()[0]
					[self.retmodule,msgwindow.detail]=Algorithm_manage.Load_task_graph(
						self._lineEdit.text(),
						self.filetype,
						[task_size,])
				elif self.order == 2:#file analysis of net graph
					[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
					self.retmodule=Algorithm_manage.Load_net_graph(
						self._lineEdit.text(),
						self.filetype,
						[net_ct,net_node,net_core,m,n])
				elif self.order == 3:
					self.retmodule=Algorithm_manage.Load_option(self._lineEdit.text())
				else:
					self.retmodule=None
			except Exception as e:
				msgwindow.exception=e
				self.retmodule=None
			else:
				pass
			finally:
				pass
			if self.retmodule==None:	#解析失败，设置状态栏的文本，并弹出信息提示界面
				self._textEdit.setTextColor(QtGui.QColor("red"))
				self._textEdit.setText("Wrong")
				msgwindow.msg="Load failed!"
			else:	#解析成功，设置状态烂文本
				self._textEdit.setTextColor(QtGui.QColor("green"))
				self._textEdit.setText("Done")

class GraphBox_Window(QtGui.QWidget):
	"""docstring for GraphBox_Window"""
	"""
	图形显示窗口，主要目的是显示可视化输入数据，载入html文件进行展示，并提供使用浏览器打开的按钮
	"""
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
		self.qt_ui.pushButton.clicked.connect(self.openBrowser)	#打开浏览器

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	@QtCore.Slot()
	def graphshow(self):
		'''窗口显示事件槽，载入html文件，隐藏父窗口，显示本窗口'''
		self.weburl=QtCore.QUrl(self.graphpath)
		self.webview.load(self.weburl)
		self.parent.setVisible(False)
		self.show()

	def closeEvent(self,event):
		#内置关闭窗口事件槽，所有关闭窗口的事件都会调用此函数，显示父窗口，关闭本窗口
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
	"""
	结果展示界面，主要作用是展示映射结果，包括散点图、映射序列、图形化显示
	"""
	def __init__(self,parent,graphpath='./Graph/mapgraph.html',treepath='./Graph/treegraph.html'):
		super(ResultBox_window, self).__init__()
		self.parent=parent
		self.graphpath=graphpath
		self.treepath=treepath
		self.paint_UI()
		self.center()

	def paint_UI(self):
		self.qt_ui=ResultBox_gui.Ui_Dialog()
		self.qt_ui.setupUi(self)
		self.webview=QtWebKit.QWebView(self.qt_ui.tab)	#窗口1,显示散点图
		self.treewebview=QtWebKit.QWebView(self.qt_ui.tab_3)	#窗口3,显示图形化热力图

		self.qt_ui.label_5.setVisible(False)	#预留的信息显示条，暂时未用上，因此不显示
		self.qt_ui.label_cputime.setVisible(False)

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	@QtCore.Slot()
	def resultshow(self):
		#窗口显示事件槽
		self.parent.setVisible(False)
		self.show()
		
	def closeEvent(self,event):
		#内置窗口关闭事件槽
		self.parent.setVisible(True)
		event.accept()

	def setResult(self,Slist,ct=1024):
		'''载入结果，显示各项数据'''
		self.qt_ui.listWidget.clear()
		#data tab
		#为每一个映射关系设置一个条目
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

		#treemap tab
		self.treeweburl=QtCore.QUrl(self.treepath)
		self.treewebview.load(self.treeweburl)

	def setAlgorithmmsg(self,algotype,tasknum,corenum,caculate_time,CPU_time):
		'''设置算法信息的显示'''
		self.qt_ui.label_algorithm.setText(Algorithm_manage.ALGORITHM_NAME[algotype])
		self.qt_ui.label_tasknum.setText(str(tasknum))
		self.qt_ui.label_corenum.setText(str(corenum))
		self.qt_ui.label_caculatetime.setText(str(caculate_time))
		self.qt_ui.label_cputime.setText(str(CPU_time))

	#translate the result net to task into task to net (S to ST)
	def ResultTranslate(self,Slist,ct):
		'''用于将“节点-进程”的对应关系转换成“进程-节点”'''
		count=0
		Stemp=[-1 for i in range(ct)]
		for s in Slist:
			Stemp[s]=count
			count+=1
		return Stemp

class Algorithm_begin(QtCore.QObject):
	"""docstring for Algorithm_begin"""
	"""
	算法开始，主要目的是为了对接算法管理模块，进行根据选择的算法进行算法调用，并接收算法返回值，调出结果展示界面
	"""
	def __init__(self, parent, algotype, configures):
		super(Algorithm_begin, self).__init__()
		self.algotype=algotype
		self.configures=configures
		self.parent=parent

	def Algorithm_choose(self):
		'''查看用户选择的算法是哪一个'''
		if self.parent.qt_ui.radioButton_algorithm_1.isChecked():
			self.algotype=Algorithm_manage.TOPOMAPPING
		elif self.parent.qt_ui.radioButton_algorithm_2.isChecked():
			self.algotype=Algorithm_manage.MPIPP
		elif self.parent.qt_ui.radioButton_algorithm_3.isChecked():
			self.algotype=Algorithm_manage.TREEMATCH

	@QtCore.Slot()
	def Algorithm_run(self):
		'''算法执行函数'''
		self.parent.set_waiting()	#使父窗口等待，直到算法调用结束
		#获取输入的三项文件的路径
		alg_tgfile=str(self.parent.qt_ui.lineEdit_filein_1.text())
		alg_ngfile=str(self.parent.qt_ui.lineEdit_filein_2.text())
		alg_cgfile=str(self.parent.qt_ui.lineEdit_filein_3.text())	#algorithm config file
		#判断通信数据文件是否是一个目录类型的文件
		alg_tgfile_isdir = self.parent.qt_ui.comboBox_tgfiletype.currentText() == "Dir"
		#尝试进行计算，若出现异常则弹出提示窗口
		try:
			#获取两项数据的配置参数
			task_size=self.parent.Config_Setter1.getopt()[0]
			[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
			#获取用户选择的算法
			self.Algorithm_choose()
			if self.algotype == Algorithm_manage.TOPOMAPPING:
				if alg_tgfile_isdir:	#若通信数据文件是目录类型，则使用其内部的result文件夹内的对应文件
					alg_tgfile=os.path.join(alg_tgfile,"result_file/ProcessCommTrace_"+str(task_size)+".TOPO")
				self.result,runtime,cputime=Algorithm_manage.Algorithm_run(
					Algorithm_manage.TOPOMAPPING,alg_tgfile,alg_ngfile,
					task_size=task_size,
					net_ct=net_ct,
					net_node=net_node,
					net_core=net_core)
			elif self.algotype == Algorithm_manage.MPIPP:
				if alg_tgfile_isdir:
					alg_tgfile=os.path.join(alg_tgfile,"result_file/ProcessCommTrace_"+str(task_size)+".MPIPP")
				ngfile_type = self.parent.qt_ui.comboBox_ngfiletype.currentText()
				self.result,runtime,cputime=Algorithm_manage.Algorithm_run(
					Algorithm_manage.MPIPP,alg_tgfile,alg_ngfile,
					nfile_type=ngfile_type,
					ct=net_ct,
					node=net_node,
					core=net_core)
			elif self.algotype == Algorithm_manage.TREEMATCH:
				if alg_tgfile_isdir:
					alg_tgfile=os.path.join(alg_tgfile,"result_file/ProcessCommTrace_"+str(task_size)+".mat")
				#获取其他配置选项
				ngfile_type = self.parent.qt_ui.comboBox_ngfiletype.currentText()
				bind_choose = self.parent.qt_ui.radioButton_config_op2.isChecked()
				bind_file = alg_cgfile if bind_choose else ''
				optimization = not self.parent.qt_ui.radioButton_config_op3.isChecked()
				metric=self.parent.qt_ui.comboBox_metric.currentIndex()+1
				self.result,runtime,cputime=Algorithm_manage.Algorithm_run(
					Algorithm_manage.TREEMATCH,alg_tgfile,alg_ngfile,
					nfile_type=ngfile_type,
					bind_file=bind_file,
					optimization=optimization,
					metric=metric)
			#显示结果展示界面
			self.parent.Result_Show.setResult(self.result,net_ct)
			self.parent.Result_Show.setAlgorithmmsg(self.algotype,task_size,net_ct,runtime,cputime)
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

class Main_Window(QtGui.QWidget):
	"""docstring for Main_Window"""
	"""系统主界面"""
	def __init__(self,parent):
		super(Main_Window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self._init()
		self.option_setting()
		self.button_binding()
		self.activity_binding()
		
	def paint_UI(self):
		self.qt_ui=Opration_gui.Ui_Form()
		self.qt_ui.setupUi(self.parent)

	def _init(self):
		#disabled at begin
		'''初始化一些控件的初始可用性'''
		self.qt_ui.pushButton_tg_show.setEnabled(False)
		self.qt_ui.pushButton_ng_show.setEnabled(False)
		self.qt_ui.pushButton_caculate.setEnabled(False)
		#line3 file in layout
		self.set_line3_file_in_layout(False)	#第三行的文件输入窗口初始不显示

		#algorithm match button 
		self.qt_ui.pushButton_algorithm_match.setVisible(False)	#算法匹配按钮暂时没用上

		#file input infomation
		self.qt_ui.textBrowser_filein_msg.setHtml(Language.STR_FILE_INPUT_INFOMATION)

		#algorithm infomation
		self.qt_ui.textBrowser_algorithm_msg.setHtml(
			Language.QTtextBrowserTranslate(
				Algorithm_manage.ALGORITHM_INFO[Algorithm_manage.TOPOMAPPING])
			)

		#slgorithm option setter
		self.qt_ui.radioButton_config_op2.setVisible(False)
		self.qt_ui.radioButton_config_op3.setVisible(False)
		self.qt_ui.radioButton_config_op4.setVisible(False) 
		self.qt_ui.comboBox_metric.setVisible(False)

	def set_line3_file_in_layout(self,state):
		'''设置第三行文件输入栏的可见性'''
		self.qt_ui.label_7.setVisible(state)
		self.qt_ui.lineEdit_filein_3.setVisible(state)
		self.qt_ui.pushButton_openfile_3.setVisible(state)
		self.qt_ui.pushButton_exefile_3.setVisible(state)
		self.qt_ui.label_8.setVisible(state)
		self.qt_ui.textEdit_exestate_3.setVisible(state)

	def option_setting(self):
		'''设置配置栏第一项、算法的文本'''
		self.qt_ui.radioButton_config_op1.setText('Debug Mode')
		self.qt_ui.radioButton_algorithm_1.setText('TopoMapping')
		self.qt_ui.radioButton_algorithm_2.setText('MPIPP')
		self.qt_ui.radioButton_algorithm_3.setText('TreeMatch')


	def button_binding(self):
		#open button in line 1 bind to file browser and line edit 1
		#通信拓扑数据文件打开按钮，绑定到文件浏览器或者文件夹浏览器
		self.File_Browser1=Open_File_Browser(self,self.qt_ui.lineEdit_filein_1)
		self.Folder_Browser1=Open_Folder_Browser(self,self.qt_ui.lineEdit_filein_1)
		self.qt_ui.pushButton_openfile_1.clicked.connect(self.File_Browser1.opendialog)
		#open button in line 2 bind to file browser and line edit 2
		#网络拓扑数据文件打开按钮，绑定到文件浏览器
		self.File_Browser2=Open_File_Browser(self,self.qt_ui.lineEdit_filein_2)
		self.qt_ui.pushButton_openfile_2.clicked.connect(self.File_Browser2.opendialog)
		#open button in line 3 bind to file browser and line edit 3
		#配置文件打开按钮，绑定到文件浏览器
		self.File_Browser3=Open_File_Browser(self,self.qt_ui.lineEdit_filein_3)
		self.qt_ui.pushButton_openfile_3.clicked.connect(self.File_Browser3.opendialog)

		#Config settings
		#通信拓扑数据配置按钮，绑定到配置窗口,窗口类型为1
		self.Config_Setter1=ConfigBox_Window(self)
		self.Config_Setter1.changewindow(1)
		self.qt_ui.pushButton_cf_set1.clicked.connect(self.Config_Setter1.Configwindow_show)
		#网络拓扑数据配置按钮，绑定到配置窗口，窗口类型为0
		self.Config_Setter2=ConfigBox_Window(self)
		self.Config_Setter2.changewindow(0)
		self.qt_ui.pushButton_cf_set2.clicked.connect(self.Config_Setter2.Configwindow_show)

		#file analysis
		#通信拓扑数据文件解析按钮，绑定到文件解析函数
		self.File_Analysis1=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_1,self.qt_ui.textEdit_exestate_1,1)
		self.qt_ui.pushButton_exefile_1.clicked.connect(self.File_Analysis1.file_analysis)
		#网络拓扑数据文件解析按钮，绑定到文件解析函数
		self.File_Analysis2=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_2,self.qt_ui.textEdit_exestate_2,2)
		self.qt_ui.pushButton_exefile_2.clicked.connect(self.activity_Net_file_analysis)
		#配置数据文件解析按钮，绑定到文件解析函数
		self.File_Analysis3=Open_File_Analysis(self,self.qt_ui.lineEdit_filein_3,self.qt_ui.textEdit_exestate_3,3)
		self.qt_ui.pushButton_exefile_3.clicked.connect(self.File_Analysis3.file_analysis)

		#graph show
		#通信拓扑图形展示按钮，绑定到展示窗口
		self.Task_Graph_Show=GraphBox_Window(self,graphpath='./Graph/taskgraph.html')
		self.qt_ui.pushButton_tg_show.clicked.connect(self.Task_Graph_Show.graphshow)
		#网络拓扑图形展示按钮，绑定到展示窗口
		self.Net_Graph_Show=GraphBox_Window(self,graphpath='./Graph/netgraph.html')
		self.qt_ui.pushButton_ng_show.clicked.connect(self.Net_Graph_Show.graphshow)

		#algorithm caculate
		#算法计算按钮，绑定到算法计算函数
		self.Caculate_begin=Algorithm_begin(self,Algorithm_manage.TOPOMAPPING,self.File_Browser3)
		self.qt_ui.pushButton_caculate.clicked.connect(self.Caculate_begin.Algorithm_run)

		#结果展示界面
		self.Result_Show=ResultBox_window(self)



	def activity_binding(self):
		#file changed ==> analysis file state clear
		#当文件输入框内容改变时（即用户重新选择了数据文件），则解析状态重置为空
		self.qt_ui.lineEdit_filein_1.textChanged.connect(self.qt_ui.textEdit_exestate_1.clear)
		self.qt_ui.lineEdit_filein_2.textChanged.connect(self.qt_ui.textEdit_exestate_2.clear)

		#file analysis done ==> graph show button enabled
		#当文件解析结果为Done时，图形展示按钮才设置为可用，其他情况都为不可用
		self.qt_ui.textEdit_exestate_1.textChanged.connect(
			lambda:
			self.qt_ui.pushButton_tg_show.setEnabled(True) 
			if self.qt_ui.textEdit_exestate_1.toPlainText() == 'Done' 
			else self.qt_ui.pushButton_tg_show.setEnabled(False)
			)
		self.qt_ui.textEdit_exestate_2.textChanged.connect(
			lambda:
			self.qt_ui.pushButton_ng_show.setEnabled(True)
			if self.qt_ui.textEdit_exestate_2.toPlainText() == 'Done' 
			and self.qt_ui.comboBox_ngfiletype.currentText() == '.txt'
			else self.qt_ui.pushButton_ng_show.setEnabled(False)
			)

		#ngfile type == Dir ==> open file button connected to open folder
		#当用户选择的通信数据文件类型改变时，执行相应事件
		self.qt_ui.comboBox_tgfiletype.currentIndexChanged.connect(self.activity_set_dir)

		#tgfile type == tgt/xml ==> config window changed to type 2
		#当用户选择的网络数据文件类型改变时，执行相应事件
		self.qt_ui.comboBox_ngfiletype.currentIndexChanged.connect(self.activity_set_tgt)

		#optimization option changed ==> algorithm recommend change
		#当用户改变优化选项时，执行相应事件
		self.qt_ui.comboBox_optimization.currentIndexChanged.connect(self.activity_algorithm_recommend)

		#algorithm changed ==> option setter change
		#当用户选择不同的算法时，执行相应事件
		self.qt_ui.radioButton_algorithm_1.toggled.connect(self.activity_set_Algorithm_TopoMapping)
		self.qt_ui.radioButton_algorithm_2.toggled.connect(self.activity_set_Algorithm_MPIPP)
		self.qt_ui.radioButton_algorithm_3.toggled.connect(self.activity_set_Algorithm_TreeMatch)

		#TreeMatch:-b set ==> file 3 input
		#对于TreeMatch算法，当用户改变了-b选项的状态时，显示/隐藏第三行的配置文件输入栏
		self.qt_ui.radioButton_config_op2.toggled.connect(lambda x:self.set_line3_file_in_layout(x))

		#debug option checked ==> open debug mode
		#当用户改变了debug选项的状态时，执行相应事件
		self.qt_ui.radioButton_config_op1.toggled.connect(self.activity_set_Debug_Mode)

		#communication file analysised ==> run algorithm button enabled
		#当通信数据文件和网络拓扑数据文件都解析成功并显示done时，算法执行按钮才被设置成可用，否则都为不可用
		self.qt_ui.textEdit_exestate_1.textChanged.connect(
			lambda:
			self.qt_ui.pushButton_caculate.setEnabled(True) 
			if self.qt_ui.textEdit_exestate_1.toPlainText() == 'Done'
			and self.qt_ui.textEdit_exestate_2.toPlainText() == 'Done'
			else self.qt_ui.pushButton_caculate.setEnabled(False)
			)
		self.qt_ui.textEdit_exestate_2.textChanged.connect(
			lambda:
			self.qt_ui.pushButton_caculate.setEnabled(True) 
			if self.qt_ui.textEdit_exestate_1.toPlainText() == 'Done'
			and self.qt_ui.textEdit_exestate_2.toPlainText() == 'Done'
			else self.qt_ui.pushButton_caculate.setEnabled(False)
			)

	@QtCore.Slot()
	def activity_Net_file_analysis(self):
		#网络拓扑解析事件槽，当按钮按下后，进行文件解析，并进行算法推荐
		self.File_Analysis2.file_analysis()
		self.activity_algorithm_recommend()

	@QtCore.Slot()
	def activity_set_dir(self):
		'''当用户改变了通信拓扑数据文件类型时：
		当改为Dir时，将文件浏览器状态设置为False，并解除文件浏览器与文件解析按钮的绑定关系，改为绑定到文件夹浏览器
		当改成其他类型时，若文件浏览器状态为False，则解除文件夹浏览器与文件解析按钮的绑定关系，改为绑定到文件浏览器'''
		if self.qt_ui.comboBox_tgfiletype.currentText() == 'Dir':
			self.File_Browser1.available=False
			self.qt_ui.pushButton_openfile_1.clicked.disconnect(self.File_Browser1.opendialog)
			self.qt_ui.pushButton_openfile_1.clicked.connect(self.Folder_Browser1.opendialog)
		elif self.File_Browser1.available == False:
			self.File_Browser1.available=True
			self.qt_ui.pushButton_openfile_1.clicked.disconnect(self.Folder_Browser1.opendialog)
			self.qt_ui.pushButton_openfile_1.clicked.connect(self.File_Browser1.opendialog)
	@QtCore.Slot()
	def activity_set_tgt(self):
		'''当用户改变了网络拓扑数据文件类型时：
		当改为tgt时，更改配置选项窗口为2类型
		当改为xml时，更改配置选项窗口为2类型
		当改为其他类型时，更改配置选项窗口为0类型'''
		if self.qt_ui.comboBox_ngfiletype.currentText() == '.tgt':
			self.Config_Setter2.changewindow(2)
		elif self.qt_ui.comboBox_ngfiletype.currentText() == '.xml':
			self.Config_Setter2.changewindow(2)
		else:
			self.Config_Setter2.changewindow(0)

	@QtCore.Slot(bool)
	def activity_set_Algorithm_TopoMapping(self,checked):
		'''当用户选择了TopoMapping算法时'''
		if not checked: return
		self.qt_ui.radioButton_config_op2.setVisible(False)	#各项配置项隐藏
		self.qt_ui.radioButton_config_op3.setVisible(False)
		self.qt_ui.radioButton_config_op4.setVisible(False) 
		self.qt_ui.comboBox_metric.setVisible(False)
		self.set_line3_file_in_layout(False)	#第三行配置文件输入栏隐藏
		self.qt_ui.textBrowser_algorithm_msg.setHtml(
			Language.QTtextBrowserTranslate(
				Algorithm_manage.ALGORITHM_INFO[Algorithm_manage.TOPOMAPPING])
			)	#设置算法信息文本
	@QtCore.Slot(bool)
	def activity_set_Algorithm_MPIPP(self,checked):
		'''当用户选择了MPIPP算法时'''
		if not checked: return
		self.qt_ui.radioButton_config_op2.setVisible(False)	#各项配置项隐藏
		self.qt_ui.radioButton_config_op3.setVisible(False)
		self.qt_ui.radioButton_config_op4.setVisible(False) 
		self.qt_ui.comboBox_metric.setVisible(False)
		self.set_line3_file_in_layout(False)	#第三行配置文件输入栏隐藏
		self.qt_ui.textBrowser_algorithm_msg.setHtml(
			Language.QTtextBrowserTranslate(
				Algorithm_manage.ALGORITHM_INFO[Algorithm_manage.MPIPP])
			)	#设置算法信息文本
	@QtCore.Slot(bool)
	def activity_set_Algorithm_TreeMatch(self,checked):
		'''当用户选择了TreeMatch算法时'''
		if not checked: return
		#各项配置项显示，并设置各项的文本和相应的提示信息
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
		#当用户选择了-b选项时，显示第三行的配置文件输入栏
		if self.qt_ui.radioButton_config_op2.isChecked():
			self.set_line3_file_in_layout(True)
		self.qt_ui.textBrowser_algorithm_msg.setHtml(
			Language.QTtextBrowserTranslate(
				Algorithm_manage.ALGORITHM_INFO[Algorithm_manage.TREEMATCH])
			)	#设置算法信息文本
	@QtCore.Slot()
	def activity_set_Debug_Mode(self):
		#当用户改变了debug选项时，更改系统的调试等级
		if self.qt_ui.radioButton_config_op1.isChecked():
			Sys_logger.setLevel(LOG_DEBUG)
		else :
			Sys_logger.setLevel(LOG_INFO)
	@QtCore.Slot()
	def activity_algorithm_recommend(self):
		'''算法推荐事件，根据网络结构和用户选择的优化选项，调用算法管理模块中的推荐函数，进行算法推荐'''
		net_file_type=self.qt_ui.comboBox_ngfiletype.currentText()	#获取网络文件类型
		opts=self.qt_ui.comboBox_optimization.currentText()	#获取用户选择的优化选项
		algo=Algorithm_manage.Algorithm_recommend(net_file_type,opts)	#调用推荐函数
		#设置算法推荐文本，向用户显示推荐的算法名称
		self.qt_ui.label_algo_recommend.setText(Language.QTLanguageTranslate(Algorithm_manage.ALGORITHM_NAME[algo]))
		#根据推荐的算法，自动切换当前选择的算法
		if algo == Algorithm_manage.TREEMATCH:
			self.qt_ui.radioButton_algorithm_3.setChecked(True)
		elif algo == Algorithm_manage.MPIPP:
			self.qt_ui.radioButton_algorithm_2.setChecked(True)
		elif algo == Algorithm_manage.TOPOMAPPING:
			self.qt_ui.radioButton_algorithm_1.setChecked(True)

	def set_waiting(self):
		#设置鼠标为等待样式，窗口为不可用状态
		self.parent.setCursor(QtCore.Qt.WaitCursor)
		self.parent.setEnabled(False)

	def set_active(self):
		#对应窗口等待状态，恢复为可用状态，并将鼠标恢复
		self.parent.setCursor(QtCore.Qt.ArrowCursor)
		self.parent.setEnabled(True)

	def setVisible(self,flag):
		#设置窗口可见性
		self.parent.setVisible(flag)

class Window(QtGui.QMainWindow):
	"""main window's option menu"""
	"""系统主界面的菜单栏，主要功能是提供各项菜单内的操作，并改变界面的样式（未实现）"""
	def __init__(self):
		super(Window, self).__init__()
		self.option_file='./examples/examples.json'	#样例数据文件
		self.qss_file='./Layout/QSS/white_styles.css'	#样式文件
		self.paint_UI()
		self.paint_style()
		self.show()
		
	def paint_UI(self):
		self.qt_ui=MainWindow_gui.Ui_MainWindow()
		self.qt_ui.setupUi(self)
		self.add_example()
		self.mainwindow=Main_Window(self)

	def paint_style(self):
		#更改系统界面样式（未实现）
		pass
		# with open(self.qss_file,'r') as style_file:
		# 	style_sheet=style_file.read()
		# 	self.setStyleSheet(Language.QTLanguageTranslate(style_sheet))

	def add_example(self):
		'''载入系统样例数据文件，并显示在菜单栏的样例中'''
		self.actions=[]
		self.option_dics=[]
		with open(self.option_file) as opf:	#读取json文件
			examples_dic=json.load(opf)
		for algo in examples_dic:	#为每一条样例都生成一个子菜单
			sub_menu=QtGui.QMenu(self.qt_ui.menu_example)
			sub_menu.setTitle(algo)
			self.qt_ui.menu_example.addAction(sub_menu.menuAction())
			for exam in examples_dic[algo]:
				actionOption=QtGui.QAction(self)
				actionOption.setText(exam)
				actionOption.triggered.connect(functools.partial(self.set_example,options_dic=examples_dic[algo][exam],algo=algo))
				#actionOption.triggered.connect(lambda x:self.set_example(examples_dic[algo][exam]))
				sub_menu.addAction(actionOption)

	def set_example(self,options_dic={},algo=""):
		'''当用户点击样例中的一项子菜单时，根据样例数据，对系统各项进行配置，以符合当前样例的输入'''
		if algo == "TreeMatch":
			self.mainwindow.qt_ui.radioButton_algorithm_3.setChecked(True)
		elif algo == "MPIPP":
			self.mainwindow.qt_ui.radioButton_algorithm_2.setChecked(True)
		elif algo == "TopoMapping":
			self.mainwindow.qt_ui.radioButton_algorithm_1.setChecked(True)
		self.mainwindow.qt_ui.lineEdit_filein_1.setText(options_dic['task_file'])
		self.mainwindow.qt_ui.comboBox_tgfiletype.setCurrentIndex(self.mainwindow.qt_ui.comboBox_tgfiletype.findText(options_dic['task_type']))
		self.mainwindow.Config_Setter1.setopt([int(options_dic['task_num']),0,0,0,0])
		self.mainwindow.qt_ui.lineEdit_filein_2.setText(options_dic['net_file'])
		self.mainwindow.qt_ui.comboBox_ngfiletype.setCurrentIndex(self.mainwindow.qt_ui.comboBox_ngfiletype.findText(options_dic['net_type']))
		self.mainwindow.Config_Setter2.setopt([int(options_dic['net_ct']),int(options_dic['net_node']),int(options_dic['net_core']),0,0])



if __name__ == '__main__':
	global msgwindow
	app=QtGui.QApplication(sys.argv)
	mainwindow=Window()
	msgwindow=MsgBox_Window(mainwindow)
	app.exec_()