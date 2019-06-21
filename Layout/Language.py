#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-17 17:13:49
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-06-21 11:45:27
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-17 17:13:49'

from PyQt4 import QtGui
def QTLanguageTranslate(chinesestr):
	return QtGui.QApplication.translate("Form", chinesestr, None, QtGui.QApplication.UnicodeUTF8)

def QTtextBrowserTranslate(chinesestr):
	htmlstr='''
<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">
'''+chinesestr+'''
</p></body></html>
'''
	return htmlstr

STR_TOTAL_TASK_NUM=QTLanguageTranslate("task总数:")
STR_CACULATE_FAILD=QTLanguageTranslate("算法计算失败，请检查输入文件以及配置数据是否正确！")

STR_RESULT_MAP=QTLanguageTranslate("任务序号\t节点序号")
STR_RESULT_DATA=QTLanguageTranslate("\'*\' 代表空闲 <节点序号>:<任务序号>")

STR_CACULATER_CHINESE="算法："
STR_TASK_NUMBER_CHINESE="任务数："
STR_CORE_NUMBER_CHINESE="核心数："
STR_CACULATER_TIME_CHINESE="算法运行时间（ms）："

STR_FILE_INPUT_INFOMATION='''
<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">TopoMapping输入：</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">    .TOPO / .APHiD</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">    .txt</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">MPIPP输入：</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">    .mat / .MPIPP</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">    .tgt / .txt</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">TreeMatch输入：</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">    .mat</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">    .tgt</span></p></body></html>
'''
STR_FILE_INPUT_INFOMATION=QTLanguageTranslate(STR_FILE_INPUT_INFOMATION)


STR_CONFIGWINDOW_TITLE_NET=QTLanguageTranslate("网络拓扑配置信息")
STR_CONFIGWINDOW_TITLE_TASK=QTLanguageTranslate("通信拓扑配置信息")
STR_CONFIGWINDOW_TITLE_BIND=QTLanguageTranslate("绑定文件配置信息")