def solution(progresses, speeds):
    answer = []
    left = []
    
    # 남은 일 수 계산하기
    for i, p in enumerate(progresses):
        temp = (100 - p) / speeds[i]
        temp = int(temp) + 1 if temp - int(temp) > 0 else int(temp)
        left.append(temp)
        
    print(left)

    start = 0 # 작업일 수를 비교하기 위한 기준이 되는 인덱스
    for idx in range(len(left)):
        if left[start] < left[idx]:
            # 기준값 보다 그 다음값이 큰 경우에 기능의 개수를 세고
            answer.append(idx-start)
            # 기준값 인덱스 업데이트
            start = idx
    answer.append(len(left)-start)
    return answer