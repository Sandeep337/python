from tkinter import *
import os

win = Tk()
win.title = "Shut Down and Restart"
win.geometry("140x120")
 
def shutdown():
	os.system("shutdown /s /t 1")
	
def restart():
	os.system("shutdown /r /t 1")
	
btn1 = Button(win, text="Shutdown", command=shutdown, height=3, width=17)
btn1.grid(row=0, column=0)

btn2 = Button(win, text="Restart", command=restart, height=3, width=17)
btn2.grid(row=1, column=0)

win.mainloop()