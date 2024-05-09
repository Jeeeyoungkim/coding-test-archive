import sys
from collections import deque

A, B = map(int, input().split())

visited = []

def bfs():
    q = deque()
    q.append((A, 1))

    while q:

        # 세가지 경우의 수
        number, count = q.popleft()
        if number == B:
            print(count)
            return
        
        if number * 2 <= B:
            q.append((number * 2, count + 1))
        
        if int(str(number) + "1") <= B:
            q.append((int(str(number) + "1"), count + 1))
        
    print(-1)

bfs()