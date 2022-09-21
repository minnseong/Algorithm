# Programmers 09/21 2022
# Level 2 - 전화번호목록

def solution(phone_book): 
    
    phone_book.sort()
    phone_set = set()
    
    for p in phone_book:
        phone_set.add(p)
    
    for phone in phone_book:
        tmp = ""
        for n in phone:
            tmp += n
            if tmp in phone_set and tmp != phone:
                return False
            
    return True