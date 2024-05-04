def solution(survey, choices):
    answer_dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score = [-1, 3, 2, 1, 0, 1, 2, 3]
    answer = ''
    
    for i, element in enumerate(survey):
        if choices[i] < 4: # 비동의 관련
            answer_dict[element[0]] += score[choices[i]]            
        elif choices[i] > 4: # 동의 관련
            answer_dict[element[1]] += score[choices[i]]
            
    if answer_dict['R'] >= answer_dict['T']:
        answer += 'R'
    else:
        answer += 'T'

    if answer_dict['C'] >= answer_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if answer_dict['J'] >= answer_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if answer_dict['A'] >= answer_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    
    return answer