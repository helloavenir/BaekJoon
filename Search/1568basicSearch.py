n = int(input())
result = 0
# 한번에 날이가는 새의 수 초기화
k = 1

# 새가 남아있는 동안
while n != 0:
  # 날아가야 하는 새의 수 k가 남은 새 수보다 크면
  if k > n:
    # 날아가야하는 새의 수를 1로 다시 한다.
    k = 1
  # 남은 수가 더 많을 때에는 남은 새의 수 에서 날아가야 하는 새의 수를 빼준다.
  n -= k 
  # 그리고 다음에 날아가야할 새의 수를 하나 더 크게 한다.
  k += 1
  # 이렇게를 한 횟수로 카운팅
  result += 1

print(result)
