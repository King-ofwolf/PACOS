all : Layout_make MPIPP_make Log_file

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
srcdir := $(dir $(mkfile_path))

PyQt_package_link := https://jaist.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-4.12.3/PyQt4_gpl_x11-4.12.3.tar.gz
PyQt_package := PyQt4_gpl_x11-4.12.3.tar.gz

Log_file : 
	mkdir $(srcdir)debug_log
	
Layout_make : 
	$(MAKE) -C $(srcdir)Layout/

MPIPP_make :
	$(MAKE) -C $(srcdir)Algorithm/MapMPIPP/

.PHONY : install
install :
	sudo apt-get update
	sudo apt-get install qt4-dev-tools qt4-doc qt4-qtconfig qt4-demos qt4-designer libqwt5-qt4 libqwt5-qt4-dev libxext6 libxext-dev libqt4-dev libqt4-sql python-qt4 python-qt4-* python-qscintilla2 
	sudo pip2 install -r requirements.txt
