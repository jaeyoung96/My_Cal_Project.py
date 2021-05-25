import tkinter
from tkinter import messagebox

def CancelClick():
    text_id.set('')
    text_pw.set('')

def OkClick():
    try:
        id_value = text_id.get()
        pw_value = text_pw.get()

        messagebox.showinfo('입력 데이터 확인', 'ID : {}, PW : {}'.format(id_value,pw_value))
    except:
        messagebox.showwarning('입력 오류', '정확히 입력하세요')
        text_id.set('')
        text_pw.set('')

mywin = tkinter.Tk()
mywin.geometry('300x300')
frame = tkinter.Frame(mywin)
frame.pack()

text_id = tkinter.StringVar(value='')
text_pw = tkinter.IntVar(value=0)

lb1 = tkinter.Label(frame, text = 'ID(문자열 입력)')
lb1.grid(row = 0, column = 0)
txt = tkinter.Entry(frame, textvariable = text_id)
txt.grid(row = 0, column = 1)

lb2 = tkinter.Label(frame, text='PW(정수 입력)')
lb2.grid(row=1, column=0)
txt_pw = tkinter.Entry(frame, textvariable=text_pw, show = '*')
txt_pw.grid(row=1, column=1)
text_pw.set('')

btn_ok = tkinter.Button(frame, text = '입력 확인', command = OkClick)
btn_ok.grid(row=2,column=1)

btn_cancel = tkinter.Button(frame, text = '입력 취소', command = CancelClick)
btn_cancel.grid(row=2, column=2)

mywin.mainloop()