class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        self.minimum = float('-inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        elif val > self.mins[-1]:
            self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.mins[-1]
        
