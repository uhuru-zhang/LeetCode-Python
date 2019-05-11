class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) > 0:
            self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)

        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) < 0:
            return None
        result = self.stack.pop()
        self.stack.pop()

        return result

    def top(self) -> int:

        if len(self.stack) < 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:

        if len(self.stack) < 0:
            return None
        return self.stack[-2]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
