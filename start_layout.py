import os
import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *

#from Ui_start_layout import form_class
from mcq_layout_2 import MyWindowClass

log_file_obj = open("LOG_FILE.txt",'a')
log_file_sr = open("LOG_FILE_sr.txt",'a')

form_start_class = uic.loadUiType("start_layout.ui")[0]

'''
class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)
'''

class MyStartWindowClass(QtGui.QMainWindow, form_start_class):
	def __init__(self, parent=None):
		
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		#self.showFullScreen()
		self.showMaximized()
		self.bStart.clicked.connect(self.bStart_clicked)
		self.bStart.setStyleSheet("background-color: greenyellow")
		#self.setStyleSheet("background-image: url(share.jgp)")
		#get info from user to store in DB(file)...
	
	
	def bStart_clicked(self):
		if self.leRecieptno.text()=="" or self.leUsername.text()=="" or self.leName.text()=="" or self.leCollege.text()=="" or self.leContact.text()=="" or self.leEmailid.text()=="" or self.cbLevel.currentText()=="select level" :
			print 'empty filed!'
		else:
			print self.cbLevel.currentText()
			if self.cbLevel.currentText() == "Junior":
			
				log_file_obj.write("\nReciept No.: " + self.leRecieptno.text())
				log_file_obj.write("\nUsername: " + self.leUsername.text())
				log_file_obj.write("\nName: " + self.leName.text())
				log_file_obj.write("\nCollege: " + self.leCollege.text())
				log_file_obj.write("\nContact: " + self.leContact.text())
				log_file_obj.write("\nEmail ID: " + self.leEmailid.text())
				#log_file_obj.write("\n------------------------------------------------------")
				log_file_obj.close()				
		
			elif self.cbLevel.currentText() == "Senior":
			
				log_file_sr.write("\nReciept No.: " + self.leRecieptno.text())
				log_file_sr.write("\nUsername: " + self.leUsername.text())
				log_file_sr.write("\nName: " + self.leName.text())
				log_file_sr.write("\nCollege: " + self.leCollege.text())
				log_file_sr.write("\nContact: " + self.leContact.text())
				log_file_sr.write("\nEmail ID: " + self.leEmailid.text())
				#log_file_obj.write("\n------------------------------------------------------")
				log_file_sr.close()
			
			self.FT = MyWindowClass()
			self.FT.showMaximized()
			self.FT.etSeconds_3.setText("<font style='color: black;'>59</font>")
			self.FT.etMinutes_3.setText("<font style='color: black;'>19/font>")
			self.FT.etScore.setText("<font style='color: red;'>0</font>")
			self.FT.etCredits.setText("<font style='color: green;'>100</font>")
			#self.FT.time_display()
			self.FT.read_ques('$',self.cbLevel.currentText())
			self.close()
			#QtCore.QCoreApplication.instance().hide()
			#self.destroy()
	

app = QtGui.QApplication(sys.argv)
myStartWindow = MyStartWindowClass(None)

'''
palette = QPalette()
palette.setBrush(QPalette.Background,QBrush(QPixmap("share.jpg")))
myStartWindow.setPalette(palette)
'''

myStartWindow.show()
app.exec_()
