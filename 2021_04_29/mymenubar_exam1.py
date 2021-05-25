import tkinter

def program_exit():
    mywin.quit()    # 윈도우 종료

mywin = tkinter.Tk()
menubar = tkinter.Menu(mywin)   # MenuBar 자리 생성
mywin['menu'] = menubar     # MenuBar 의 menu 생성

menu_file = tkinter.Menu(menubar, tearoff = 0)
menu_edit = tkinter.Menu(menubar,tearoff = 0)
menu_help = tkinter.Menu(menubar, tearoff = 0)

menubar.add_cascade(menu = menu_file, label = 'file')
menubar.add_cascade(menu = menu_edit, label = 'edit')
menubar.add_cascade(menu = menu_help, label = 'help')

menu_file.add_command(label = 'Open')
menu_file.add_command(label = 'Save_as')
menu_file.add_command(label = 'Exit', command = program_exit)

mywin.mainloop()