all : Layout_make MPIPP_make

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
srcdir := $(dir $(mkfile_path))

PyQt_package_link := https://jaist.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-4.12.3/PyQt4_gpl_x11-4.12.3.tar.gz
PyQt_package := PyQt4_gpl_x11-4.12.3.tar.gz

Layout_make : 
	$(MAKE) -C $(srcdir)Layout/

MPIPP_make :
	$(MAKE) -C $(srcdir)Algorithm/MapMPIPP/

.PHONY : install
install :
	sudo apt-get update
	sudo apt-get install qt4-dev-tools qt4-doc qt4-qtconfig qt4-demos qt4-designer libqwt5-qt4 libqwt5-qt4-dev
	sudo pip2 install -r requirements.txt
	mkdir $(srcdir)install
	cd $(srcdir)install
	curl -o $(srcdir)install/$(PyQt_package) $(PyQt_package_link)
	tar -xzf $(PyQt_package)
	cd PyQt4_gpl_x11-4.12.3
	sudo python configure.py 
	sudo $(MAKE) -C $(srcdir)install/PyQt4_gpl_x11-4.12.3/
	sudo $(MAKE) -C $(srcdir)install/PyQt4_gpl_x11-4.12.3/ install
	cd $(srcdir)
	rm -rd install