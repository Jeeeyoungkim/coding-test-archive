def solution(s):
    partition = []
    isX = 0
    notX = 0
    answer = 1
    
    for string in s:
        
        if isX > 0 and isX == notX: # 두 횟수가 같아지는순간
            partition = [] # 파티션 초기화
            answer += 1
            
        partition.append(string) # 파티션에 문자 추가
        x = partition[0] # x 파티션의 첫번째 글자
        
        if string == x: # x인 글자가 나온 횟수
            isX += 1
        else:
            notX += 1
            

    return answer