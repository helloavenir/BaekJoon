# factorial 함수 정의
def factorial(n):
  # n=0 일때 출력값
  result = 1
  if n > 0:
    # 재귀함수 사용
    # n=1일 때, 1 출력됨
    result = n * factorial(n-1)
  return result

# n 입력받음
# 들여쓰기 주의 !!
n = int(input())

print(factorial(n))
