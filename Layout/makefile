all : Opration_gui.py sourcefile_rc.py MsgBox_gui.py ConfigBox_gui.py Graph_gui.py ResultBox_gui.py

Opration_gui.py : Opration_gui.ui
	pyuic4 -o Opration_gui.py Opration_gui.ui
sourcefile_rc.py : sourcefile.qrc
	pyrcc4 -o sourcefile_rc.py sourcefile.qrc
MsgBox_gui.py : MsgBox_gui.ui 
	pyuic4 -o MsgBox_gui.py MsgBox_gui.ui
ConfigBox_gui.py : ConfigBox_gui.ui
	pyuic4 -o ConfigBox_gui.py ConfigBox_gui.ui
Graph_gui.py : Graph_gui.ui
	pyuic4 -o Graph_gui.py Graph_gui.ui
ResultBox_gui.py : ResultBox_gui.ui
	pyuic4 -o ResultBox_gui.py ResultBox_gui.ui


.PHONY : clean
clean : 
	rm -rf *.pyc