# 백준_알고리즘/숫자_카드_2
n = int(input())
n_list = sorted(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
index, m_dic = 0, {}

for i in sorted(m_list):
    cnt = 0
    if i not in m_dic:
        while index < len(n_list):
            if i == n_list[index]:
                cnt += 1
                index += 1
            elif i > n_list[index]:
                index += 1
            else:
                break
        m_dic[i] = cnt

print(' '.join(str(m_dic[i]) for i in m_list))