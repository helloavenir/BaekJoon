import sys
input = sys.stdin.readline

n = int(input())
# 입력받을 단어들의 배열
words = []
for i in range(n):
  # 문자열 오른쪽에 같이 포함된 개행문자 제거 cf.lstrip()
  words.append(input().rstrip())

# 같은 단어가 여러번 입력시 한번만 출력될 수 있게
# set 함수로 unique 값 집합을 만든 후, ({}형태)
# list 함수로 배열화
unique_words = list(set(words))

to_sort_uniques = []
for i in unique_words:
  # 길이가 짧은 것부터 출력되게 하기 위해 
  # 앞에 길이가 오고 뒤에 단어가 오는 튜플형으로 우선 만든다.  
  to_sort_uniques.append((len(i), i))

# 첫번째 원소인 길이순으로, 그 다음에 단어순으로 정렬됨
sorted_uniques = sorted(to_sort_uniques)

# 튜플형에서 앞 원소인 길이는 출력안하고(무시), 단어만으로 해서 결과 출력
for _, unique in sorted_uniques:
  print(unique)




