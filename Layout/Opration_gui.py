# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Opration_gui.ui'
#
# Created: Sun Mar 10 14:30:34 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(1100, 530)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1100, 530))
        Form.setMaximumSize(QtCore.QSize(1100, 530))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/.png/png/1208066.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 1041, 202))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_8.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setMinimumSize(QtCore.QSize(180, 30))
        self.label.setMaximumSize(QtCore.QSize(180, 30))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton_openfile_1 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_openfile_1.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_openfile_1.setMaximumSize(QtCore.QSize(90, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/.png/png/1208069.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openfile_1.setIcon(icon1)
        self.pushButton_openfile_1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_openfile_1.setCheckable(False)
        self.pushButton_openfile_1.setChecked(False)
        self.pushButton_openfile_1.setAutoRepeat(False)
        self.pushButton_openfile_1.setAutoExclusive(False)
        self.pushButton_openfile_1.setObjectName("pushButton_openfile_1")
        self.horizontalLayout_2.addWidget(self.pushButton_openfile_1)
        self.lineEdit_filein_1 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_filein_1.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_filein_1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_filein_1.setObjectName("lineEdit_filein_1")
        self.horizontalLayout_2.addWidget(self.lineEdit_filein_1)
        self.pushButton_exefile_1 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_exefile_1.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_exefile_1.setMaximumSize(QtCore.QSize(30, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/.png/png/1222647.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exefile_1.setIcon(icon2)
        self.pushButton_exefile_1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_exefile_1.setObjectName("pushButton_exefile_1")
        self.horizontalLayout_2.addWidget(self.pushButton_exefile_1)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(70, 30))
        self.label_2.setMaximumSize(QtCore.QSize(70, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_exestate_1 = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_exestate_1.setMaximumSize(QtCore.QSize(80, 30))
        self.textEdit_exestate_1.setUndoRedoEnabled(True)
        self.textEdit_exestate_1.setReadOnly(True)
        self.textEdit_exestate_1.setObjectName("textEdit_exestate_1")
        self.horizontalLayout_2.addWidget(self.textEdit_exestate_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(180, 30))
        self.label_3.setMaximumSize(QtCore.QSize(180, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_openfile_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_openfile_2.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_openfile_2.setMaximumSize(QtCore.QSize(90, 30))
        self.pushButton_openfile_2.setIcon(icon1)
        self.pushButton_openfile_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_openfile_2.setCheckable(False)
        self.pushButton_openfile_2.setChecked(False)
        self.pushButton_openfile_2.setAutoRepeat(False)
        self.pushButton_openfile_2.setAutoExclusive(False)
        self.pushButton_openfile_2.setObjectName("pushButton_openfile_2")
        self.horizontalLayout_3.addWidget(self.pushButton_openfile_2)
        self.lineEdit_filein_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_filein_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_filein_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_filein_2.setObjectName("lineEdit_filein_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_filein_2)
        self.pushButton_exefile_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_exefile_2.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_exefile_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_exefile_2.setIcon(icon2)
        self.pushButton_exefile_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_exefile_2.setObjectName("pushButton_exefile_2")
        self.horizontalLayout_3.addWidget(self.pushButton_exefile_2)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setMinimumSize(QtCore.QSize(70, 30))
        self.label_4.setMaximumSize(QtCore.QSize(70, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.textEdit_exestate_2 = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_exestate_2.setMaximumSize(QtCore.QSize(80, 30))
        self.textEdit_exestate_2.setUndoRedoEnabled(True)
        self.textEdit_exestate_2.setReadOnly(True)
        self.textEdit_exestate_2.setObjectName("textEdit_exestate_2")
        self.horizontalLayout_3.addWidget(self.textEdit_exestate_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setMinimumSize(QtCore.QSize(180, 30))
        self.label_7.setMaximumSize(QtCore.QSize(180, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.pushButton_openfile_3 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_openfile_3.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_openfile_3.setMaximumSize(QtCore.QSize(90, 30))
        self.pushButton_openfile_3.setIcon(icon1)
        self.pushButton_openfile_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_openfile_3.setCheckable(False)
        self.pushButton_openfile_3.setChecked(False)
        self.pushButton_openfile_3.setAutoRepeat(False)
        self.pushButton_openfile_3.setAutoExclusive(False)
        self.pushButton_openfile_3.setObjectName("pushButton_openfile_3")
        self.horizontalLayout_6.addWidget(self.pushButton_openfile_3)
        self.lineEdit_filein_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_filein_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_filein_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_filein_3.setObjectName("lineEdit_filein_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_filein_3)
        self.pushButton_exefile_3 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_exefile_3.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_exefile_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_exefile_3.setIcon(icon2)
        self.pushButton_exefile_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_exefile_3.setObjectName("pushButton_exefile_3")
        self.horizontalLayout_6.addWidget(self.pushButton_exefile_3)
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setMinimumSize(QtCore.QSize(70, 30))
        self.label_8.setMaximumSize(QtCore.QSize(70, 30))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.textEdit_exestate_3 = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_exestate_3.setMaximumSize(QtCore.QSize(80, 30))
        self.textEdit_exestate_3.setUndoRedoEnabled(True)
        self.textEdit_exestate_3.setReadOnly(True)
        self.textEdit_exestate_3.setObjectName("textEdit_exestate_3")
        self.horizontalLayout_6.addWidget(self.textEdit_exestate_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setMinimumSize(QtCore.QSize(180, 30))
        self.label_9.setMaximumSize(QtCore.QSize(180, 30))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.radioButton_config_op1 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_config_op1.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_config_op1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_config_op1.setObjectName("radioButton_config_op1")
        self.horizontalLayout_7.addWidget(self.radioButton_config_op1)
        self.radioButton_config_op2 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_config_op2.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_config_op2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_config_op2.setObjectName("radioButton_config_op2")
        self.horizontalLayout_7.addWidget(self.radioButton_config_op2)
        self.radioButton_config_op3 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_config_op3.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_config_op3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_config_op3.setObjectName("radioButton_config_op3")
        self.horizontalLayout_7.addWidget(self.radioButton_config_op3)
        self.radioButton_config_op4 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_config_op4.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_config_op4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_config_op4.setObjectName("radioButton_config_op4")
        self.horizontalLayout_7.addWidget(self.radioButton_config_op4)
        self.pushButton_algorithm_match = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_algorithm_match.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_algorithm_match.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_algorithm_match.setObjectName("pushButton_algorithm_match")
        self.horizontalLayout_7.addWidget(self.pushButton_algorithm_match)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.groupBox = QtGui.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 180))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 180))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_filein_msg = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_filein_msg.setGeometry(QtCore.QRect(0, 30, 300, 140))
        self.textBrowser_filein_msg.setMinimumSize(QtCore.QSize(300, 140))
        self.textBrowser_filein_msg.setMaximumSize(QtCore.QSize(300, 140))
        self.textBrowser_filein_msg.setObjectName("textBrowser_filein_msg")
        self.horizontalLayout_8.addWidget(self.groupBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 240, 1131, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 270, 1041, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setMinimumSize(QtCore.QSize(180, 30))
        self.label_10.setMaximumSize(QtCore.QSize(180, 30))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.radioButton_algorithm_1 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_algorithm_1.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_algorithm_1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_algorithm_1.setObjectName("radioButton_algorithm_1")
        self.horizontalLayout_9.addWidget(self.radioButton_algorithm_1)
        self.radioButton_algorithm_2 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_algorithm_2.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_algorithm_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_algorithm_2.setObjectName("radioButton_algorithm_2")
        self.horizontalLayout_9.addWidget(self.radioButton_algorithm_2)
        self.radioButton_algorithm_3 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_algorithm_3.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_algorithm_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.radioButton_algorithm_3.setObjectName("radioButton_algorithm_3")
        self.horizontalLayout_9.addWidget(self.radioButton_algorithm_3)
        self.pushButton_caculate = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_caculate.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_caculate.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_caculate.setObjectName("pushButton_caculate")
        self.horizontalLayout_9.addWidget(self.pushButton_caculate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setMinimumSize(QtCore.QSize(100, 30))
        self.label_11.setMaximumSize(QtCore.QSize(100, 30))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.textBrowser_algorithm_msg = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_algorithm_msg.setObjectName("textBrowser_algorithm_msg")
        self.verticalLayout_2.addWidget(self.textBrowser_algorithm_msg)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "基于拓扑映射的并行应用通信优化系统", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "应用进程拓扑数据文件输入", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_openfile_1.setText(QtGui.QApplication.translate("Form", "打开", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exefile_1.setText(QtGui.QApplication.translate("Form", "文件解析", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "解析状态：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "计算节点拓扑数据文件输入", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_openfile_2.setText(QtGui.QApplication.translate("Form", "打开", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exefile_2.setText(QtGui.QApplication.translate("Form", "文件解析", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "解析状态：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "配置数据文件输入", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_openfile_3.setText(QtGui.QApplication.translate("Form", "打开", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exefile_3.setText(QtGui.QApplication.translate("Form", "文件解析", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "解析状态：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "配置选项", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_config_op1.setText(QtGui.QApplication.translate("Form", "配置选项1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_config_op2.setText(QtGui.QApplication.translate("Form", "配置选项1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_config_op3.setText(QtGui.QApplication.translate("Form", "配置选项1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_config_op4.setText(QtGui.QApplication.translate("Form", "配置选项1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_algorithm_match.setText(QtGui.QApplication.translate("Form", "可用算法匹配", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "文件输入操作提示：", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_filein_msg.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件输入操作提示：</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "算法选择", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_algorithm_1.setText(QtGui.QApplication.translate("Form", "算法1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_algorithm_2.setText(QtGui.QApplication.translate("Form", "算法2", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_algorithm_3.setText(QtGui.QApplication.translate("Form", "算法3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_caculate.setText(QtGui.QApplication.translate("Form", "开始计算", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "算法概要：", None, QtGui.QApplication.UnicodeUTF8))

import sourcefile_rc
