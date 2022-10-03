def solution(brown, yellow):
    
    tmp = 1
    while tmp <= yellow:
        if yellow % tmp == 0:
            w, h = tmp, yellow//tmp
            
            if 2*w+2*h+4 == brown:
                return [max(w,h)+2, min(w,h)+2]
            else:
                tmp += 1
        else:
            tmp += 1
                