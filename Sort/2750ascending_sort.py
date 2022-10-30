# 입력받을 수의 갯수
n = int(input())

if 1 <= n <= 1000:
  num_list = []
  for i in range(n):
    if abs(int(input())) <= 1000:
      num_list.append(int(input()))

sorted_list = sorted(num_list)

for i in range(len(sorted_list)):
  print(sorted_list[i])
