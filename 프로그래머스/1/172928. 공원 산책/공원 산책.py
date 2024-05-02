def solution(park, routes):
    answer = []
    sX = 0
    sY = 0
    dx = [1, -1, 0, 0] # 동(S), 남(E), 서(N), 북(W) 순서로 변경
    dy = [0, 0, -1, 1]

    for x, p in enumerate(park):
        for y, word in enumerate(p):
            if word == "S":
                print("starting point :", x, y) # 시작점 찾기
                sX = x
                sY = y
 
    for route in routes:
        check = True
        directions = {"S":0, "N":1, "W":2, "E":3}
        step = int(route[-1])
        direction = directions[route[0]]
        nX, nY = sX, sY 
        for _ in range(step):
            nX += dx[direction]
            nY += dy[direction]
            print("Y체크",nY, len(park[0]))
            if (0 <= nX < len(park)) and (0 <= nY < len(park[0])):
                if park[nX][nY] == "X":
                    check = False
                    break;
            else:
                check = False
                break;
        
        if check:
            sX += dx[direction] * step
            sY += dy[direction] * step
    
    return [sX, sY]