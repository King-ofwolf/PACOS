all : Opration_gui.py sourcefile_rc.py MsgBox_gui.py ConfigBox_gui.py

Opration_gui.py : Opration_gui.ui
	pyside-uic -o Opration_gui.py Opration_gui.ui
sourcefile_rc.py : sourcefile.qrc
	pyrcc4 -o sourcefile_rc.py sourcefile.qrc
MsgBox_gui.py : MsgBox_gui.ui 
	pyside-uic -o MsgBox_gui.py MsgBox_gui.ui
ConfigBox_gui.py : ConfigBox_gui.ui
	pyside-uic -o ConfigBox_gui.py ConfigBox_gui.ui

.PHONY : clean
clean : 
	rm -rf *.pyc