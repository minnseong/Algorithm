# BaekJoon 01/25 2021
# 1316번 그룹 단어 체커

input_num = int(input())
answer = 0
word_list = []

for i in range(0, input_num):
    word_list.append(input())

# aabbcc   0~5
for word in word_list:
    cnt = 0
    for j in range(0, len(word)-1):
        if word[j] != word[j+1]:
            re_word = word[j+1:]
            if re_word.count(word[j]) != 0:
                cnt += 1
    if cnt == 0:
        answer += 1

print(count)