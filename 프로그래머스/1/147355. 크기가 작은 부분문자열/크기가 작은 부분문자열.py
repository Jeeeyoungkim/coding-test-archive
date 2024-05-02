from collections import deque

def solution(t, p):
    answer = 0
    q = deque('')
    
    for word in t:
        q.append(word)
        if len(q) >= len(p):
            if int(''.join(q)) <= int(p):
                answer += 1
            q.popleft()
        
    return answer