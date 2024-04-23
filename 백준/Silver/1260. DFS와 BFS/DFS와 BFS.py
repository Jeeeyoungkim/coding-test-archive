def dfs(c):
    visited[c] = 1 # 방문 표시
    answer_dfs.append(c) # 방문 노드 추가

    for n in adj[c]:
        if not visited[n]: # 방문하지 않았다면
            dfs(n)

def bfs(s):
    q  = []
    q.append(s) # 큐에 초기 데이터 삽입
    visited[s] = 1 # 방문 표시
    answer_bfs.append(s) # 방문 노드 추가

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not visited[n]: # 방문하지 않았다면 큐에 넣기
                q.append(n)
                visited[n] = 1 # 단위작업 시작
                answer_bfs.append(n)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)] # 인접 리스트 초기화

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향임 !!

# 인접 리스트 오름차순 정렬하기
for i in range(1, N+1):
    adj[i].sort()

visited = [0] * (N+1)
answer_dfs = []
dfs(V)

visited = [0] * (N+1)
answer_bfs = []
bfs(V)

print(*answer_dfs)
print(*answer_bfs)