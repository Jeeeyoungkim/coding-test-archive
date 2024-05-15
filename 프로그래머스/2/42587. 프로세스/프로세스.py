from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    answer = []
    
    while q:
        flag = 0
        target = q.popleft()
        
        if target[1] < max(priorities):
            q.append(target)
        else:
            answer.append(target)
            priorities.remove(target[1])

    process = -1
    for i in range(len(answer)):
        if answer[i][0] == location:
            process = i + 1
            
    return process