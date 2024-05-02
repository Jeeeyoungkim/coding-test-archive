import sys
from collections import deque

N, M = map(int, input().split())
MAP = [[i for i in list(input())] for _ in range(M)]

visited = [[0 for i in range(N)] for i in range(M)]
white_count = 0
blue_count = 0

def bfs(i,j):
    q = deque()
    q.append([i,j]) 
    visited[i][j] = 1
    count = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        curX, curY = q.popleft()
        for i in range(4):
            mX = curX + dx[i]
            mY = curY + dy[i]

            if 0 <= mX < M and 0 <= mY < N:
                if MAP[mX][mY] == MAP[curX][curY] and visited[mX][mY] == 0:
                    q.append([mX, mY])
                    visited[mX][mY] = 1
                    count += 1

    return count

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            cnt = bfs(i, j)
            if MAP[i][j] == 'W':
                white_count += cnt ** 2
            else:
                blue_count += cnt ** 2


print(white_count, blue_count)
