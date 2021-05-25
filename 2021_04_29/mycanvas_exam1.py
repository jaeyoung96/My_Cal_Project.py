import tkinter
import random

def randxy():
	a = random.randint(1,250)
	return a

def click():
	cvs.create_line(randxy(), randxy(), randxy(), randxy())

def delpic():
    cvs.delete('all')   # 캔버스에 그려진 모든 그림 지우기
    #cvs.create_window(150, 200, window=button)
    #cvs.create_window(100,200, window=delbutton)

mywin = tkinter.Tk()
frame = tkinter.Frame(mywin)
cvs = tkinter.Canvas(mywin, width=250, height = 250)
cvs.pack()

button = tkinter.Button(frame, text = "click", command = click)
button.pack()
#cvs.create_window(150,200, window = button)

delbutton = tkinter.Button(frame, text = "clear", command = delpic)
delbutton.pack()
#cvs.create_window(100,200, window=delbutton)

mywin.mainloop()
