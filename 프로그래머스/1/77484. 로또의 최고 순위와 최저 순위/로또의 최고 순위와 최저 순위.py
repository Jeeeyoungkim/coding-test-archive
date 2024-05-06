def solution(lottos, win_nums):
    score = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0) # 안 보이는 숫자 count
    
    min_score = len(set(lottos) & set(win_nums))
    max_score = min_score + zero_count
    
    answer = [score[max_score], score[min_score]]
    return answer