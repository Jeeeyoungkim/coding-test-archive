def solution(answers):
    
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)
    
    count1, count2, count3 = 0, 0, 0
    
    for index, elem in enumerate(answers):
        if s1[index % s1_len] == elem:
            count1 += 1
        if s2[index % s2_len] == elem:
            count2 += 1
        if s3[index % s3_len] == elem:
            count3 += 1
                
    temp = [count1, count2, count3]    
    max_count = max(temp)
    answer = [index + 1 for index, t in enumerate(temp) if t == max_count]
    
    return answer