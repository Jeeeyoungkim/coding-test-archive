# 바이러스

N = int(input())
M = int(input())

MAP = [[] for i in range(N+1)]
vistied = [0] * (N+1)
answer = []

for _ in range(M):
    s, e = map(int, input().split())
    MAP[s].append(e)
    MAP[e].append(s)

def dfs(s):
    vistied[s] = 1
    answer.append(s)

    for i in MAP[s]:
        if vistied[i] != 1:
            dfs(i)

    return len(answer)

print(dfs(1)-1)