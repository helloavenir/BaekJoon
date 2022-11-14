import sys
input = sys.stdin.readline

# 주어진 리스트를 정렬
def merge_sort(List, left, right):
  # 왼쪽 인덱스가 오른쪽 인덱스가 되기 전까지 저장된 차례가 
  # 입력된 k보다 작거나 같을때까지 반복(재귀)
  # k가 cnt보다 크면, merge_sort는 실행되지 않음 !
  if(left < right and cnt <= k):
    # 요소가 홀수개일 때는 분할된 왼쪽 리스트가 오른쪽 리스트보다 1개 작은 크기가 됨
    mid = (left + right) // 2
    # 함수가 재귀적으로 실행되면서 요소가 1개가 될때까지(left == right) 반복 분할 & 병합
    merge_sort(List, left, mid)
    merge_sort(List, mid+1, right)
    merge(List, left, mid, right)

  # 주어진 리스트, 분할된 왼쪽 리스트 인덱스, 위에서 구해진 중간점, 
  # 분할된 오른쪽 리스트 인덱스를 인수로 넣음
def merge(List, left, mid, right):
  # 함수 밖에서 사용할 수 있도록 전역변수로 선언
  global cnt, res
  # 분할된 왼쪽 리스트의 첫번째 요소 인덱스 i, 분할된 오른쪽 리스트의 첫번째 요소 인덱스 j
  i, j = left, mid+1
  # 병합정렬한 리스트를 담을 새 리스트
  new_List = []

  # 왼쪽 리스트의 첫번째 요소가 분할된 지점까지 오고, 
  # 오른쪽 리스트의 첫번째 요소가 마지막 요소가 될 때까지
  while i <= mid and j <= right:
    # 두 리스트의 맨 앞 요소를 비교해서 왼쪽 요소가 작으면 왼쪽 요소를 새 리스트에 담음
    if(List[i] <= List[j]):
      new_List.append(List[i])
      i += 1
    # 그렇지 않고 오른쪽 요소가 작으면 오른쪽 요소를 새 리스트에 담음
    else:
      new_List.append(List[j])
      j += 1
  # j > right 즉, 오른쪽 요소가 다 담겼을 때, 남은 왼쪽 요소들을 순차적으로 담는다.
  while i <= mid:
    new_List.append(List[i])
    i += 1
  # i > mid 즉, 왼쪽 요소가 다 담겼을 때, 남은 오른쪽 요소들을 순차적으로 담는다.
  while j <= right:
    new_List.append(List[j])
    j += 1

  # t: 새 리스트의 인덱스
  # 만들어진 새 리스트를 순차적으로 원래 리스트에 담으면서 순서를 count한다.
  i, t = left, 0
  while i <= right:
    List[i] = new_List[t]
    cnt += 1
    # cnt가 입력된 k와 같으면 res에 현재의 요소를 반환한다.
    if cnt == k:
      res = List[i]
      break;
    # cnt가 k와 같은게 아니면 원래 리스트의 인덱스와 새 리스트의 인덱스를 하나씩 올려준다.
    i += 1
    t += 1

n, k = map(int, input().split())
List = list(map(int, input().split()))
cnt = 0
# 반환할 값의 기본값은 -1로 설정하고, 위의 함수의 조건에 해당할 경우에만 해당 요소를 반환
res = -1
# 왼쪽 인덱스 0, 오른쪽 인덱스는 배열의 크기-1
merge_sort(List, 0, n-1)
print(res)

