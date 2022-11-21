# 집의 개수와 설치할 공유기 개수
n, c = list(map(int, input().split(' ')))
# 입력받은 집 위치를 저장할 리스트
houses = []
# 이진탐색은 반복문으로 접근하는게 유리한 경우가 많음
for _ in range(n):
  houses.append(int(input()))
houses = sorted(houses)
# 첫 집으로부터의 최소거리와 최대거리
min_distance = 1
max_distance = houses[-1] - houses[0]
# 공유기 최대거리 초기화
result = 0

while(min_distance <= max_distance):
  # 닶이 가능한 작은 거리부터 최대 큰 거리까지 순회하면서 두 값의 중간값에서부터 답을 찾기 시작 
  mid = (min_distance + max_distance) // 2
  # 첫 공유기를 설치할 첫번째 집 위치
  installed = houses[0]
  router_cnt = 1
  for i in range(1, len(houses)):
    # 이전 라우터와 첫번째 설정한 거리를 더한 값과 같거나 크다면 또 설치 가능 
    if houses[i] >= installed + mid:
      # 새로 설치된 위치에서 다시 거리 계산 시작  
      installed = houses[i]
      router_cnt += 1
  # 설치가능 공유기가 주어진 개수 이상이면 가능한 거리(mid)이므로
  if router_cnt >= c:
    # 먼저 가능한 이 값에서 +1한 거리로 다시 시도해본다.
    min_distance = mid + 1
    # 이 값을 공유기 최대거리로 우선 저장
    result = mid
  # 만약 주어진 개수가 다 안 설치되면 최대거리를 -1 줄여 다시 해봄 
  else:
    max_distance = mid - 1
# 최종적으로 담기는 최대거리를 출력함
print(result)

   





  




   





  


