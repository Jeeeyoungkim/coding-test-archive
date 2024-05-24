import math

def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(1, total+1):
        if total % i != 0:
            continue
        j = int(total / i)
        
        if (i-2) * 2 + (j-2)* 2 + 4 == brown:
            break;
            
    answer = sorted([i, j], reverse=True)
    return answer