from tkinter import *
import time
root  = Tk()
#Variables
score = IntVar()
score.set(0)
#Functions
def upgrade():
    global score  
    if score.get() > 99:
        score.set(score.get() +3 )
def upgrade1():
    global score 
    if score.get() > 49:
        score.set(score.get() + 2)

def update_score():
    global score 
    root.after(1)
    root.update()
    score.set(score.get() + 1)
def bad_autocliker():
    global score 
    if score.get() > 999:
        while True:
            root.update()
            root.after(100)
            root.update()
            score.set(score.get() + 1)
#Labels
welcome_screen = Label(root, text = "welcome to cheese clicker!!").grid(row = 0 , column = 3)
score_display = Label(root, text = "your score is below this line:").grid(row = 1,column = 3)
score_label = Label(root, textvariable = score).grid(row = 2, column = 3)
#Buttons
Cheese = Button(root, text = "tasty cheese", bg = "#ffa600", fg = "black", activebackground = "#ffa600", padx = 70 , pady= 65,command = update_score).grid(row = 3, column = 3)
Buy_upgrade_1 = Button(root, text = "american cheese", bg = "#f3af41", fg = "black", activebackground = "#f3af41", padx = 70 , pady = 65,command = upgrade1).grid(row = 3, column = 4)
blue_cheese = Button(root, text = "blue cheese" , bg = "blue", fg = "black", activebackground = "blue", padx = 70, pady = 65, command = upgrade).grid(row = 4, column = 3)
autoclicker = Button(root, text = "autoclicker" , bg = "green" , fg = "black", activebackground = "green" , command = bad_autocliker, padx = 87 ,pady = 65).grid(row = 4, column = 4)
root.mainloop()
