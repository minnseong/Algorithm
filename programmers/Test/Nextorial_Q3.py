# 넥토리얼 코딩테스트 10/07 2022
# Q3 - 100

from bisect import bisect_left

def getMinimumHealth(initial_players, new_players, rank):

    health = 0
    initial_players.sort()

    opponent = initial_players[len(initial_players)-rank]
    health += opponent
    for np in new_players:
        initial_players.insert(bisect_left(initial_players, np), np)
        health += initial_players[len(initial_players)-rank]

    return health

print(getMinimumHealth([1,1,3], [2,2,4], 2))
print(getMinimumHealth([1,2,3], [6,5,4], 1))