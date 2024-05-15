from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    answer = []
    index = 0
    while q:
        target = q.popleft()
        
        if target[1] < max(priorities):
            q.append(target)
        else:
            priorities.remove(target[1])
            index += 1
            if target[0] == location:
                return index

    return index