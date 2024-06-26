def solution(s):
    stack = []
    
    for i in range(len(s)):  
        if stack and stack[-1] == "(" and s[i] == ")":
            stack.pop()
        else:
            stack.append(s[i])

    answer = True if len(stack) == 0 else False
    
    return answer