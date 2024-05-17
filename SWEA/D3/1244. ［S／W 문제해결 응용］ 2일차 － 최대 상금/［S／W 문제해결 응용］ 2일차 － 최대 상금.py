'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

def dfs(n):
    global answer
    if n == change:
        answer = max(answer, int("".join(map(str, goal))))
        return
    
    # 0에서 시작하는거니까
    for i in range(len(goal)):
        for j in range(i+1, len(goal)):
            goal[i], goal[j] = goal[j], goal[i]
            temp = int("".join(goal))
            if (n, temp) not in visited:
                dfs(n+1)
                visited.append((n, temp))
            goal[j], goal[i] = goal[i], goal[j]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, change = map(int, input().split())
    lst, visited = [], []
    goal = list(str(N))
    answer = 0
    dfs(0)
    print(f'#{test_case} {answer}')






    


