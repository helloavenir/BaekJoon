# 오늘 책이 팔린 갯수
n = int(input())
# 팔린 책 종류와 갯수를 담을 딕셔너리 선언
books = {}

# 여기에서의 _는 필요하지 않거나 사용되지 않는 값을 할당하는데 사용된다.
# "인덱스 무시"의 의미
for _ in range(n):
  book = input()
  # 입력받은 값이 기존의 키로 없다면 키를 넣고 1로 값을 넣어줌
  if book not in books:
    books[book] = 1
  # 이미 기존 목록에 있는 책이라면 팔린 갯수만 하나 더 늘려줌
  else:
    books[book] += 1

# 가장 많이 팔린 갯수를 확인하고, 
best_selling = max(books.values())
# 같은 갯수의 베스트셀링이 있을 경우 사전 순으로 가리기 위해 동점자 담는 리스트
same_score = []

# books에 담긴 딕셔너리형 k-v 데이터(items())를 이름과 갯수로 나눠 처리
for book, selling in books.items():
  # 동점자면 이름만 사전순 정렬할 리스트에 담음
  if selling == best_selling:
    same_score.append(book)

# 담은 리스트를 정렬(이름이니 사전순으로 될 것)하여 첫번째 오는 것 출력
print(sorted(same_score)[0])
