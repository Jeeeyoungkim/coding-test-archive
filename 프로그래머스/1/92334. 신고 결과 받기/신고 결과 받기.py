def solution(id_list, report, k):
    report_count = {}
    report_history = {}
    
    # 신고당한 기록 dictionary 초기화
    for ID in id_list:
        report_count[ID] = 0 
    
    # 신고한 기록 dictionary 초기화
    for ID in id_list:
        report_history[ID] = []  

    # 신고당한 횟수, 신고한 id 기록 dictionary에 기록
    for element in report:
        user_id, report_id = element.split(' ')
        
        if not report_id in report_history[user_id]:
            report_history[user_id].append(report_id)
            report_count[report_id] += 1
            
    # 정지먹은 유저 계산하기
    stop_user = [user for user in list(report_count.keys()) if report_count[user] >= k]
    
    answer = []

    # 결과 메일 수 계산 로직
    for user in (list(report_history.keys())):
        ans = 0
        for ID in report_history[user]:
            if ID in stop_user:
                ans += 1
        answer.append(ans)

    return answer