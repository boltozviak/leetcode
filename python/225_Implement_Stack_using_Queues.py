class MyStack:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        while len(self.first) != 1:
            self.second.append(self.first.pop(0))
        z = self.first.pop(0)
        self.first, self.second = self.second, self.first
        return z

    def top(self) -> int:
        while self.first:
            self.second.append(self.first.pop(0))
        z = self.second[-1]
        self.first, self.second = self.second, self.first
        return z

    def empty(self) -> bool:
        return len(self.first) == 0
