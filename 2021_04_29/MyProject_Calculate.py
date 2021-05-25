import tkinter  
mywin = tkinter.Tk()
mywin.title('계산기')
# mywin.geometry('350x350')

frame1 = tkinter.Frame(mywin)
frame2 = tkinter.Frame(mywin)
frame2.pack()
frame1.pack()

num1, num2 = 0, 0
input_cal = 0
input_str = ''
sum1 = tkinter.StringVar()
label1 = tkinter.Label(frame2, textvariable = sum1)
sum1.set('계산식을 입력하세요 :')
label1.pack()

def Push_Btn():
def InputNum(num):
    global num1, num2
    if input_cal == 'none':
        if
    input_str += str(num)
    sum1.set(input_str)

def Add_Btn():
    global input_str, math, f_num, s_num, result
    first_num = sum1.get()
    if math == '':
        f_num = int(first_num)
        print('no plus')
    else:
        print('plus')
        s_num = int(first_num)
        result = f_num + s_num
        return result

    math = 'Add'
    print(f_num, s_num, result)
    input_str = ''
    # f_num = s_num
    # s_num = 0
    sum1.set(input_str)

    # if math == 1:
    #     print('숫자')
    #     frist_num = sum1.get()
    #     print(first_num,'+ ')
    #     math += 1
    #     return first_num
    # else:
    #     print('연산자')

    # first_num = sum1.get()
    # math = 'Add'
    # F_num = int(first_num)
    # input_str += '+'

def Min_Btn():
    pass

def Mul_Btn():
    pass

def Div_Btn():
    pass

def Equal_Btn():
    global input_str
    # total = str(eval(oper_exp))
    # result.set(total)   
    for x in input_str:
        if input_str == int:
            Mynum += str(input_str)
            print(Mynum)
        else:
            pass
    #sum1.set()
    input_str = ''

def Clear_Btn():
    global input_str
    sum1.set('')

button1 = tkinter.Button(frame1, text = '1', command = lambda: InputNum(1), padx=20, pady=10)
button1.grid(row=1, column=0, padx = 10, pady = 10)
button2 = tkinter.Button(frame1, text = '2', command = lambda: InputNum(2), padx=20, pady=10)
button2.grid(row=1, column=1, padx = 10, pady = 10)
button3 = tkinter.Button(frame1, text = '3', command = lambda: InputNum(3), padx=20, pady=10)
button3.grid(row=1, column=2, padx = 10, pady = 10)
button4 = tkinter.Button(frame1, text = '4', command = lambda: InputNum(4), padx=20, pady=10)
button4.grid(row=2, column=0, padx = 10, pady = 10)
button5 = tkinter.Button(frame1, text = '5', command = lambda: InputNum(5), padx=20, pady=10)
button5.grid(row=2, column=1, padx = 10, pady = 10)
button6 = tkinter.Button(frame1, text = '6', command = lambda: InputNum(6), padx=20, pady=10)
button6.grid(row=2, column=2, padx = 10, pady = 10)
button7 = tkinter.Button(frame1, text = '7', command = lambda: InputNum(7), padx=20, pady=10)
button7.grid(row=3, column=0, padx = 10, pady = 10)
button8 = tkinter.Button(frame1, text = '8', command = lambda: InputNum(8), padx=20, pady=10)
button8.grid(row=3, column=1, padx = 10, pady = 10)
button9 = tkinter.Button(frame1, text = '9', command = lambda: InputNum(9), padx=20, pady=10)
button9.grid(row=3, column=2, padx = 10, pady = 10)
button0 = tkinter.Button(frame1, text = '0', command = lambda: InputNum(0), padx=20, pady=10)
button0.grid(row=4, column=1, padx = 10, pady = 10)

buttonC = tkinter.Button(frame1, text = 'C', command = Clear_Btn, padx=20, pady=10)
buttonC.grid(row=4, column=0, padx = 10, pady = 10)
buttonTot = tkinter.Button(frame1, text = '=', command = Equal_Btn, padx=20, pady=10)
buttonTot.grid(row=4, column=2, padx = 10, pady = 10)
buttonAdd = tkinter.Button(frame1, text = '+', command = lambda: Push_Btn('+'), padx=20, pady=10)
buttonAdd.grid(row=1, column=3, padx = 10, pady = 10)
buttonMin = tkinter.Button(frame1, text = '-', command = lambda: Push_Btn('-'), padx=20, pady=10)
buttonMin.grid(row=2, column=3, padx = 10, pady = 10)
buttonMul = tkinter.Button(frame1, text = '*', command = lambda: Push_Btn('*'), padx=20, pady=10)
buttonMul.grid(row=3, column=3, padx = 10, pady = 10)
buttonDiv = tkinter.Button(frame1, text = '/', command = lambda: Push_Btn('/'), padx=20, pady=10)
buttonDiv.grid(row=4, column=3, padx = 10, pady = 10)

mywin.mainloop()