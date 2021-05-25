class myclasstest():
    def __init__(self):
        self.m_val = 30 # self로 속성변수로 설정
        print('init oper,,,')
    def show_data(self):
        print('m_val : ', self.m_val)

inst1 = myclasstest()   # 객체 생성
print(inst1)
inst1.show_data()   # 객체에 들어있는 멤버변수 접근
print(inst1.m_val)  # private 개념이 따로 없어서 멤버변수 외부에서 접근 가능