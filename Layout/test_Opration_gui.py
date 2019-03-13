#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-02 16:54:15
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-10 16:28:59
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-02 16:54:15'

import sys
from PySide import QtGui
from Opration_gui import *
from File_Browser import *





app=QtGui.QApplication(sys.argv)
ex=Ui_Form()
windows=QtGui.QWidget()
ex.setupUi(windows)

Form=ex
#open button in line 1 bind to file browser and line edit 1
File_Browser1=Open_File_Browser(Form.lineEdit_filein_1)
Form.pushButton_openfile_1.clicked.connect(File_Browser1.opendialog)
#open button in line 2 bind to file browser and line edit 2
File_Browser2=Open_File_Browser(Form.lineEdit_filein_2)
Form.pushButton_openfile_2.clicked.connect(File_Browser2.opendialog)
#open button in line 3 bind to file browser and line edit 3
File_Browser3=Open_File_Browser(Form.lineEdit_filein_3)
Form.pushButton_openfile_3.clicked.connect(File_Browser3.opendialog)
Form.lineEdit_filein_3.setText("hello world")
print(Form.lineEdit_filein_3.text())
Form.lineEdit_filein_1.setValidator(QtGui.QIntValidator())

windows.show()
app.exec_()
