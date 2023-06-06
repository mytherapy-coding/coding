class MinStack:
    def __init__(self):
        self.items = []
        self.minvals = []

    def push(self, val: int) -> None:
        self.items.append(val)  # [1, 4]
        if self.minvals:
            self.minvals.append(min(self.minvals[-1], val))
        else:
            self.minvals.append(val)

    def pop(self) -> None:
        self.items.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minvals[-1]

