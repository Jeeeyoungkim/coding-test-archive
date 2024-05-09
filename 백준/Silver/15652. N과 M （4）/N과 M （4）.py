import sys

# 1부터 N까지 자연수 중에서 M개를 고른 수열 + 같은 수를 여러개 골라도 됨 + 오름차순
N, M = map(int, input().split())
sequence = []

def dfs(start, end, select):
    if len(sequence) == select:
        print(*sequence)
        return
    
    for i in range(start, end+1):
        sequence.append(i)
        dfs(i, end, select)
        sequence.pop()

dfs(1, N, M)