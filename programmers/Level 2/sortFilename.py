# Programmers 02/08 2022
# 파일명 정렬

def solution(files):
    answer = []

    fileList = []

    for f in files:
        file = ["", "", ""]
        prvIdx = 0
        for idx, val in enumerate(f):
            if val.isdigit():
                if prvIdx == 0:
                    file[0] = f[:idx]
                    prvIdx = idx
                elif idx-prvIdx == 1:
                    prvIdx = idx
                else:
                    break
        file[1] = f[len(file[0]):prvIdx+1]
        file[2] = f[prvIdx+1:]
        fileList.append(file)

    fileList.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    for f in fileList:
        answer.append(''.join(f))

    return answer

print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
