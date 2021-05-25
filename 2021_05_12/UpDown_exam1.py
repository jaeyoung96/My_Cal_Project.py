import time
import random

N = 80000

input_list = []
output_list = []
for i in range(N):
    input_list.append(random.randint(0,100000))

start_time = time.time()
count = [0] * (max(input_list) + 1)

for j in range(len(input_list)):
    count[input_list[j]] += 1
# print(count)

count.reverse()
print(count)

end_time = time.time()
print("\ntime = ",end_time - start_time)