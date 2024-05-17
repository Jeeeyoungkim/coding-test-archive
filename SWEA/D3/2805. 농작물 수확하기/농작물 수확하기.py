T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int, input()))
        arr.append(temp)
    
    start, end = N // 2, N // 2
    value = 0

    for i in range(N):
        for j in range(start, end+1):
            value += arr[i][j]

        if i < N // 2: # mid 전까지는
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f"#{test_case} {value}")
