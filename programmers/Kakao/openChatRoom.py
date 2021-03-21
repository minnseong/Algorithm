# Programmers 03/21 2021
# 오픈채팅방

def solution(record):
    answer = []
    user = {}
    action = []

    for i in record:
        splitRecord = i.split(" ")
        if splitRecord[0] == "Enter":
            user[splitRecord[1]] = splitRecord[2]
            action.append(splitRecord[1] + "님이 들어왔습니다.")
        elif splitRecord[0] == "Leave":
            action.append(splitRecord[1] + "님이 나갔습니다.")
        elif splitRecord[0] == "Change":
            user[splitRecord[1]] = splitRecord[2]
    print(action)

    for i in action:
        for key in user:
            if key in i:
                answer.append(i.replace(key, user[key]))

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))