# 오답
import heapq


def search(jobs, time):
    can_list = []
    rest_list = []

    for job in jobs:
        if job[0] <= time:
            can_list.append(job)
        else:
            rest_list.append(job)

    if can_list:
        can_list = sorted(can_list, key=lambda x: x[1])
        return can_list + rest_list
    elif not can_list and rest_list:
        return rest_list
    elif not can_list and not rest_list:
        return False


def solution(jobs):
    # jobs = [[0,3],[1,9],[2,6],[6,8],[7,2]]
    cal_time = []
    works = []
    jobs.sort(key = lambda x : (x[0],x[1]))
    heapq.heapify(jobs)

    while jobs:
        work = heapq.heappop(jobs)
        works.append(work)
        time = work[1]
        jobs = search(jobs, time)

    cur_start_time = 0
    end_time = 0
    for x,y in enumerate(works):
        cur_start_time += x
        processing_time = cur_start_time + y

    print(works)


    # answer = sum(cal_time) // len(cal_time)
    answer = None
    return answer

jobs = [[0, 3], [1, 9], [500, 6]]
jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
jobs = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
jobs = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]

print(solution(jobs))

# # 정답
#
# import heapq
# def solution(jobs):
#     last=-1
#     now=0
#     answer=0
#     wait=[]
#     n=len(jobs)
#     count=0
#
#     while(count<n):
#         for job in jobs:
#             if last <job[0]<=now:
#                 answer+=(now-job[0])
#                 heapq.heappush(wait,job[1])
#
#         print('=====first for loop')
#         print("answer : ", answer)
#         print('wait : ', wait)
#
#         if len(wait)>0:
#             answer+=len(wait)*wait[0]
#             last=now
#             now+=heapq.heappop(wait)
#             count+=1
#         else:
#             now+=1
#
#         print('=====if wait')
#         print('answer : ', answer)
#         print('wait : ', wait)
#         print('now : ', now)
#         print('last : ', last)
#     return answer//n
#
# jobs = [[0, 3], [1, 9], [2, 6]]
# solution(jobs)
# jobs = [[0, 3], [1, 9], [500, 6]]
# jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
# jobs = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
# jobs = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]
# solution(jobs)
#
# print(solution(jobs))

## 이시윤 정답 아름답다

import heapq
from collections import deque

def solution(jobs):
    # jobs = [[0, 3], [1, 9], [2, 6]]
    # jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # a [(3, 0), (6, 2), (9, 1)]
    # tasks deque([(3, 0), (9, 1), (6, 2)])

    # a = sorted([(x[1], x[0]) for x in jobs])

    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0

    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr

        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)