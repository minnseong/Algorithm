def solution(infos, m):

    use_car = 0
    for info in infos:
        use_car += info[0]

    use_bike = 0
    i = 0
    while i < len(infos):
        if infos[i][1] <= infos[i][3]:
            use_bike += infos[i][1]
            i += 1
        else:
            walk = 0
            while infos[i][1] > infos[i][3] and walk + infos[i][3] <= m:
                walk += infos[i][3]
                i += 1
            use_bike += (walk + infos[i][1])
            i += 1

    use_public = 0
    i = 0
    while i < len(infos):
        if infos[i][2] == -1 and infos[i][3] > m:
            use_public = 1e9
            break

        if infos[i][2] != -1 and infos[i][2] <= infos[i][3]:
            use_public += infos[i][2]
            i += 1
        else:
            walk = 0
            public = 0
            exit_flag = False
            not_walk_flag = False
            while infos[i][2] == -1 or (infos[i][2] > infos[i][3] and walk + infos[i][3] <= m):
                if infos[i][2] == -1:
                    if infos[i][3] > m:
                        use_public = 1e9
                        exit_flag = True
                        break
                    if (walk + infos[i][3]) > m:
                        not_walk_flag = True
                        break
                public += infos[i][2]
                walk += infos[i][3]
                i += 1
            if exit_flag:
                break

            if not_walk_flag:
                use_public += (public + infos[i][3])
            else:
                use_public += (walk + infos[i][2])
            i += 1

    use_walk = 0
    for info in infos:
        use_walk += info[3]
        if use_walk > m:
            use_walk = 1e9
            break

    answer = min(use_car, use_bike, use_public, use_walk)
    return answer
