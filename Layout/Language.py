#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-17 17:13:49
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-04-14 17:03:43
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-17 17:13:49'

from PySide import QtGui
def QTLanguageTranslate(chinesestr):
	return QtGui.QApplication.translate("Form", chinesestr, None, QtGui.QApplication.UnicodeUTF8)

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


STR_TOPOMAPPING_INFOMATION='''
<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TopoMapping进行拓扑映射的思路是首先对任务图进行分析，使用CommProfiler对任务图进行分析并得出任务图通信信息，并使用脚本生成最优的任务通信图作为ParMapper算法的输入，然后根据不同的输入配置要求，生成多个初始输入配置文件，再根据各个不同的配置文件，使用基于贪心的GreedyMap算法，并行计算各个配置条件下的最优映射方案，最后通过统一的量化标准，比较每个配置下生成的最优映射方案，得到全局最优映射方案作为算法的输出方案</p></body></html>
'''
STR_TOPOMAPPING_INFOMATION=QTLanguageTranslate(STR_TOPOMAPPING_INFOMATION)
