T = int(input())

def dfs(index, score, calorie):
    global answer

    if index == N-1:
        if calorie <= L:
            answer = max(answer, score)
        return
    # 추가하는 경우
    dfs(index+1, score + clst[index+1][0], calorie + clst[index+1][1])
    # 추가하지 않는 경우
    dfs(index+1, score, calorie)


for test_case in range(1, T+1):
    N, L = map(int, input().split())
    clst = []

    for i in range(N):
        c, taste = map(int, input().split())
        clst.append((c, taste))

    answer = 0
    dfs(-1, 0, 0)
    print(f"#{test_case} {answer}")