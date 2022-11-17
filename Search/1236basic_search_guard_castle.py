# 성의 가로, 세로 크기 한 번에 입력받음
n, m = map(int, input().split())
# 성의 행과 열의 상태를 담을 배열
row_condition = []

# 행의 개수 n개 만큼 .이나 x로 구성된 행의 배열을 입력받음
for _ in range(n):
  row_condition.append(input())

# 입력된 성의 상태를 통해 파악된 행열의 경비원 존재를 나타낼 2차원 배열 초기화
row_guard = [0] * n
column_guard = [0] * m

# 한 행씩 각 열을 돌면서 경비원이 존재하는 칸(x)을 발견하면 
for i in range(n):
  for j in range(m):
    if row_condition[i][j] == 'x':
      # 그 행과 열에는 한 명의 경비원이 존재한다는 의미로 1을 할당
      row_guard[i] = 1
      column_guard[j] = 1

# 경비원이 존재하지 않은 행과 열의 갯수를 0으로 초기화
no_row = 0
no_column = 0

# 경비원이 존재하지 않는 행(0)을 발견하면 하나씩 카운팅
for i in range(n):
  if row_guard[i] == 0:
    no_row += 1
# 경비원이 존재하지 않는 열(0)을 발견하면 하나씩 카운팅
for j in range(m):
  if column_guard[j] == 0:
    no_column += 1

print(max(no_row, no_column))
