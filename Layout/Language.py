#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-17 17:13:49
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-17 19:25:18
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-17 17:13:49'

from PySide import QtGui
def QTLanguageTranslate(chinesestr):
	return QtGui.QApplication.translate("Form", chinesestr, None, QtGui.QApplication.UnicodeUTF8)

STR_TOTAL_TASK_NUM=QTLanguageTranslate("task总数:")
STR_CACULATE_FAILD=QTLanguageTranslate("算法计算失败，请检查输入文件以及配置数据是否正确！")