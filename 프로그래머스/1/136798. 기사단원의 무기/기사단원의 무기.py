import math

def solution(number, limit, power):
    yaksu_list = []
    answer = 0
    
    # 1~number 까지의 약수의 개수 list 구하기
    for k in range(1, number+1):
        yaksu = 0
        
        for i in range(1, int(math.sqrt(k))+1):
            if k % i == 0:
                yaksu += 1
                if i != k // i:
                    yaksu += 1
        yaksu_list.append(yaksu)
        
    
    # 약수의 개수 list 돌면서 limit 넘는지 확인, 
    # limit 제한조건 확인하면서 answer에 더하기
    answer = sum([value if value <= limit else power for value in yaksu_list ])
    
    return answer