N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

sequence = []

def dfs(end_sequence):
    if len(sequence) == M:
        print(*sequence)
        return
    
    for i in range(1, end_sequence + 1):
        if i in sequence:
            continue

        sequence.append(i)
        dfs(end_sequence)
        sequence.pop()

dfs(N)
