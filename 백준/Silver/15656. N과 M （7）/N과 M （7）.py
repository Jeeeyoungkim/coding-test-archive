# N개의 자연수 중에서 M개를 고른 수열 + 중복 허용 + 오름차순

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
sequence = []

def dfs(start):
    if len(sequence) == M:
        print(*sequence)
        return
    
    for i in range(start, N):
        sequence.append(num_list[i])
        dfs(0)
        sequence.pop()

dfs(0)