import tkinter
# 파일 대화상자 사용
from tkinter import filedialog

mywin = tkinter.Tk()
mywin.geometry('200x100')
frame = tkinter.Frame(mywin,background = 'green')
frame.pack()

def openfile():
    f = filedialog.askopenfile()    # 파일 대화상자 오픈
    if f == None:
        return
    else:
        filepath.set(f.name)
        f.close()

filepath = tkinter.StringVar()
filepath.set('No File')
btn = tkinter.Button(frame, text = 'open', command = openfile)
btn.grid(row = 0, column = 0)

lb = tkinter.Label(frame, textvariable = filepath)
lb.grid(row = 1, column = 0)
mywin.mainloop()