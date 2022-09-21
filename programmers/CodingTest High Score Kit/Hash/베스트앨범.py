# Programmers 09/21 2022
# Level 3 - 베스트앨범

from collections import defaultdict

def solution(genres, plays):
    
    album = []
    
    genreCnt_dict = defaultdict(int)
    album_dict = defaultdict(list)
    
    idx = 0
    for genre, play in zip(genres, plays):
        album_dict[genre].append([idx, play])
        genreCnt_dict[genre] += play
        idx += 1
    
    for key, value in sorted(genreCnt_dict.items(), key=lambda item: -item[1]):
        sorted_dict = sorted(album_dict[key], key=lambda x : (-x[1], x[0]))
        if len(sorted_dict) == 1:
            album.append(sorted_dict[0][0])
        else:
            album.append(sorted_dict[0][0])
            album.append(sorted_dict[1][0])
            
        
    return album