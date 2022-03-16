class stack:
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, x):
        if not stack:
            self.min.append(x)
        else:
            if x < self.getMin():
                self.min.append(x)
        self.data.append(x)
        return None

    def pop(self):
        val = self.data.poo(-1)
        if self.getMin() == val:
            self.min.pop(-1)

    def top(self):
        if not self.data:
            return None

        return self.data[-1]

    def getMin(self):
        if not self.min:
            return None

        return self.min[-1]