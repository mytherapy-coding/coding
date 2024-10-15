'''
import collections


class ArrStack:
    def __init__(self, seq=None):
        self.elems = []
        if seq:
            for x in seq:
                self.push(x)

    def push(self, x):
        self.elems.append(x)

    def pop(self):
        return self.elems.pop()

    def __len__(self) -> int:
        return len(self.elems)

    def top(self):
        return self.elems[-1]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.elems})'

    def __getitem__(self, index):
        return self.elems[index]

    def __setitem__(self, index, value):
        self.elems[index] = value

    def __eq__(self, other):
        return self.elems == other.elems

    def __contains__(self, item):
        return item in self.elems


container = ArrStack([10, 20, 30])
if 30 in container:
    print("We found it")
else:
    print("We did't find it")
if container:
    print(f'container is not empty')
else:
    print(f'empty')

container.push(10)
container.push(20)
container.push(30)
print(str(container))
print(len(container))
print(container[0])
container[0] = 1000
print(container)
print()
busket = ArrStack()
busket.push(1000)
busket.push(20)
busket.push(30)
print(busket)
print(busket == container)
print()

if container:
    print(f'container is not empty')
else:
    print(f'empty')
container.pop()
container.pop()
container.pop()
if container:
    print(f'container is not empty')
else:
    print(f'empty')

print('__________________')


class DequeStack:
    def __init__(self, seq=None):
        self.elems = collections.deque()
        if seq:
            for x in seq:
                self.push(x)

    def push(self, x):
        self.elems.append(x)

    def pop(self):
        return self.elems.pop()

    def __len__(self) -> int:
        return len(self.elems)

    def top(self):
        return self.elems[-1]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.elems})'

    def __getitem__(self, index):
        return self.elems[index]

    def __setitem__(self, index, value):
        self.elems[index] = value

    def __eq__(self, other):
        return self.elems == other.elems


container = DequeStack([10, 20, 30])
if container:
    print(f'container is not empty')
else:
    print(f'empty')

container.push(10)
container.push(20)
container.push(30)
print(str(container))
print(len(container))
print(container[0])
container[0] = 1000
print(container)
print()
busket = DequeStack("hello")
busket.push(1000)
busket.push(20)
busket.push(30)
print(busket)
print(busket == container)
print()

if container:
    print(f'container is not empty')
else:
    print(f'empty')
container.pop()
container.pop()
container.pop()
if container:
    print(f'container is not empty')
else:
    print(f'empty')

print("================")

print(list('hello'))
print(ArrStack("hello"))
print(list(range(10)))
print(ArrStack(range(10)))
print(ArrStack(DequeStack(list(range(10)))))
print(list(ArrStack(DequeStack(list('hello')))))
print(":".join(ArrStack(DequeStack(list('hello')))))
stack = ArrStack([10, 20, 30])
for x in stack:
    print(x)
while stack:
    print(stack.pop())
'''

class Stack:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __bool__(self):
        return bool(self.items)


my_stack = Stack()
my_stack.append(1)
my_stack.append(2)
print(bool(my_stack))  # Output: True
print(my_stack.pop())  # Output: 2
print(my_stack.pop())  # Output: 1
print(bool(my_stack))  # Output: False

phrase = 'Giraffe Academy'
print(phrase[0])

