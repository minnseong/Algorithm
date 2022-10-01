from collections import defaultdict

def solution(num_teams, remote_tasks, office_tasks, employees):
    result = []

    members_office_mb = set()
    teams = defaultdict(set)

    set_office_tasks = set(office_tasks)

    for idx, info in enumerate(list(employees)):
        cnt = 0
        info_list = info.split(" ")
        for i in range(len(info_list)):
            if i == 0:
                teams[info_list[i]].add(idx+1)
            elif info_list[i] in set_office_tasks:
                members_office_mb.add(idx+1)
                break

    print(members_office_mb)
    print(teams)
    
    for k, v in teams.items():
        if len(v & members_office_mb) >= 1:
            continue
        else:
            members_office_mb.add(min(v))
    
    for i in range(1, len(employees)+1):
        if i not in members_office_mb:
            result.append(i)
    return result

print(solution(3, ["development", "marketing", "hometask"],
               ["recruitment", "education", "officetask"],
               ["1 development hometask", "1 recruitment marketing",
                "2 hometask", "2 development marketing hometask",
                "3 marketing", "3 officetask", "3 development"]))

print(solution(2, ["design"], ["[building", "supervise"],
               ["2 design", "1 supervise building design", "1 design", "2 design"]))