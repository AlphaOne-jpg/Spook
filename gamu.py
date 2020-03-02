from tkinter import *
from tkinter import messagebox
import time
from gameevents import gameevents
import random

GeometryX = 350
GeometryY = 200

items = ["First","Second","Third"]
health = "Healthy"
tags = ["Human"]
stats = {'Strength': 2, 'Dexterity': 2, 'Constitution': 2, 'Charisma': 2, 'Recursos': 1, 'Daycount': 1}

#gamewindows
statwindow = None
itemwindow = None

#main window
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry(str(GeometryX)+'x'+str(GeometryY))

#label
lbl = Label(window, text="Hello,thanks for comming",font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

#Stats
def clicked1():
	global statwindow
	global stats
	global window
	print(statwindow)
	if statwindow is None:
		statwindow = Toplevel(window)
		statwindow.grab_set()
		statwindow.title("Stats")
		statwindow.geometry('200x'+str(len(stats)*30))
		draw = []
		i = 0
		for elem in stats:
			draw.append(Label(statwindow,text=str(elem)+":    "+str(stats[elem]),font=("Arial Bold", 15)))
			draw[i].grid(column=0, row=i)
			i+=1
btn1 = Button(window, text="Stats",command=clicked1)
btn1.grid(column=0, row=2)

#Inventory button
def clicked2():
	global items
	global window
	if len(items) == 0:
		messagebox.showinfo('!!!', 'Empty inventory')
	else:
		window2 = Toplevel(window)
		window2.grab_set()
		window2.title("Inventory")
		window2.geometry('300x'+str(len(items)*30))
		draw = []
		btns = []
		for i in range(0,len(items)):
			def clickeduse(someNumber):
				res = messagebox.askquestion('Used', 'Used: '+str(items[someNumber]))
				print(res)
				if res == "yes":
					print("it was yes")
					items.remove(items[someNumber])
				window2.destroy()
			draw.append(Label(window2,text=items[i],font=("Arial Bold", 15)))
			btns.append(Button(window2, text="Use",command= lambda j=i: clickeduse(j)))
			draw[i].grid(column=0, row=i)
			btns[i].grid(column=1, row=i)
	
btn2 = Button(window, text="Inventory",command=clicked2)
btn2.grid(column=0, row=3)



#Work Button
def clicked3():
	global stats
	global statwindow
	res = messagebox.askquestion('Work', 'You can spend another mundain day working...')
	if res == "yes":
		stats['Recursos']+=1
	statwindow.update()
	
	dayloop()
btn3 = Button(window, text="Work",command=clicked3)
btn3.grid(column=0, row=4)

#Do Nothing
def clicked4():
	global stats
	res = messagebox.askquestion('Do nothing', 'You want to do nothing for the day')
	if res == "yes":
		dayloop()
	
btn4 = Button(window, text="Do nothing",command=clicked4)
btn4.grid(column=0, row=5)

#Event button
def clicked5():
	global stats
	global window
	btns = []
	eventwindow = Toplevel(window)
	eventwindow.grab_set()
	event = gameevents("TagTest")
	eventwindow.title(event.name)
	lbl = Label(eventwindow, text=event.description,font=("Arial Bold", 20))
	lbl.grid(column=0, row=0)
	selected = -1
	def clickedevent(someNumber):
		selected = someNumber
		print(selected)
	for i in range(0,len(event.options)):
		btns.append(Button(eventwindow, text=event.options[i],command= lambda j=i: clickedevent(j)))
		btns[i].grid(column=0, row=i+30)
	print(btns)
	
btn5 = Button(window, text="Test Event",command=clicked5)
btn5.grid(column=0, row=6)

#mainloop
def dayloop():
	global stats
	if(stats['Recursos'] > 2):
		messagebox.showinfo("!!!","You got attacked on your way home and lost all your money")
		stats['Recursos'] = 0
	stats['Daycount'] += 1


#tag methods
def hasTag(tag):
	global tags
	for elem in tags:
		if elem == tag:
			return true
	return false

#Roll methods
def regularRoll(caracteristic, difficulty):
	global stats
	successes = 0
	for i in range (1,stats[caracteristic]):
		roll = random.randint(1,10)
		if roll == 10:
			successes += 2
		elif roll >= difficulty:
			successes += 1
		elif roll == 1:
			successes -= 1
	
	return successes


#loop
window.mainloop()