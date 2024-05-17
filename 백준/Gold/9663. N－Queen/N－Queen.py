import sys

N = int(input())
answer = 0

v1 = [0] * N # 열체크 
v2 = [0] * (2 * N) # 대각선1
v3 = [0] * (2 * N) # 대각선 2

def dfs(n):
    global answer # answer 전역변수 선언

    if n == N: # N행까지 진행한 경우 성공
        answer += 1
        return

    for j in range(N):
        if v1[j] == v2[j+n] == v3[n-j] == 0:
            v1[j] = v2[j+n] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[j+n] = v3[n-j] = 0

dfs(0)
print(answer)