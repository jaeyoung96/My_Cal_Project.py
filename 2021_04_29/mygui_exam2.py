import tkinter

def increase():     # number 1씩 증가
    number.set(number.get() + 1)

mywin = tkinter.Tk()    # 윈도우창 생성
mywin.geometry('200x200')   # 윈도우 사이즈 200x200
frame = tkinter.Frame(mywin)    # frame 생성
frame.pack()    # frame 배치

number = tkinter.IntVar(value=0)    # number 정수형 제어변수 클래스 생성, 초기값:0
button = tkinter.Button(frame, text='increase', command = increase, repeatdelay = 300, repeatinterval = 100)
# repeatdelay : 버튼 눌린 상태에서 command 실행까지의 대기 시간
# repeatinterval : 버튼 눌린 상태에서 command 실행의 반복 시간
button.pack()   # button 배치
label = tkinter.Label(frame, text = 'start', textvariable = number)
label.pack()    # label 배치

mywin.mainloop()