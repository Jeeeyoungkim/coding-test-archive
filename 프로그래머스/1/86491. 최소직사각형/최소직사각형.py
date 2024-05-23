def solution(sizes):
    maxX, maxY = 0, 0
    
    for x, y in sizes:
        if x < y:
            x, y = y, x
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y
    
    answer = maxX * maxY
    return answer