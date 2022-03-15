# BaekJoon 03/15 2022
# 17609 회문

import sys

def solution(string, i, s, e, dFlag):
        flag = True
        printFlag = False
        tmp = []
        while i < len(string) // 2:
            if string[i+s] == string[len(string)-1 -i -e]:
                pass
            else:
                if not dFlag:
                    if string[i] == string[len(string) - i - 2] and string[i+1] == string[len(string) -1 -i]:
                        tmp.extend(solution(string, i, 0, 1, True))
                        tmp.extend(solution(string, i, 1, 0, True))
                        printFlag = True
                    elif string[i] == string[len(string) - i - 2]:
                        e = 1
                    elif string[i+1] == string[len(string) -1 -i]:
                        s = 1
                    
                    else:
                        flag = False
                        break
                    dFlag = True
                else:
                    flag = False
                    break
            i += 1


        if printFlag:
            return tmp
            pass
        elif flag and not dFlag:
            return [0]
        elif flag and dFlag:
            return [1]
        else:
            return [2]

t = int(input())
ans = []
for _ in range(t):
    string = sys.stdin.readline().strip()
    ans.append(solution(string, 0, 0, 0, False))
    
for a in ans:
    if len(a) == 1:
        print(a[0])
    else:
        print(min(a))