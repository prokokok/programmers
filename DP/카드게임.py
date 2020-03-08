#카드 게임
import heapq

def solution(left, right):


    left = [-l for l in left]
    right = [-r for r in right]

    heapq.heapify(left)
    heapq.heapify(right)

    cnt = 0
    index = 0
    while left and right:
        # print(index)
        # print(right)
        # print(left)
        # print(cnt)
        # index+=1
        # print('===')

        # right가 left 보다 작을 경우
        if -right[0] < -left[0]:
            cnt += -1 * heapq.heappop(right)

        # right left 같을 경우
        elif -right[0] == -left[0]:
            heapq.heappop(right)

        # right가 left 보다 클경우
        elif -right[0] > -left[0]:
            # left.pop()
            # break
            heapq.heappop(right)

    print(cnt)
    return cnt

if __name__ == "__main__":
    # left = [1, 2, 2]
    # right = [1, 1, 1]

    left = [1,1,1]
    right = [1,1,1]
    solution(left, right)