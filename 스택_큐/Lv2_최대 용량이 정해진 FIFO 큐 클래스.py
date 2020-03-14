class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        if self.qsize() < self.max_size:
            self.stack1.push(item)
            return True
        else:
            return False

    def pop(self):
        if self.stack2.size() == 0:
            if self.stack1.size() == 0:
                return False
            else:
                while self.stack1.size() != 0:
                    self.stack2.push(self.stack1.pop())
                return self.stack2.pop()
        else:
            return self.stack2.pop()


n, max_size = map(int, input().strip().split(' '))
a = MyQueue(max_size)

while n:
    n -= 1
    cmd = str(input().strip())

    if 'PUSH' in cmd:
        # 1) 다른 변수를 선언하지 않고, 2) cmd.split(' ')를 두번 호출하지 않고 표현 하는 방법이 있을까요?
        q_method, num_push = cmd.split(' ')[0].lower(), int(cmd.split(' ')[1])
        print(getattr(a, q_method)(num_push))
    else:
        q_method = cmd.lower()
        if q_method == 'size':
            q_method = 'qsize'
        print(getattr(a, q_method)())