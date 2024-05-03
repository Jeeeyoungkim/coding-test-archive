def solution(a, b):

    weekdays = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    monthdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    
    for i in range(1, a):
            day += monthdays[i-1]
    day += b
    answer = weekdays[(day-1)%7]
    
    return answer