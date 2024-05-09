def solution(n, m, section):
    answer = 1 # 첫번째 페인트칠하기
    standard = section[0]
    
    for paint in section:
        if paint > standard + m - 1:
            answer += 1
            standard = paint
        
    return answer