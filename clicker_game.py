from tkinter import *
import time
root  = Tk()
#Variables
score = IntVar()
score.set(0)
#Functions
def upgrade():
	global score  
	if score.get() > 100:
		score.set(score.get() +3 )
def upgrade1():
	global score 
	if score.get() > 50:
		score.set(score.get() + 2)

def update_score():
	global score 
	root.after(1)
	root.update()
	score.set(score.get() + 1)
def bad_autocliker():
	global score 
	if score.get() > 1000:
		while True:
			root.update()
			root.after(100)
			root.update()
			score.set(score.get() + 1)
#Labels
welcome_screen = Label(root, text = "welcome to cheese clicker!!").pack()
score_display = Label(root, text = "your score is below this line:").pack()
score_label = Label(root, textvariable = score).pack()
#Buttons
Cheese = Button(root, text = "tasty cheese", bg = "#ffa600", fg = "black", activebackground = "#ffa600", padx = 55 , pady= 55,command = update_score).pack()
Buy_upgrade_1 = Button(root, text = "american cheese", bg = "#f3af41", fg = "black", activebackground = "#f3af41", padx = 50 , pady = 50,command = upgrade1).pack()
blue_cheese = Button(root, text = "blue cheese" , bg = "blue", fg = "black", activebackground = "blue", padx = 50, pady = 50, command = upgrade).pack()
autoclicker = Button(root, text = "autoclicker" , bg = "green" , fg = "black", activebackground = "green" , command = bad_autocliker).pack()
root.mainloop()
