def solution(phone_book):
    phone_book = set(phone_book)
        
    for phone in phone_book:
        temp = ""
        for number in phone:
            temp += number
            if temp in phone_book and temp != phone:
                print(temp)
                return False

        

            
    return True
                