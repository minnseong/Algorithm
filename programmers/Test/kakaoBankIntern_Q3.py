# Programmers 11/13 2022
# 2022 카카오뱅크 인턴 코딩 테스트 Q3
# 성공

def solution(rooms):
    answer = 0

    open_rooms = set()

    for room_num in range(len(rooms)):
        if room_num not in open_rooms:
            answer += 1

        while room_num not in open_rooms:
            open_rooms.add(room_num)
            room_num = rooms[room_num] - 1

    return answer-1 if answer != 1 else answer