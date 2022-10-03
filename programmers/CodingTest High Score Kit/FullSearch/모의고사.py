def solution(answers):
    
    ans = []
    
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score_1, score_2, score_3 = 0, 0, 0
    
    for i in range(len(answers)):
        if person_1[i % len(person_1)] == answers[i]:
            score_1 += 1
        if person_2[i % len(person_2)] == answers[i]:
            score_2 += 1
        if person_3[i % len(person_3)] == answers[i]:
            score_3 += 1
    
    max_score = max(score_1, score_2, score_3)
    
    for idx, s in enumerate([score_1, score_2, score_3]):
        if s == max_score:
            ans.append(idx+1)
            
    return ans