# 좌표 압축이란 여러 곳에 흩어진 좌표들을 연속된 수들로 모아 압축하는 것

# 좌표에 인덱스를 부여
# 먼저 수들을 입력 받은 후 집합(set)으로 중복값을 없앤 뒤,
# 정렬을 해서 각 숫자들과 인덱스를 딕셔너리에 저장

# 데이터 100만개 정도 => 시간복잡도 NlogN의 알고리즘이 적당


import sys
input = sys.stdin.readline

n = int(input())
# 입력받은 좌표들의 배열
arr = list(map(int, input().split()))

# set으로 중복값 없애기
unique = list(set(arr))
# 오름차순 정렬
unique.sort()
# 딕셔너리 형태로 인덱스와 좌표를 매핑
mapping = {}
# enumerate(배열) 함수는 기본적으로는 인덱스와 원소로 이뤄진 튜플(tuple)을 만들어 줌
# 인덱스와 원소를 각각 다른 변수에 할당하기 위해 인자 풀기(unpacking)하기 위해 
# 변수 인덱스 변수인 i와 각 좌표 변수인 x를 설정해줌
for i, x in enumerate(unique):
  # 실제 좌표를 인덱스 값으로 바꿔줌 - 좌표압축
  mapping[x] = i

# 좌표압축 결과 출력(띄어쓰기로 구분)
for x in arr:
  print(mapping[x], end = ' ')





