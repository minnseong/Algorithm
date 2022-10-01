def q1(logs):
    ans = 0
    lg = ["team_name", "application_name", "error_level", "message"]

    for l in logs:
        if len(l) >= 100:
            continue
        l_split = l.split(" ")
        print(l_split)
        if len(l_split) != 12:
            continue
        else:
            cnt = 0
            idx = 0
            for i in [2,5,8,11]:
                if l_split[i-2] == lg[idx] and l_split[i].isalpha():
                    cnt += 1
                else:
                    break
                idx += 1
            if cnt == 4:
                ans += 1

    return len(logs) - ans

print(q1(["team_name : db application_name : dbtest error_level : info message : test",
                "team_name : test application_name : I DONT CARE error_level: error message : x",
                "team_name : ThislsJustForTest application_name : TestAndTestAndTestAndTest error _level: test message : lAlwaysTestingAndIWillTestForever",
                "team_name :oberervability application_name : LogViewer error_level : error"]))
print(q1(["team_name: MyTeam application_name : YourApp error_level : info messag :IndexOutOfRange",
                "no such file or directory",
                "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11",
                "team_name : recommend application_name : recommend error_level : info message : Success!",
                " team_name : db application_name : dbtest error_level : info message : test",
                "team_name  : db application_name : dbtest error_level : info message : test",
                "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))
