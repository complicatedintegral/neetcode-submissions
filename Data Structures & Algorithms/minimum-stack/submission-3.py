class MinStack:

    def __init__(self):
        self.MinStack = list()
        self.m = [] # second stack to track minimum value in the main stack
    def push(self, val: int) -> None:
        self.MinStack.append(val)
        if self.m:
            self.m.append(min(self.m[-1], val))
        else:
            self.m.append(val)

        # print(self.MinStack)
        # print(self.m)

    def pop(self) -> None:
        self.MinStack.pop()
        self.m.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.m[-1]
