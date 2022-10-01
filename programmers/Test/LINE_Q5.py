def solution(abilities, k):

    result = 0

    if len(abilities) & 1:
        abilities.append(0)

    abilities.sort(reverse=True)

    diff = []
    for i in range(0, len(abilities), 2):
        diff.append([i//2+1, abs(abilities[i+1]-abilities[i])])

    diff.sort(key=lambda x: -x[1])


    select_round = set()
    for idx in range(k):
        select_round.add(diff[idx][0])

    for i in range(0, len(abilities), 2):
        if i//2+1 in select_round:
            result += abilities[i]
        else:
            result += abilities[i+1]

    return result

print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))
print(solution([7, 6, 8, 9, 10], 1))