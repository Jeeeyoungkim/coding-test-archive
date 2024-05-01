def solution(n, lost, reserve):
    answer = 0
    
    execept = set(lost) & set(reserve)
    lost = list(set(lost) - execept)
    reserve = list(set(reserve) - execept)
    
    for student in range(1, n+1):
        if student in lost:
            if student in reserve:
                answer += 1
                reserve.remove(student)
            elif student-1 in reserve:
                answer += 1
                reserve.remove(student-1)
            elif student+1 in reserve:
                answer += 1
                reserve.remove(student+1)
        else:
            answer +=1
        print(student, reserve)
                
    return answer