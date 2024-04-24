def solution(babbling):
    answer = 0
    joka = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        if word in joka:
            answer += 1
        else:
            temp1 = ''
            temp2 = ''
            for w in word:
                temp1 += w
                if temp1 != temp2 and temp1 in joka:
                    print(temp1)
                    temp2 = temp1
                    temp1 = ''
            if temp1 == '':
                answer += 1
        
    return answer