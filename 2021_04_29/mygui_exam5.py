import tkinter
from tkinter import messagebox
def InputNum():
    sum1.set(sum1.get())

def InputBtn():
    pass


mywin = tkinter.Tk()
mywin.title('계산기')
mywin.geometry('350x350')

frame_up = tkinter.Frame(mywin,height = 100,width = 350,background = 'blue')
frame_up.pack()
frame1 = tkinter.Frame(mywin, height = 200, width = 350)
frame1.pack()

sum1 = tkinter.IntVar(value=0)
#label1 = tkinter.Label(frame_up, text = '계산식을 입력하세요',textvariable = sum1)
#label1.pack()
button1 = tkinter.Button(frame1, text = '1', command = InputNum, padx=20, pady=10)
button1.grid(row=1, column=0, padx = 10, pady = 10)
button2 = tkinter.Button(frame1, text = '2', command = InputNum, padx=20, pady=10)
button2.grid(row=1, column=1, padx = 10, pady = 10)
button3 = tkinter.Button(frame1, text = '3', command = InputNum, padx=20, pady=10)
button3.grid(row=1, column=2, padx = 10, pady = 10)
button4 = tkinter.Button(frame1, text = '4', command = InputNum, padx=20, pady=10)
button4.grid(row=2, column=0, padx = 10, pady = 10)
button5 = tkinter.Button(frame1, text = '5', command = InputNum, padx=20, pady=10)
button5.grid(row=2, column=1, padx = 10, pady = 10)
button6 = tkinter.Button(frame1, text = '6', command = InputNum, padx=20, pady=10)
button6.grid(row=2, column=2, padx = 10, pady = 10)
button7 = tkinter.Button(frame1, text = '7', command = InputNum, padx=20, pady=10)
button7.grid(row=3, column=0, padx = 10, pady = 10)
button8 = tkinter.Button(frame1, text = '8', command = InputNum, padx=20, pady=10)
button8.grid(row=3, column=1, padx = 10, pady = 10)
button9 = tkinter.Button(frame1, text = '9', command = InputNum, padx=20, pady=10)
button9.grid(row=3, column=2, padx = 10, pady = 10)
button0 = tkinter.Button(frame1, text = '0', command = InputNum, padx=20, pady=10)
button0.grid(row=4, column=1, padx = 10, pady = 10)

buttonC = tkinter.Button(frame1, text = 'C', command = InputBtn(), padx=20, pady=10)
buttonC.grid(row=4, column=0, padx = 10, pady = 10)
buttonTot = tkinter.Button(frame1, text = '=', command = InputBtn(), padx=20, pady=10)
buttonTot.grid(row=4, column=2, padx = 10, pady = 10)
buttonAdd = tkinter.Button(frame1, text = '+', command = InputBtn(), padx=20, pady=10)
buttonAdd.grid(row=1, column=3, padx = 10, pady = 10)
buttonMin = tkinter.Button(frame1, text = '-', command = InputBtn(), padx=20, pady=10)
buttonMin.grid(row=2, column=3, padx = 10, pady = 10)
buttonMul = tkinter.Button(frame1, text = '*', command = InputBtn(), padx=20, pady=10)
buttonMul.grid(row=3, column=3, padx = 10, pady = 10)
buttonDiv = tkinter.Button(frame1, text = '/', command = InputBtn(), padx=20, pady=10)
buttonDiv.grid(row=4, column=3, padx = 10, pady = 10)

mywin.mainloop()