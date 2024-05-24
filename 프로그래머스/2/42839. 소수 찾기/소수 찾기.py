import math

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    arr = [int(num) for num in numbers]
    prime_set = []
    visited = [0] * len(arr)
    
    def dfs(start, sequence, visited):
        if start == len(arr) and sequence:
            prime_set.append(sequence)
            return

        for i in range(0, len(arr)):
            if visited[i] != 1: # 선택안한 숫자면
                visited[i] = 1
                dfs(start+1, sequence + str(arr[i]), visited) # 선택한경우
                dfs(start+1, sequence, visited) # 선택안한경우
                visited[i] = 0

    answer = 0
    dfs(0, "", visited)
    prime_set = set(map(int, prime_set))   
    
    for target in prime_set:
        if isPrime(target):
            answer += 1
    
    return answer