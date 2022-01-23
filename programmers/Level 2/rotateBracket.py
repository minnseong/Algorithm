# Programmers 01/23 2022
# 괄호 회전하기

def rotate(bracket):
    bracket = bracket[1:] + bracket[0]
    return bracket

def solution(s):
    answer = 0
    b_dict = {"(":"x", ")":"(", "{":"x", "}":"{", "]":"[", "[":"x"}

    for i in range(len(s)):
        if i == 0:
            rb = s
        else:
            rb = rotate(rb)
        
        rb_ = list(rb)
        stack = [rb_[0]]

        i = 1
        while i < len(rb_):
            if stack and stack[-1] == b_dict[rb_[i]]:
                stack.pop()
            else:
                stack.append(rb_[i])
            
            i += 1

        if not stack:
            answer += 1

    return answer

print(solution("[](){}"))