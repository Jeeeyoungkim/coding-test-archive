from collections import deque

N, M, K = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 인접 리스트 만들기
MAP = [[0 for i in range(M)] for _ in range(N)]
visited = [[0 for i in range(M)] for _ in range(N)]

# 좌표로 지도 만들기
for _ in range(K):
    x, y = map(int, input().split())
    MAP[x-1][y-1] = 1

# 인접한 음식물의 개수 구하기
def bfs(x, y):
    food = 1
    visited[x][y] = 1
    q = deque()
    q.append((x,y))

    while q:
        curX, curY = q.popleft()
        for i in range(4):
            mX, mY = curX + dx[i], curY + dy[i]

            if 0 <= mX < N and 0 <= mY < M and visited[mX][mY] == 0 and MAP[mX][mY] == 1:
                q.append((mX, mY)) # 방문처리
                visited[mX][mY] = 1
                food += 1

    return food

result = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1 and visited[i][j] == 0:
            temp = bfs(i,j)
            
            if result < temp:
                result = temp

print(result)