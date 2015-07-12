from PyQt4 import QtCore, QtGui, uic

form_final_class = uic.loadUiType("final_layout.ui")[0]

class MyFinalWindowClass(QtGui.QMainWindow, form_final_class):
	def __init__(self, parent=None):
		
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)

