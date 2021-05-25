f = open('mytest.txt','r')  # 'write'로 해야 파일 생성

# #f.write('python')
# rd = f.readlines()  # line별로 읽고 list 반환
# print(rd)
#
# for line in rd:
#     print(line,end='')

for line in f:
    print(line, end='')
else:
    print()

print(f.tell()) # 파일의 포인터 위치
#f.seek(0,0)    # 파일 포인터의 위치를 (0,0)으로 옮겨서 처음부터 파일 읽고,쓰기 가능
print(f.tell())

for line in f:
    print(line, end='')
else:
    print()

f.close()