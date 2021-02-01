# Programmers 02/01 2021
# 위장

def solution(clothes):
    answer = 1
    array = []
    num_array = []

    for i in range(len(clothes)):
        array.append(clothes[i][1])

    array.sort()

    cnt = 0
    for i in range(1, len(array)):
        if array[i-1] != array[i]:
            if not num_array:
                num_array.append(i)
            else:
                num_array.append(i - sum(num_array))
                cnt += 1

    num_array.append(len(array) - sum(num_array))

    print(array)
    print(num_array)

    for i in range(len(num_array)):
        answer *= (num_array[i]+1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

'''
    dictionary : key + value, 순서x -> index로 접근할수 없으며, key로 접근가능 
        ex) {"a" : 1, "b" : 2}
    
    선언 : a = {} , a = dict()
    for문 :
        1) key : for key in a:
        2) value : for val in a.values():
        3) key + value : for key, val in a.items():
                            print("key = {key}, value = {value}".format(key=key,value=val))
    삭제 : del a['key']
    변경,추가 : a.update({'a':2, 'b':3})                   
'''

'''
    rewrite the code above using dictionary
    
    def solution(clothes):
        answer = 1
        cloth_dic = {}
        
        for cloth in cloths:
            if cloth[1] not in cloth_dic:  
                dic[cloth[1]] = 1
            else:
                dic[cloth[1]] += 1
        
        for n in cloth_dic.values():
            answer *= n + 1
        
        return (answer - 1)
'''