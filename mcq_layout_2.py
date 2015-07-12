import sys
import random
from time import sleep
from PyQt4 import QtGui, QtCore, uic

from final_layout import MyFinalWindowClass

form_class = uic.loadUiType("mcq_layout_1.ui")[0]                 # Load the UI

#global variables...
credits = 100 #credits of participant
score = 0  #score updated for every que
ques_order=0 #random no generator algo will store it in this list
que_obj =0 #file object to open que file
index = 0 #index of the random ques_order array
flagDD = prev = 0 #for DoubleDip lifeline
level_select = 0 #to select in which level we should append! 
log_file_obj = open("LOG_FILE.txt","a")
log_file_sr = open("LOG_FILE_sr.txt",'a')

class MyWindowClass(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		
		self.etMinutes_3.setEnabled(False)
		self.etSeconds_3.setEnabled(False)
		self.etScore.setEnabled(False)
		self.etCredits.setEnabled(False)
		self.etOption1.setEnabled(False)
		self.etOption2.setEnabled(False)
		self.etOption3.setEnabled(False)
		self.etOption4.setEnabled(False)
		
		self.etQuestion.setReadOnly(True)
		#self.etQuestion.setDisabled(True)
		
		self.bSubmit.clicked.connect(self.bSubmit_clicked)
		self.bPtoc.clicked.connect(self.bPtoc_clicked)
		self.bDoubledip.clicked.connect(self.bDoubledip_clicked)
		self.bJack.clicked.connect(self.bJack_clicked)
		self.bFinish.clicked.connect(self.bFinish_clicked)
		
		self.bSubmit.setStyleSheet("background-color: palegreen")
		self.bFinish.setStyleSheet("background-color: tomato")
		self.bDoubledip.setStyleSheet("background-color: aqua")
		self.bPtoc.setStyleSheet("background-color: aqua")
		self.bJack.setStyleSheet("background-color: aqua")
		
		self.etQuestion.setStyleSheet("background-color: lightblue")
		#self.etQuestion.setStyleSheet("border: 0px ")
		
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update_timer)
		self.timer.start(1000)
		self.minute_count = 19
		self.second_count = 59
				
		global ques_order
		global que_obj
		ques_order = random.sample(range(1,83),82)
		print ques_order
		#self.bDoubledip.clicked.connect(self.bDoubledip_clicked)

	def update_timer(self):
		#time_color = 0
		self.second_count -= 1
		#self.etMinutes_3.setText(str(self.minute_count))
		self.etMinutes_3.setText("<font style='color: black;'>" + str(self.minute_count)+"</font>")
		
		
		if self.second_count <= 0:
			self.minute_count -= 1
			self.second_count = 59
				
		if self.minute_count == -1:
			self.minute_count = -2
			self.finish_program()
					
		if self.minute_count <= 4 and self.minute_count > 1 and self.second_count >= 0:
			self.etSeconds_3.setText("<font style='color: orange;'>" + str(self.second_count)+"</font>")
			self.etMinutes_3.setText("<font style='color: orange;'>" + str(self.minute_count)+"</font>")		
			#time_color = 1
		elif self.minute_count <= 1 and self.second_count >= 0:
			self.etSeconds_3.setText("<font style='color: red;'>" + str(self.second_count)+"</font>")
			self.etMinutes_3.setText("<font style='color: red;'>" + str(self.minute_count)+"</font>")		
			#time_color = 1
		else:
			self.etSeconds_3.setText("<font style='color: black;'>" + str(self.second_count)+"</font>")
			self.etMinutes_3.setText("<font style='color: black;'>" + str(self.minute_count)+"</font>")
		
	
	def bFinish_clicked(self):
		self.finish_program()
		
	
	def finish_program(self):
		global score
		global credits
		self.close()
		self.FT2 = MyFinalWindowClass()
		self.FT2.showMaximized()
		self.FT2.etScoreobtained.setText(str(score))
		self.FT2.etCreditsremaining.setText(str(credits))
		self.FT2.etFinalscore.setText(str(score + credits/10))
		if level_select == "Junior":
			log_file_obj.write("\nScore: " + str(score + credits/10))
			log_file_obj.write("\n------------------------------------------------------")
			log_file_obj.close()				
		elif level_select == "Senior":
			log_file_sr.write("\nScore: " + str(score + credits/10))
			log_file_sr.write("\n------------------------------------------------------")
			log_file_sr.close()
		#put final score in DB(file) for record..!
		
	def read_ques(self,splChar, level):
		global index
		global que_obj
		global level_select
		level_select = level
	 	que_obj = open(str(ques_order[index]),"r")
	 	prev = index
	 	index = index+1
	 	st = ""
	 	while 1:
	 		ch = que_obj.read(1)
	 		if ch==splChar : break
	 		st = st+ch
	 	self.etQuestion.clear()
	 	#self.etQuestion.append(st)
	 	self.etQuestion.setText(st)
	 	#self.etQuestion.setText(st)
	 	
	 	for i in range(0,4):
	 		st1 = ""
	 		#optionName = "etOption" + str(i+1)
	 		while 1:
	 			ch = que_obj.read(1)
	 			if ch==splChar : break
	 			st1 = st1 + ch
	 		if i==0:
	 			self.etOption1.setText("<font style='color: black;'>" + st1 +"</font>")
	 		elif i==1:
	 			#self.etOption2.append(st1)
	 			self.etOption2.setText("<font style='color: black;'>" + st1 +"</font>")
	 		elif i==2:
	 			#self.etOption3.append(st1)
	 			self.etOption3.setText("<font style='color: black;'>" + st1 +"</font>")
	 		elif i==3:
	 			#self.etOption4.append(st1)
	 			self.etOption4.setText("<font style='color: black;'>" + st1 +"</font>")
	
	#starting of check function...
	def check(self):
		if self.a.isChecked():
			return 1
		if self.b.isChecked():
			return 2
		if self.c.isChecked():
			return 3
		if self.d.isChecked():
			return 4
		return 0
		

	def load_next_que(self):
		print "In load_next_que"
		global index
		global level_select
		print ques_order[index]
		level = level_select
		#que_obj = open(str(ques_order[index]),"r")
		#self.a.setCheckable(True)
		self.read_ques('$',level)


	def bSubmit_clicked(self):
		global flagDD
		global index
		given_ans = self.check()
		if given_ans == 0:
			print 'select ans'
		else:
			correct_ans = (int)(que_obj.read(1))		
			print correct_ans 
			print given_ans
			if given_ans == correct_ans:
				global score 
				if(flagDD == 1):
					index = index + 1
				score = score + 4
				#score color...
				if score <= 10:	
					self.etScore.setText("<font style='color: red;'>" + str(score) +"</font>")
				elif score > 10 and score <= 30:	
					self.etScore.setText("<font style='color: orange;'>" + str(score) +"</font>")
				else:
					self.etScore.setText("<font style='color: green;'>" + str(score) +"</font>")
			else:
				global credits 
				credits = credits - 10
				
				if(credits==0):
					self.bSubmit.setEnabled(False)
					self.bSubmit.setStyleSheet("background-color: none")
				
				#credit color...
				if credits >= 50:	
					self.etCredits.setText("<font style='color: green;'>" + str(credits) +"</font>")
				elif credits < 50 and credits >= 20:	
					self.etCredits.setText("<font style='color: orange;'>" + str(credits) +"</font>")
				else:
					self.etCredits.setText("<font style='color: red;'>" + str(credits) +"</font>")
				
							
			que_obj.close()
			
			if(flagDD == 1):
				flagDD = 0
				index = index - 1
			
			#if questions finishes...
			if index == 79:
				self.finish_program()
			else:	
				self.load_next_que()
			

	def bPtoc_clicked(self):
		global score
		global credits
		score = score - 4
		credits = credits + 10
		self.bSubmit.setStyleSheet("background-color: palegreen")
		self.bSubmit.setEnabled(True)
		#self.etScore.setText("<font style='color: black;'>" + str(score) +"</font>")
		if score <= 10:	
			self.etScore.setText("<font style='color: red;'>" + str(score) +"</font>")
		elif score > 10 and score <= 30:	
			self.etScore.setText("<font style='color: orange;'>" + str(score) +"</font>")
		else:
			self.etScore.setText("<font style='color: green;'>" + str(score) +"</font>")
		
		#self.etCredits.setText("<font style='color: black;'>" + str(credits) +"</font>")
		if credits >= 50:	
			self.etCredits.setText("<font style='color: green;'>" + str(credits) +"</font>")
		elif credits < 50 and credits >= 20:	
			self.etCredits.setText("<font style='color: orange;'>" + str(credits) +"</font>")
		else:
			self.etCredits.setText("<font style='color: red;'>" + str(credits) +"</font>")
	
	
	def bDoubledip_clicked(self):
		global flagDD
		flagDD = 1				
		self.bDoubledip.setEnabled(False)					
		self.bDoubledip.setStyleSheet("background-color: none")
	
	def bJack_clicked(self):
		global score
		global index
		score = score + 4
		#self.etScore.setText("<font style='color: black;'>" + str(score) +"</font>")
		if score <= 10:	
			self.etScore.setText("<font style='color: red;'>" + str(score) +"</font>")
		elif score > 10 and score <= 30:	
			self.etScore.setText("<font style='color: orange;'>" + str(score) +"</font>")
		else:
			self.etScore.setText("<font style='color: green;'>" + str(score) +"</font>")
		
		self.bJack.setEnabled(False)
		self.bJack.setStyleSheet("background-color: none")
		self.load_next_que()

'''
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.read_ques('$')
myWindow.show()
app.exec_()
'''
