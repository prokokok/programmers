
def solution(answers):
    pattern_1 = [1 ,2 ,3 ,4 ,5]
    pattern_2 = [2 ,1 ,2 ,3 ,2 ,4 ,2 ,5]
    pattern_3 = [3 ,3 ,1 ,1 ,2 ,2 ,4 ,4 ,5 ,5]

    # 함수로 리팩토링 가능
    quo_len_1 = len(answers) // len(pattern_1)
    mod_len_1 = len(answers) % len(pattern_1)

    quo_len_2 = len(answers) // len(pattern_2)
    mod_len_2 = len(answers) % len(pattern_2)

    quo_len_3 = len(answers) // len(pattern_3)
    mod_len_3 = len(answers) % len(pattern_3)

    answer_1 = pattern_1 * quo_len_1 + pattern_1[:mod_len_1]
    answer_2 = pattern_2 * quo_len_2 + pattern_2[:mod_len_2]
    answer_3 = pattern_3 * quo_len_3 + pattern_3[:mod_len_3]

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0

    for _, answer in enumerate(answers):
        if answer_1[_] == answer:
            cnt_1 += 1
        if answer_2[_] == answer:
            cnt_2 += 1
        if answer_3[_] == answer:
            cnt_3 += 1
    answer_list = [cnt_1 ,cnt_2, cnt_3]
    print(answer_list)
    max_num = max(answer_list)

    final_answer = []
    for index, answer in enumerate(answer_list ,1):
        if max_num == answer:
            final_answer.append(index)

    final_answer.sort()
    return final_answer


## 정답

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result