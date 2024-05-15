def solution(arr):
    answer = []
    
    for num in arr:
        answer.append(num)
        
        if len(answer) >1 and answer[-1] == answer[-2]:
            answer.pop()
    
    return answer