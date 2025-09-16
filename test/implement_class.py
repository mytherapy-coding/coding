"""
Implement the following class:

class SumMinStack:
    def __init__(self) -> None:

    def push(self, val: float) -> None:

    def pop(self) -> None:

    def last(self, default: float = None) -> float:

    def sum(self) -> float:

    def min(self, default: float = None) -> float:

    def __len__(self) -> int:

    def __str__(self) -> str:

    def __repr__(self) -> str:


The following code must work:


stack: SumMinStack = SumMinStack()

print(stack.last(), stack.sum(), stack.min(), len(stack))

stack.push(5)
stack.push(10)
stack.push(7)

print(stack.last(), stack.sum(), stack.min(), len(stack))

stack.push(10)
stack.push(20)

print(stack.last(), stack.sum(), stack.min(), len(stack))

stack.pop()

print(stack.last(), stack.sum(), stack.min(), len(stack))

print(f'{stack}')


Output:

None 0 None 0
7 22 5 3
20 52 5 5
10 32 5 4
SumMinStack[5, 10, 7, 10]

The time complexity of all operations except for __str__ and __repr__ must be O(1).
"""
