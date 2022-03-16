from collections import deque

class stack:
    def __init__(self):
        self.q = deque()

    def push(x):
        self.q.append(x)
        q_len = len(self.q)

        while q_len > 1:
            self.q.append(self.q.popleft())
            q_len -= 1

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0