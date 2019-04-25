# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultBox_gui.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(840, 600)
        Dialog.setMinimumSize(QtCore.QSize(840, 600))
        Dialog.setMaximumSize(QtCore.QSize(840, 600))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 810, 480))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.listWidget = QtGui.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 810, 451))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 510, 811, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_algorithm = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_algorithm.setObjectName(_fromUtf8("label_algorithm"))
        self.horizontalLayout.addWidget(self.label_algorithm)
        self.label_1 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.horizontalLayout.addWidget(self.label_1)
        self.label_tasknum = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_tasknum.setObjectName(_fromUtf8("label_tasknum"))
        self.horizontalLayout.addWidget(self.label_tasknum)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_corenum = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_corenum.setObjectName(_fromUtf8("label_corenum"))
        self.horizontalLayout.addWidget(self.label_corenum)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.label_caculatetime = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_caculatetime.setObjectName(_fromUtf8("label_caculatetime"))
        self.horizontalLayout.addWidget(self.label_caculatetime)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "结果展示", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "图形", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "任务序号\\t节点序号", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "数字", None))
        self.label_2.setText(_translate("Dialog", "算法：", None))
        self.label_algorithm.setText(_translate("Dialog", "TopoMapping", None))
        self.label_1.setText(_translate("Dialog", "任务数：", None))
        self.label_tasknum.setText(_translate("Dialog", "128", None))
        self.label_3.setText(_translate("Dialog", "核心数：", None))
        self.label_corenum.setText(_translate("Dialog", "128", None))
        self.label_4.setText(_translate("Dialog", "算法运行时间（ms）：", None))
        self.label_caculatetime.setText(_translate("Dialog", "33355.35", None))

