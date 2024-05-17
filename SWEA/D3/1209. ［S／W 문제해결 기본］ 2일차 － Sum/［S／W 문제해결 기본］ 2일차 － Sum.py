
T = 10

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test = 100
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(test)]
    #arr = [[1, 2, 3], [4, 5, 6], [6, 8, 9]]
    # 행열 구하기
    row_total = []
    col_total = []

    for i in range(test):
        row_temp = 0
        col_temp = 0
        for j in range(test):
            row_temp += arr[i][j]
            col_temp += arr[j][i]
       
        row_total.append(row_temp)
        col_total.append(col_temp)

   
    d1, d2 = 0, 0
    # 부 대각선 구하기
    for i in range(test):
        d1 += arr[i][i]

    # 주 대각선 구하기
    for i in range(test):
        for j in range(test-1, -1, -1):
            if i + j == test-1:
                d2 += arr[i][j]


    total = []
    total.append(max(row_total))
    total.append(max(col_total))
    total.append(max(d1, d2))

    answer = max(total)

    print(f"#{test_case} {answer}")