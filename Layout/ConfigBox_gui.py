# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigBox_gui.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(300, 400)
        Form.setMinimumSize(QtCore.QSize(300, 400))
        Form.setMaximumSize(QtCore.QSize(300, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/.png/png/1208066.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 391))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label_cf_1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_cf_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_cf_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cf_1.setObjectName(_fromUtf8("label_cf_1"))
        self.gridLayout.addWidget(self.label_cf_1, 0, 1, 1, 1)
        self.lineEdit_in_1 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_in_1.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_in_1.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_in_1.setObjectName(_fromUtf8("lineEdit_in_1"))
        self.gridLayout.addWidget(self.lineEdit_in_1, 0, 2, 1, 1)
        self.label_cf_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_cf_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cf_5.setObjectName(_fromUtf8("label_cf_5"))
        self.gridLayout.addWidget(self.label_cf_5, 4, 1, 1, 1)
        self.label_cf_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_cf_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cf_3.setObjectName(_fromUtf8("label_cf_3"))
        self.gridLayout.addWidget(self.label_cf_3, 2, 1, 1, 1)
        self.label_cf_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_cf_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cf_2.setObjectName(_fromUtf8("label_cf_2"))
        self.gridLayout.addWidget(self.label_cf_2, 1, 1, 1, 1)
        self.lineEdit_in_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_in_2.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_in_2.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_in_2.setObjectName(_fromUtf8("lineEdit_in_2"))
        self.gridLayout.addWidget(self.lineEdit_in_2, 1, 2, 1, 1)
        self.lineEdit_in_3 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_in_3.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_in_3.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_in_3.setObjectName(_fromUtf8("lineEdit_in_3"))
        self.gridLayout.addWidget(self.lineEdit_in_3, 2, 2, 1, 1)
        self.label_cf_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_cf_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cf_4.setObjectName(_fromUtf8("label_cf_4"))
        self.gridLayout.addWidget(self.label_cf_4, 3, 1, 1, 1)
        self.lineEdit_in_4 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_in_4.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_in_4.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_in_4.setObjectName(_fromUtf8("lineEdit_in_4"))
        self.gridLayout.addWidget(self.lineEdit_in_4, 3, 2, 1, 1)
        self.lineEdit_in_5 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_in_5.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_in_5.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_in_5.setObjectName(_fromUtf8("lineEdit_in_5"))
        self.gridLayout.addWidget(self.lineEdit_in_5, 4, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.pushButton_cancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton_cancel)
        self.pushButton_ensure = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_ensure.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_ensure.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButton_ensure.setObjectName(_fromUtf8("pushButton_ensure"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.pushButton_ensure)
        self.verticalLayout.addLayout(self.formLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "网络拓扑配置信息", None))
        self.label_cf_1.setText(_translate("Form", "Core总个数:", None))
        self.label_cf_5.setText(_translate("Form", "option2", None))
        self.label_cf_3.setText(_translate("Form", "单节点Core个数:", None))
        self.label_cf_2.setText(_translate("Form", "Node总个数:", None))
        self.label_cf_4.setText(_translate("Form", "option1", None))
        self.pushButton_cancel.setText(_translate("Form", "取消", None))
        self.pushButton_ensure.setText(_translate("Form", "确定", None))

import sourcefile_rc
