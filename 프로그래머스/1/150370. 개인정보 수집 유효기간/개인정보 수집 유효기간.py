def count_day(today):
    # 오늘이 2000년 1월 1일 로부터 얼마나 떨어져 있는지 계산하는 함수
    today = list(map(int, today.split(".")))
    today_count = (today[0] - 2000) * 12 * 28 + (today[1]-1) * 28 + today[2]  
    
    return today_count

def solution(today, terms, privacies):
    # 2000년 1월 1일 = 1일로 산정, 2000년 1월 2일 = 2일..
    today_count = count_day(today)
    
    limit = []
    terms_dict = {}
    
    # terms -> 2차원 dictionary로 분리
    for index, term in enumerate(terms):
        term = term.split(" ")
        terms_dict[term[0]] = int(term[-1])
        
    for privacie in privacies:
        privacie = privacie.split(" ")
        limit_month = terms_dict[privacie[-1]] # 개월 수 구하기
        limit.append(count_day(privacie[0]) + limit_month * 28 - 1)
    

    answer = [i+1 for i in range(len(limit)) if today_count > limit[i]]
    
    return answer