# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1120, 530)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 530))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 530))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_main = QtGui.QMenu(self.menubar)
        self.menu_main.setObjectName(_fromUtf8("menu_main"))
        self.menuOption = QtGui.QMenu(self.menu_main)
        self.menuOption.setObjectName(_fromUtf8("menuOption"))
        self.menu_example = QtGui.QMenu(self.menubar)
        self.menu_example.setObjectName(_fromUtf8("menu_example"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSuboption = QtGui.QAction(MainWindow)
        self.actionSuboption.setObjectName(_fromUtf8("actionSuboption"))
        self.menuOption.addAction(self.actionSuboption)
        self.menu_main.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menu_main.menuAction())
        self.menubar.addAction(self.menu_example.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "基于拓扑映射的并行应用通信优化系统", None))
        self.menu_main.setTitle(_translate("MainWindow", "菜单", None))
        self.menuOption.setTitle(_translate("MainWindow", "option", None))
        self.menu_example.setTitle(_translate("MainWindow", "样例", None))
        self.actionSuboption.setText(_translate("MainWindow", "suboption", None))

