# 촌수 계산
import sys

#sys.stdin = open("input.txt", "r")

N = int(input())
i, j = map(int, input().split())
M = int(input())
MAP = [[] for i in range(N+1)]
visited = [0] * (N+1)
result = []

for _ in range(M):
    s, e = map(int, input().split())
    MAP[s].append(e)
    MAP[e].append(s)


def dfs(x, y, chon):
    visited[x] = 1

    if x == y:
        result.append(chon)

    for i in MAP[x]:
        if visited[i] != 1:
            dfs(i, y, chon+1)

dfs(i, j, 0)
if len(result) == 0:
    print(-1)
else: 
    print(result[0])