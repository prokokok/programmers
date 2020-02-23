def solution(genres, plays):
    genre_dic = {}

    # genres = ['classic','pop','classic','classic']
    # plays = [100,300,200,200]

    for _, i in enumerate(genres):
        # print(_,i,plays[_])

        genre_dic.setdefault(i, {})
        genre_dic[i][_] = plays[_]

    print(genre_dic)

    genre_list = []
    total_list = []

    for key_value in genre_dic:
        genre_list.append(key_value)
        total = 0
        # print(key_value)
        for num_play in genre_dic[key_value].items():
            total += num_play[1]
        total_list.append(total)

    sorted_genre_list = [x for _, x in sorted(zip(total_list, genre_list), reverse=True)]
    # print(sorted_genre_list)

    list_index = []
    for genre in sorted_genre_list:

        # print(list(genre_dic[genre].keys())[0])
        # print(genre)
        if len(genre_dic[genre].keys()) == 1:
            list_index.append(list(genre_dic[genre].keys())[0])
        else:
            index_list = []
            value_list = []
            for index, value in genre_dic[genre].items():
                index_list.append(index)
                value_list.append(value)
            # print(index_list)
            # print(value_list)
            sorted_index_list = [x for _, x in sorted(zip(value_list, index_list), reverse=True)]

            first_index = sorted_index_list[0]
            second_index = sorted_index_list[1]

            if plays[first_index] == plays[second_index] and first_index > second_index:
                first_index, second_index = second_index, first_index

            list_index.append(first_index)
            list_index.append(second_index)
    # print(list_index)

    # answer = list_index

    answer = list_index
    return answer

#######

def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer