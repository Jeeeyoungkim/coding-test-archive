
N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
sequence = []

def dfs(select):
    if len(sequence) == select:
        print(*sequence)
        return
    
    for i in num_list:
        if i in sequence:
            continue

        sequence.append(i)
        dfs(select)
        sequence.pop()

dfs(M)