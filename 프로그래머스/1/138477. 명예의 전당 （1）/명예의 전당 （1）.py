def solution(k, score):
    print(score)
    honor = []
    answer = []
    
    for s in score:

        if not (len(honor) == k):
            honor.append(s)
            honor.sort(reverse=True)
        else:
            if len(honor) > 0 and (min(honor) < s):
                honor.pop()
                honor.append(s) 
                honor.sort(reverse=True)
                
        answer.append(honor[-1])

    
    return answer