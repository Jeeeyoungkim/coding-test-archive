def solution(numbers, hand):
    answer = ""
    left = 10
    right = 12
    
    left_nums = [1, 4, 7]
    right_nums = [3, 6, 9]
        
    for num in numbers:
        if num == 0:
            num = 11
        
        if num in left_nums:
            answer += "L"
            left = num
        elif num in right_nums:
            answer += "R"
            right = num
        else:
            absL = abs(left-num)
            absR = abs(right-num)
            dL = (absL // 3) + (absL % 3)
            dR = (absR // 3) + (absR % 3)
            
            if dL > dR:
                answer += "R"
                right = num
            elif dL < dR:
                answer += "L"
                left = num
            else:
                if hand == "right":
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num
         
    return answer