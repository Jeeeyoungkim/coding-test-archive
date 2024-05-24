import math

def solution(brown, yellow):
    total = brown + yellow
    possible_set = []
    
    for i in range(1, total+1):
        j = total / i
        if j - int(j) != 0:
            continue
        
        possible_set.append([i, int(j)])
    
    for i, j in possible_set:
        y_h, y_v = i-2, j-2
        if y_h * 2 + y_v * 2 + 4 == brown:
            break;
            
    if i < j:
        i, j = j, i
    answer = [i, j]
    return answer