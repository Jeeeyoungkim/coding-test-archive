def solution(k, m, score):
    answer = 0
    apples = sorted(score, reverse=True)
    score = []
    temp = []
    
    for apple in apples:
        temp.append(apple)
        if len(temp) == m:
            score.append(min(temp))
            temp = []
    
    for i in range(len(score)):
        answer += score[i] * m
        
    return answer