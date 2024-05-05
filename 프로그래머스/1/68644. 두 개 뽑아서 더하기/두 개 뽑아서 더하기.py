import itertools

def solution(numbers):
    answer = []
    number_index = list(range(len(numbers)))

    combi = list(itertools.combinations(number_index,2))
    
    for index1, index2 in combi:
        answer.append(numbers[index1] + numbers[index2])
        
    answer = list(set(answer))
    answer.sort()
    
    return answer
    
    
          
    