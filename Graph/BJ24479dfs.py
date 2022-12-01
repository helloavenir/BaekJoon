import sys
input = sys.stdin.readline

# 정점 N, 간선 M, 시작점 R 입력받음
N, M, R = map(int, input().split())
# 정점 N개만큼 만들어 줄 인접 리스트
adj_N = [[] for _ in range(N + 1)]

# 주어진 간선의 개수만큼 간선정보인 정점 u, v를 입력받아 나타냄
for _ in range(M):
    u, v = map(int, input().split())
    adj_N[u].append(v)
    adj_N[v].append(u)

# 호출 스택에서 입력 순서 반대로 출력되므로 출력 원하는 오름차순을 위해 내림차순으로 정렬 
for i in range(1, len(adj_N)):
    adj_N[i].sort(reverse=True)
    
def DFS(start):
    # 맨 처음 호출 스택에 시작점을 넣어 시작해주고,
    call_stack = [start]
    # 각 인덱스는 정점을 나타내고 값은 방문 여부(-1/ 1)를 나타내는 리스트 초기화
    visited = [-1]*(N + 1)
    # 방문 순서를 담을 리스트 초기화
    result = [0]*(N + 1)
    # 방문 순서 초기화
    cnt = 1
    
    while call_stack:
        # 호출 스택에서 하나씩 꺼내 
        cnt_node = call_stack.pop()
        # 이미 방문(본인 인덱스에 해당하는 값이 1)한거면 아래 코드 실행하지 말고 넘어가고
        if visited[cnt_node] == 1:
          continue
        # 방문한 게 아니면 지금 방문하니 방문(1)로 표시  
        visited[cnt_node] = 1
        # 처음 실행될 때는 초기화한 cnt 1이 방문 순서로 부여됨
        # 1~ N개의 정점을 인덱스로 하여 방문순서를 값으로 받는 리스트 result
        result[cnt_node] = cnt
        cnt += 1

        # 방문을 마친 정점의 인접리스트에서 인접점들을 돌며
        for adj_node in adj_N[cnt_node]:
            # 그 인접점 중 방문이 이루어지지 않은
            if visited[adj_node] == -1:
              # 내림차순되어 있는 정점들을 호출 스택에 모두 넣어준다
              call_stack.append(adj_node)
      # 그리고 다시 while문이 돌고 호출 스택에 아무 것도 들어 있지 않을 때 빠져나와    
    return result

# 결과는 함수 DFS를 실행하여 cnt_node를 인덱스로 하여 방문순서를 담고 있는 배열이다.
result = DFS(R)
# *는 매개변수가 몇 개가 들어갈 지 모를 리스트일 때 붙여줌 -> 첫번째 요소부터 끝까지의 값을 출력
# 각 결과의 구분자는 줄바꿈.
print(*result[1:], sep="\n")
