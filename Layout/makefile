all : Opration_gui.py sourcefile_rc.py MsgBox_gui.py Config_Box.py

Opration_gui.py : Opration_gui.ui
	pyside-uic -o Opration_gui.py Opration_gui.ui
sourcefile_rc.py : sourcefile.qrc
	pyrcc4 -o sourcefile_rc.py sourcefile.qrc
MsgBox_gui.py : MsgBox_gui.ui 
	pyside-uic -o MsgBox_gui.py MsgBox_gui.ui
Config_Box.py : Config_Box.ui
	pyside-uic -o Config_Box.py Config_Box.ui

.PHONY : clean
clean : 
	rm -rf *.pyc