class MinStack:

    def __init__(self):
        self.stack = []
        self.size = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.size) == 0:
            self.size.append(val)
        else:
            self.size.append(min(self.size[-1], val))

    def pop(self) -> None:
        self.stack.pop(-1)
        self.size.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.size[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()