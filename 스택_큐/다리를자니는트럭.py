# M1
def solution(bridge_length, weight, truck_weights):

    number_trucks = len(truck_weights)
    passed = []
    bridge_queue = [0] * bridge_length

    cnt = 0
    ti = 0
    index = 0
    weight_sum = 0

    while len(passed) < number_trucks:

        if ti > number_trucks - 1:
            next_bus = 0
        else:
            next_bus = truck_weights[ti]

        if bridge_queue[index] != 0:
            passed.append(bridge_queue[index])
            weight_sum -= bridge_queue[index]
        index += 1

        if weight_sum + next_bus <= weight:
            bridge_queue.append(next_bus)
            weight_sum += next_bus
            ti += 1
        else:
            bridge_queue.append(0)
        cnt += 1

    answer = cnt
    return answer

###

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()