def solution(n):
    answer = 0
    
    v1 = [0] * n
    v2 = [0] * (2*n)
    v3 = [0] * (2*n)

    
    # visited 배열 세개
    # 1. 행을 배교하는 visited 배열 j
    # 2. 오른쪽으로 가는 대각선 visited 배열 i+j
    # 3. 왼쪽으로 가는 대각선 visited 배열 i-j
    def dfs(x, n):
        nonlocal answer

        if x == n:
            answer += 1
            return

        for j in range(n):
            if v1[j] == v2[x+j] == v3[x-j] == 0:
                v1[j] = v2[x+j] = v3[x-j] = 1
                dfs(x+1, n)
                v1[j] = v2[x+j] = v3[x-j] = 0

    dfs(0, n)
    return answer

