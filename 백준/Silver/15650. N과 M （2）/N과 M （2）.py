import sys

#sys.stdin = open("input.txt", "r")

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순으로 

N, M = map(int, input().split())

sequence = []

def dfs(start_index, end_index, select_count):
    if len(sequence) == select_count:
        print(*sequence)
        return

    for i in range(start_index, end_index+1):
        if i not in sequence:
            sequence.append(i)
            dfs(i+1, end_index, select_count)
            sequence.pop()

dfs(1, N, M)