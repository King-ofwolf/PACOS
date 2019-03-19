#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kingofwolf
# @Date:   2019-03-17 10:59:54
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-17 14:39:13
# @Email:	wangshenglingQQ@163.com
'Info: a Python file '
__author__ = 'Wang'
__version__= '2019-03-17 10:59:54'

import logging
import os

SYSWORD_DIR=os.getcwd()
RUNLOG_DIR=os.path.join(SYSWORD_DIR,"debug_log/")
LOG_FILE=os.path.join(RUNLOG_DIR,"System.log")
logging.basicConfig(level=logging.INFO,
					format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename=LOG_FILE,
					filemode='w')
Sys_logger=logging.getLogger("System")

