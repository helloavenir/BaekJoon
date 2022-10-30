# 변수 n과 k의 값을 한꺼번에 입력받아 split으로 나눠 담아줌
# map(적용시킬 함수, 적용시킬 값) : 특정한 함수를 리스트의 각 요소에 적용하고 결과를 담은 map 객체를 반환
n, k = map(int, input().split())
# 반환된 map객체를 list로 변환시켜줌
scores = list(map(int, input().split()))
# 내림차순
scores.sort(reverse=True)
# 입력받은 k등까지 출력
print(scores[k-1])
