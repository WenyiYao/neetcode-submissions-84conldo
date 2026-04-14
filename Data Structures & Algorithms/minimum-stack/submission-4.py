class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp = []
        mini = self.stack[-1]

        while self.stack:
            mini = min(self.stack[-1],mini)
            temp.append(self.stack.pop()) # temp + 1
        
        while temp:
            self.stack.append(temp.pop()) # stack + 1
        
        return mini



