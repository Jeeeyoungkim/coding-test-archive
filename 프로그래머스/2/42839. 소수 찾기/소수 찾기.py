import math
import itertools

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    arr = [int(num) for num in numbers]
    prime_set = set()
    
    for i in range(1, len(numbers) + 1):
        for perm in itertools.permutations(numbers, i):
            num = int(''.join(perm))
            prime_set.add(num)
    
    answer = 0
    for target in prime_set:
        if isPrime(target):
            answer += 1
    
    return answer