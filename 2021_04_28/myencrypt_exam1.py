'''
def encrypt(msg):
    for ch in msg:
        if ch in encbook:
            msg = msg.replace(ch, encbook[ch])
    return msg

def Decryptfnc(msg):
    decbook = {}
    for ch in encbook:
        decbook[encbook[ch]] = ch
    print(decbook)
    for ch in msg:
        if ch in decbook:
            msg = msg.replace(ch, decbook[ch])
    return msg

encbook = {'p':'%','y':'!','t':'@','h':'#','o':'^','n':'&',}

res_msg = encrypt('I love python programming')
print(res_msg)
dec_msg = Decryptfnc(res_msg)
print(dec_msg)
'''

def MakeAlphaValue(key):
    mylist = [(chr(x+65),x)for x in range(26)]  # (0~25)를 (x+65,x)에 매칭하여 65인 A부터 출력

    mydic = {}  # 새로운 list 생성
    mydic = dict(mylist)

    print(mylist,'\n')
    print(mydic,'\n')

    if key in mydic:
        k = mydic[key]
    else:
        return None
    return k

key_data = MakeAlphaValue('L')
print('key_data :',key_data)