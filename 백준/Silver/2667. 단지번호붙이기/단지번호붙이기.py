# 단지번호 붙이기

from collections import deque

N = int(input())
MAP = [[int(i) for i in list(input())] for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = []

def bfs(x, y):
    q = deque()
    q.append([x, y]) # 큐에 초기 데이터 삽입하기
    visited[x][y] = 1 # 방문했다는 표시하기
    count = 1

    while q:
        curX, curY = q.popleft()

        for i in range(4):
            mx, my = curX + dx[i], curY + dy[i]
            if mx >= 0 and my >= 0 and mx < N and my < N:
                if visited[mx][my] != 1 and MAP[mx][my] != 0:
                    q.append([mx, my])
                    visited[mx][my] = 1
                    count += 1
    
    return count


for i in range(N):
    for j in range(N):
        if visited[i][j] != 1 and MAP[i][j] != 0:  
            ans.append(bfs(i, j))

print(len(ans))
ans.sort()
for i in ans:
    print(i)