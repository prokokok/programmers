import itertools


# itertools.product([1,2,3], [4,5,6])
def solution(monster, S1, S2, S3):
    s1_list = [x for x in range(1, S1 + 1)]
    s2_list = [x for x in range(1, S2 + 1)]
    s3_list = [x for x in range(1, S3 + 1)]

    dice_sum_count = dict()
    all_permute = list(itertools.product(s1_list, s2_list, s3_list))

    for die in all_permute:
        dice_sum_count[sum(die)] = dice_sum_count.get(sum(die), 0) + 1

    total = sum(dice_sum_count.values())
    counter_mon = 0

    for m in monster:
        counter_mon += dice_sum_count.get(m - 1, 0)

    answer = 1000 * (total - counter_mon) // total

    return answer