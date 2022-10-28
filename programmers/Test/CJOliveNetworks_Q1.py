# Programmers 10/28 2022
# 2022 CJ 올리브네트웍스 Q1

def solution(image):

    for i in image:
        i.extend(i[::-1])

    for i in range(len(image)-1, -1, -1):
        image.append(image[i])

    return image
