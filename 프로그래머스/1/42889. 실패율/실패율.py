def solution(N, stages):
    fault = [0] * N # index - 스테이지 번호, fault[index][0] - 도전한 유저
    clear = [0] * N # index - 스테이지 번호, clear[index][0] - 성공한 유저
    user = len(stages)
    
    for index, stage in enumerate(stages):
        if stage == N+1:
            for i in range(len(fault)):
                fault[i] += 1
        else:
            clear[stage-1] += 1
            for i in range(stage):
                fault[i] += 1
    
    fault_dict = {}
    # 실패율 계산
    for i in range(N):
        if fault[i] == 0:
            fault_dict[i] = 0
        else:
            fault_dict[i] = clear[i] / fault[i]
    
    answer = []
    for (s, e) in sorted(fault_dict.items(), key = lambda x: x[1], reverse=True):
        answer.append(s+1)
        
    return answer