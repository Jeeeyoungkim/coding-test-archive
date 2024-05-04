import pprint

def solution(board, moves):
    n = len(board) # 가로 길이
    stack = [] # stack 사용
    flag = 0 # 인형이 없는 곳에서 크레인을 작동시키는 경우
    answer = 0
    
    for move in moves:
        flag = 0
        for i in range(n):
            if board[i][move-1] != 0: # 인형이 있는지 확인
                flag = 1
                break;
        
        if flag == 1:
            stack.append(board[i][move-1])
            board[i][move-1] = 0
            
            
        # 같은 인형 없애기
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
            
    
    return answer