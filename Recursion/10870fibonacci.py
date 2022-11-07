# fibonacci 함수 정의
def fibonacci(n):
  # n이 0과 1일때는 자기 자신이 출력됨
  if (n == 0) or (n == 1):
    return n
  # n이 1보다 클 때
  if n > 1:
    # n을 만들기 위해 그 이전 수와 그 이전의 이전 수와 더함
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
  
