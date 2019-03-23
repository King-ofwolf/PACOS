#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-10 15:25:06
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-23 22:11:59
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-10 15:25:06'

import sys
import os
import subprocess
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit
from Layout import Language
from Layout import Opration_gui
from Layout import MsgBox_gui
from Layout import ConfigBox_gui
from Layout import Graph_gui
from Layout import ResultBox_gui
from Run_log import Sys_logger,LOG_DEBUG,LOG_INFO

import Algorithm_manage

global msgwindow
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot

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
			self.qt_ui.label_cf_2.setVisible(True)
			self.qt_ui.label_cf_3.setVisible(True)
			self.qt_ui.lineEdit_in_2.setVisible(True)
			self.qt_ui.lineEdit_in_3.setVisible(True)
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
		elif self._windows == 2:
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
				if self.filetype == '.APHiD':
					self.retmodule=Algorithm_manage.Load_task_graph_APHiD(self._lineEdit.text())
					if self.retmodule != None:
						if self.retmodule.size != task_size :
							msgwindow.msg="Task number in Task file is %d, but you set it as %d."%(self.retmodule.size,task_size)
							retmodule=None
				elif self.filetype == '.mat':
					self.retmodule=Algorithm_manage.Load_task_graph_MAT(self._lineEdit.text())
					if self.retmodule != None:
						if len(self.retmodule) != task_size:
							msgwindow.msg="Task number in Task file is %d, but you set it as %d."%(len(self.retmodule),task_size)
							retmodule=None
			elif self.order == 2:#file analysis of task graph
				if self.filetype == '.txt':
					[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
					self.retmodule=Algorithm_manage.Load_net_graph_txt(self._lineEdit.text(),net_ct,net_node,net_core)
				elif self.filetype == '.tgt':
					self.retmodule=Algorithm_manage.Load_net_graph_tgt(self._lineEdit.text())
				elif self.filetype == '.xml':
					pass#----------------------------------
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
	def __init__(self,parent):
		super(ResultBox_window, self).__init__()
		self.parent=parent
		self.paint_UI()
		self.center()

	def paint_UI(self):
		self.qt_ui=ResultBox_gui.Ui_Dialog()
		self.qt_ui.setupUi(self)
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
		#data tab
		item = self.qt_ui.listWidget.item(0).setText(Language.STR_RESULT_MAP)
		count=0
		for s in Slist:
			item = QtGui.QListWidgetItem()
			tempstr="%d\t%d"%(count,s)
			count+=1
			item.setText(tempstr)
			self.qt_ui.listWidget.addItem(item)

		#map tab
		#item = self.qt_ui.listWidget_2.item(0).setText(_translate("Dialog", "", None))
		Stemp=self.ResultTranslate(Slist,ct)
		index=0
		while index<ct:
			strtemp=''
			for i in range(9):
				if index >= ct:
					break
				strtemp+=str(index)+":"+str('*' if Stemp[index] == -1 else Stemp[index])+"\t"
				index+=1
			item=QtGui.QListWidgetItem()
			item.setText(strtemp)
			self.qt_ui.listWidget_2.addItem(item)


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
		try:
			task_size=self.parent.Config_Setter1.getopt()[0]
			[net_ct,net_node,net_core,m,n]=self.parent.Config_Setter2.getopt()
			self.Algorithm_choose()

			if self.algotype == Algorithm_manage.TOPOMAPPING:
				self.result=Algorithm_manage.Algorithm_run_TopoMapping(alg_tgfile,alg_ngfile,task_size,net_ct,net_node,net_core)
			elif self.algotype == Algorithm_manage.MPIPP:
				ngfile_type = self.parent.qt_ui.comboBox_ngfiletype.currentText()
				self.result=Algorithm_manage.Algorithm_run_MPIPP(alg_tgfile,alg_ngfile,ngfile_type,net_ct,net_node,net_core)

			self.parent.Result_Show.setResult(self.result,net_ct)
			self.parent.Result_Show.resultshow()
		except Exception as e:
			Sys_logger.debug(str(e))
			msgwindow.msg=Language.STR_CACULATE_FAILD
			raise
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
		self.option_setting()
		self.button_binding()
		self.activity_binding()
		self.show()
		
	def paint_UI(self):
		self.qt_ui=Opration_gui.Ui_Form()
		self.qt_ui.setupUi(self)
		#disabled at begin
		self.qt_ui.pushButton_exefile_1.setEnabled(False)
		self.qt_ui.pushButton_exefile_2.setEnabled(False)
		self.qt_ui.pushButton_tg_show.setEnabled(False)
		#line3 file in layout
		self.qt_ui.label_7.setVisible(False)
		self.qt_ui.lineEdit_filein_3.setVisible(False)
		self.qt_ui.pushButton_openfile_3.setVisible(False)
		self.qt_ui.pushButton_exefile_3.setVisible(False)
		self.qt_ui.label_8.setVisible(False)
		self.qt_ui.textEdit_exestate_3.setVisible(False)

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
		self.qt_ui.pushButton_cf_set1.released.connect(lambda:self.qt_ui.pushButton_exefile_1.setEnabled(True))
		self.qt_ui.pushButton_cf_set2.released.connect(lambda:self.qt_ui.pushButton_exefile_2.setEnabled(True))

		#file changed ==> analysis file state clear
		self.qt_ui.lineEdit_filein_1.textChanged.connect(self.qt_ui.textEdit_exestate_1.clear)
		self.qt_ui.lineEdit_filein_2.textChanged.connect(self.qt_ui.textEdit_exestate_2.clear)

		#file analysis done ==> graph show button enabled
		self.qt_ui.textEdit_exestate_1.textChanged.connect(lambda:self.qt_ui.pushButton_tg_show.setEnabled(True) if self.qt_ui.textEdit_exestate_1.toPlainText() == 'Done' else 0)

		#tgfile type == tgt ==> no config setting
		self.qt_ui.comboBox_ngfiletype.currentIndexChanged.connect(self.activity_set_tgt)

	@QtCore.Slot()
	def activity_set_tgt(self):
		if self.qt_ui.comboBox_ngfiletype.currentText() == '.tgt':
			self.Config_Setter2.changewindow(2)
		else:
			self.Config_Setter2.changewindow(0)

	def set_waiting(self):
		self.setCursor(QtCore.Qt.WaitCursor)
		self.setEnabled(False)

	def set_active(self):
		self.setCursor(QtCore.Qt.ArrowCursor)
		self.setEnabled(True)

if __name__ == '__main__':
	global msgwindow
	Sys_logger.setLevel(LOG_DEBUG)
	app=QtGui.QApplication(sys.argv)
	mainwindow=Main_Window()
	msgwindow=MsgBox_Window(mainwindow)
	app.exec_()