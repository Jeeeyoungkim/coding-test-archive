def solution(new_id):
    munja = '~!@#$%^&*()=+[{]}:?,<>/'

    new_id = new_id.lower() # 소문자로
    new_id = ''.join([e for e in new_id if not e in munja]) # 특수문자제거

    
    while '..' in new_id:
        new_id = new_id.replace('..', '.') # 연속된 마침표 삭제
    
    if new_id[0] == ".":
        new_id = new_id[1:]
        
    # if len(new_id) > 2 and new_id[-1] == ".":
    #     new_id = new_id[:-1]
    
    if new_id.endswith("."):
        new_id = new_id[:-1]
        
    if len(new_id) == 0:
        new_id += "a"
        
    if len(new_id) >= 16:
        new_id = new_id[:15]   
        if len(new_id) > 2 and new_id[-1] == ".":
            new_id = new_id[:-1]
        
    while (len(new_id)< 3):
        new_id += new_id[-1]

    return new_id