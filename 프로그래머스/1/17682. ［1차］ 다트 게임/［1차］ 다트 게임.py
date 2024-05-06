def solution(dartResult):
    score = []
    bonus = {'S':1, 'D':2, 'T':3}
    option = ['*', '#']
    dart_round = 0
    
    for index, dart in enumerate(list(dartResult)):
        if dart.isnumeric():     # 숫자 추출하기
            if index < len(dartResult)-1 and dartResult[index+1].isnumeric():
                score.append(int(dartResult[index:index+2]))
                dart_round += 1

            elif index >= 1 and dartResult[index-1].isnumeric():
                pass
            else:
                score.append(int(dart))
                dart_round += 1

            
        if dart in ['S', 'T', 'D'] and len(score) >= dart_round:
            score[dart_round-1] = score[dart_round-1] ** bonus[dart]
        
        if dart == '*' and len(score) >= dart_round:
            score[dart_round-1] = score[dart_round-1] * 2
            if dart_round > 1:
                score[dart_round-2] = score[dart_round-2] * 2
                
        if dart == '#' and len(score) >= dart_round:
            score[dart_round-1] = score[dart_round-1] * -1
            
    print(score)
    return sum(score)