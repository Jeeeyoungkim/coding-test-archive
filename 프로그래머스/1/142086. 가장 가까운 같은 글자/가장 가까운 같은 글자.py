def solution(s):
    answer = []

    for i, v in enumerate(s):
        target_index = s.rfind(v, 0, i)
        answer.append(-1 if target_index == -1 else i-target_index)
    
    return answer