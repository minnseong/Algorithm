from itertools import combinations

def solution(sentence, n):
    
    result = 0
    possible_key = dict()
    keys = set()

    for s in sentence:
        tmp = set()
        for key in set(list(s)):
            if key == " ":
                continue
            elif 65 <= ord(key) <= 90:
                tmp.add("shift")
                tmp.add(key.lower())
            else:
                tmp.add(key)
        possible_key[s] = tmp
        keys.update(tmp)

    score_dic = dict()
    for st in sentence:
        score = 0
        for s in st:
            if 65 <= ord(s) <= 90:
                score += 2
            else:
                score += 1
        score_dic[st] = score

    for combi in set(combinations(keys, n)):
        score = 0
        for k, v in possible_key.items():
            if set(combi) & set(v) == set(v):
                score += score_dic[k]
        result = max(score, result)

    return result


print(solution(["line in line", "LINE", "in lion"], 5))
print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))
