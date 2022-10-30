# 빠른 입력 함수(sys.stdin.readline) 사용
import sys
# sys.stdin.readline()은 개행문자 포함하여 한줄 단위로 입력받음
input = sys.stdin.readline
# 입력값은 문자열로 인식하기 때문에 형변환해줌
n = int(input())

vectors = []
for i in range(n):
  [x, y] = map(int, input().split())
  # y좌표를 기준으로 정렬하기 위해 y좌표를 앞으로 오게 한 뒤 정렬 예정
  reverse = [y, x]
  vectors.append(reverse)
# y좌표 기준으로 오름차순 정렬
sorted_vectors = sorted(vectors)
# [y, x]순으로 되어 있는 배열 원소를 출력시 [x, y]로 위치 변경
# y 좌표순으로 정렬되어 있는 상태에서 x 먼저 출력되므로, x는 자동 정렬되어 출력 될 것
for y, x in sorted_vectors:
  print(x, y)
