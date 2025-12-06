class MyQueue:
    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)
        
    def pop(self) -> int:
        while len(self.first) != 1:
            self.second.append(self.first.pop())
        z = self.first.pop()
        while len(self.second) != 0:
            self.first.append(self.second.pop())
        return z
  
    def peek(self) -> int:
        while self.first:
            self.second.append(self.first.pop())
        z = self.second[-1]
        while len(self.second) != 0:
            self.first.append(self.second.pop())
        return z

    def empty(self) -> bool:
        return len(self.first) == 0
