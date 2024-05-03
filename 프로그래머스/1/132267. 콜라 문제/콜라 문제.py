def solution(a, b, n):
    answer = 0
    cock = 0

    while (n >= a):
        cock = n // a * b
        n = n % a + cock
        answer += cock
        
    
    return answer