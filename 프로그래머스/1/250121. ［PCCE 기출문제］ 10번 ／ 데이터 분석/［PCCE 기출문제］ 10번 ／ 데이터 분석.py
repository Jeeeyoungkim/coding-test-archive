def solution(data, ext, val_ext, sort_by):
    answer = []

    ext_list = {"code":0, "date":1, "maximum":2, "remain":3}
    
    for d in data:
        if d[ext_list[ext]] < val_ext:
            answer.append(d)

    answer.sort(key = lambda x:x[ext_list[sort_by]])
    return answer