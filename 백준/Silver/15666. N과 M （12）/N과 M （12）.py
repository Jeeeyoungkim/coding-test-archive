N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
sequence = []

def dfs(start):
    if len(sequence) == M:
        print(*sequence)
        return
    
    check_number = 0
    for i in range(start, N):
        if check_number != num_list[i]:
            sequence.append(num_list[i])
            check_number = num_list[i]

            dfs(i)
            sequence.pop()
            

dfs(0)