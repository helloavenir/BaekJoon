document = input()
word = input()

index = 0
result = 0

# 문서 전체 길이에서 현재 인덱스가 단어 길이만큼 남아있거나 조금 더 남아있으면 수행
while len(document) - index >= len(word):
  # 문서와 문자 비교, 처음엔 인덱스 0~글자길이의 인덱스까지 해서 비교
  if document[index : index+len(word)] == word:
    # 단어 찾으면 갯수 하나 카운팅
    result += 1
    # 단어 길이만큼 인덱스 이동해서 새로 비교 시작
    index += len(word)
  # 같은 글자 발견 안되면 인덱스 하나만 옆으로 가서 다시 비교
  else:
    index += 1

print(result) 
