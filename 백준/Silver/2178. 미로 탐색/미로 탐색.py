from collections import deque

N, M = map(int, input().split()) # N 는 세로고 M은 가로
MAP = [[int(i) for i in list(input())] for _ in range(N)]
visited = [[0 for i in range(M)] for _ in range(N)] # 방문 정보

def bfs():
    q = deque()
    q.append([0,0]) # 큐에 초기 데이터 삽입
    visited[0][0] = 1 # 방문했다는 표시하기

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        curX, curY = q.popleft()
        for i in range(4):
            mX = curX + dx[i]
            mY = curY + dy[i]

            if 0 <= mX < N and 0 <= mY < M:
                if MAP[mX][mY] == 1 and visited[mX][mY] == 0:
                    q.append([mX,mY])
                    visited[mX][mY] = visited[curX][curY] + 1

                    
    print(visited[-1][-1]) # N-1, M-1은 도착 지점이 됩니다.

bfs()