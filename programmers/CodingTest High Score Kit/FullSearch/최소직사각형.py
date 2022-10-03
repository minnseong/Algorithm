def solution(sizes):
    
    size_1 = []
    size_2 = []
    
    for i in range(len(sizes)):
        sizes[i].sort()
        size_1.append(sizes[i][0])
        size_2.append(sizes[i][1])
    
    return max(size_1) * max(size_2)