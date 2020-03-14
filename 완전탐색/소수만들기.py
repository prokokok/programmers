import itertools

def check_prime(x):
    upper_bound = int(x**(0.5))+1
    for i in range(2,upper_bound + 1):
        if x % i == 0:
            return 0
    return 1

def solution(nums):

    # itertools.combinations를 활용 모든 경우의 수를 도출
    # map 을 활용 모두 경우의 수를 sum 하고 소수 check
    # sum 을 활용 갯수 도출
    return sum(map(lambda x: check_prime(sum(x)), itertools.combinations(nums,3)))