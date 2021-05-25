import tkinter
fig = 0

def draw_figure(event):
    if fig ==1:
        cvs.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10)
    elif fig ==2:
        cvs.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10)
    elif fig ==3:
        cvs.create_line(event.x, event.y, event.x+10, event.y+10)

def choose_rectangle():
    global fig
    fig = 1

def choose_oval():
    global fig
    fig = 2

def choose_line():
    global fig
    fig = 3

def program_delete():
    cvs.delete('all')

def program_exit():
    mywin.quit()    # 윈도우 종료

mywin = tkinter.Tk()
menubar = tkinter.Menu(mywin)   # MenuBar 자리 생성
mywin['menu'] = menubar     # MenuBar 의 menu 생성

cvs = tkinter.Canvas(mywin, width = 500, height = 500)
cvs.pack()
cvs.bind('<Button-1>',draw_figure)
menu_draw = tkinter.Menu(menubar, tearoff = 0)
menu_delete = tkinter.Menu(menubar,tearoff = 0)
menu_exit = tkinter.Menu(menubar, tearoff = 0)

menubar.add_cascade(menu = menu_draw, label = '도형 그리기')
menubar.add_cascade(menu = menu_delete, label = '도형 삭제')
menubar.add_cascade(menu = menu_exit, label = '프로그램 종료')

menu_draw.add_command(label = '사각형 그리기', command = choose_rectangle)
menu_draw.add_command(label = '원 그리기', command = choose_oval)
menu_draw.add_command(label = '선 그리기', command = choose_line)

menu_delete.add_command(label = '모두 삭제', command = program_delete)
menu_exit.add_command(label = '종료', command = program_exit)

mywin.mainloop()