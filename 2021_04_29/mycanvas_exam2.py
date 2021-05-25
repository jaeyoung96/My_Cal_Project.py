import tkinter
import time
mywin = tkinter.Tk()
cvs = tkinter.Canvas(mywin, width=600, height = 400)
cvs.pack()
x = 100
y = 100
img = tkinter.PhotoImage(file = "beachball.png")
ball1 = cvs.create_image(x,y, image = img)

for x in range(0,60):
	cvs.move(ball1, 7 ,3)
	mywin.update()
	time.sleep(0.01)

mywin.mainloop()
