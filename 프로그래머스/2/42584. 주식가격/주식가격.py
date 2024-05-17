from collections import deque

def solution(prices):
    answer = []
    cnt = len(prices)
    queue = deque(prices)
    
    # index를 기준으로 배열 슬라이싱해서 떨어지는지 찾는다
    # 효율성을 위해 배열 슬라이싱 -> 큐로 바꿈
    for index, price in enumerate(prices):
        down = -1
        queue.popleft()
        
        for q in queue:
            if price > q:
                down = queue.index(q)
                break;
        
        if down != -1:
            answer.append(down + 1)
        else:
            answer.append(cnt-index-1)
            
    return answer
