def solution(genres, plays):
    # 장르 별 총 재생 횟수가 정리되어 있는 list : genres_all_dict
    genres_all_dict = dict()
    # 장르별로 노래별 재생 횟수가 정리되어 있는 리스트 : genres_play_dict
    genres_play_dict = dict()
    for i, genre in enumerate(genres):
        if genre not in genres_all_dict:
            genres_all_dict[genre] = plays[i]
        else:
            genres_all_dict[genre] += plays[i]
            
        if genre not in genres_play_dict:
            genres_play_dict[genre] = [(i,plays[i])]
        else:
            genres_play_dict[genre].append((i,plays[i]))
    genres_all_dict = sorted(genres_all_dict.items(), key=lambda x: x[1],reverse = True)
    answer = []
    for genre in genres_all_dict:
        genre = genre[0]
        genres_play_dict[genre] = sorted(genres_play_dict[genre], key=lambda x:(x[1], -x[0]),reverse = True)
        if len(genres_play_dict[genre]) < 2:
            answer.append(genres_play_dict[genre][0][0])
        else:
            answer.append(genres_play_dict[genre][0][0])
            answer.append(genres_play_dict[genre][1][0])
    return answer

