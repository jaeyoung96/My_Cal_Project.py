def InsertData():
    name = input('이름 입력 : ')
    number = input('전화번호 입력 : ')
    addresslist[name] = number

def Display():
    for x in addresslist:
        print(x,' : ',addresslist[x])

def DeleteData():
    delname = input('삭제할 이름 입력 :')
    for x in addresslist:
        if delname == list(addresslist.keys(x)):
            res = addresslist.pop(delname)
        else:
            print('등록되지 않은 이름입니다!')

def MenuSel():
    print('1.Insert 2.Display 3.Delete 4.Exit')
    selnum = int(input('menu sel :'))
    return selnum

def runprogram():
    while True:
        selmenu = MenuSel()
        if selmenu == 1:
            InsertData()
        elif selmenu ==2:
            Display()
        elif selmenu ==3:
            DeleteData()
        elif selmenu == 4:
            break

if __name__ == '__main__':
    addresslist = {}    # 빈 사전 등록
    runprogram()