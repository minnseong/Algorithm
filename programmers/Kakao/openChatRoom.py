# Programmers 03/21 2021
# KaKao 오픈채팅방

def solution(record):
    answer = []
    user = {}
    action = []
    id = []

    for i in record:
        splitRecord = i.split(" ")

        if splitRecord[0] == "Enter":
            user[splitRecord[1]] = splitRecord[2]
            id.append(splitRecord[1])
            action.append("님이 들어왔습니다.")

        if splitRecord[0] == "Leave":
            id.append(splitRecord[1])
            action.append("님이 나갔습니다.")

        if splitRecord[0] == "Change":
            user[splitRecord[1]] = splitRecord[2]

    for i in range(len(action)):
        answer.append(user[id[i]] + action[i])

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))