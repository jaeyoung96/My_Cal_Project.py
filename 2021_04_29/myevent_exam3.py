import tkinter

def CallBack_Mouse(event):  # 이벤트 받아와서 원 그리기
	cvs.create_oval(event.x-10, event.y-10, event.x+10, event.y+10)
    # 마우스 좌표를 기준으로 +-10 크기의 원 그리기
def Delete_pic(event):  # 이벤트 받아와서 처리(오른쪽 마우스)
	cvs.delete("all")
    # 캔버스의 모든 요소 삭제
mywind = tkinter.Tk()

cvs = tkinter.Canvas(mywind, width = 500, height = 400)
cvs.pack()
cvs.bind("<Button-1>", CallBack_Mouse)
cvs.bind("<B1-Motion>", CallBack_Mouse)
cvs.bind("<Button-3>", Delete_pic)


mywind.mainloop()
