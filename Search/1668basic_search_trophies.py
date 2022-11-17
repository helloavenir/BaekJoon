# 왼쪽에서 쳐다볼 때 보일 트로피 개수 계산 함수
def left_ascending(trophies):
  comparing_one = trophies[0]
  # 우선 first 한 개는 보이니까 result = 1로 초기화
  result = 1

  for i in range(1, len(trophies)):
    # 비교기준보다 다음께 크면 결과 카운팅 하나 추가
    # 비교기준보다 다음께 작으면 비교기준이 다음꺼로 바뀌지 않고 다다음 것과 비교
    if comparing_one < trophies[i]:      
      result += 1
      # 비교 기준이 다음 트로피로 바뀜 
      comparing_one = trophies[i]
  # 왼쪽 시작을 기준으로 이전 것보다 큰 것만 추가 카운팅되어 결과 담김
  return result

# 나열할 트로피 개수
n = int(input())
# 입력받을 트로피들 높이 리스트 초기화
trophies = []

# 높이 리스트 입력받은 개수만큼 채우기
for _ in range(n):
  trophies.append(int(input))

# 위의 리스트를 인수로 하여 왼쪽에서 보이는 갯수 구하는 함수 실행
print(left_ascending(trophies))
# 오른쪽에서 볼 때의 보이는 개수를 위해 리스트를 반대로 뒤집어 위의 함수 실행
# reverse하면 리스트가 새로 만들어지는 게 아니라 원형 변형(훼손)됨 
trophies.reverse()
print(left_ascending(trophies))
