Opration_gui.py : Opration_gui.ui
	pyside-uic -o Opration_gui.py Opration_gui.ui
sourcefile_rc.py : sourcefile.qrc
	pyrcc4 -o sourcefile_rc.py sourcefile.qrc

.PHONY : clean
clean : 
	rm -rf *.pyc