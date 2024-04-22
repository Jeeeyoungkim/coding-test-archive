def solution(food):
    string = ""
    
    for i, v in enumerate(food[1:]):
        v = int((v if v % 2 == 0 else v-1)/2)
        for _ in range(v):
            string += str(i+1)
        
    answer = string + "0" + string[::-1]
    
    print(answer)
    
    return answer