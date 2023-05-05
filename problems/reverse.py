def reversed_array1(data):
    values = []
    for e in data:
        values.append(e)
    res = list(reversed(values))
    return res


print(reversed_array1([1, 4, 7, 9, 98, 54]))


def reversed_array2(data):
    values = []
    for e in data:
        values.append(e)
    res = values[::-1]
    return res


print(reversed_array2([1, 4, 7, 9, 98, 54]))


def reversed_array3(data):
    return [e for e in data][::-1]


print(reversed_array3([1, 4, 7, 9, 98, 54]))


def reversed_array4(data):
    values = list()
    for e in data:
        values.append(e)
    res = []
    while values:
        x = values.pop()
        res.append(x)
    return res


print(reversed_array4([1, 4, 7, 9, 98, 54]))

print()


def reversed_array5(data):
    from collections import deque
    values = deque()
    for e in data:
        values.append(e)
    res = []
    while values:
        res.append(values.pop())
    return res


print(reversed_array5([1, 4, 7, 9, 98, 54]))


class Mystack:
    def __init__(self):
        self.elems = []

    def push(self, e):
        self.elems.append(e)

    def pop(self):
        return self.elems.pop()

    def empty(self):
        return self.size() == 0

    def top(self):
        return self.elems[-1]

    def size(self):
        return len(self.elems)

    def __len__(self):
        return len(self.elems)


'''
assume I have mystack() with following methods push, pop and empty 
'''
print()


def reversed_array6(data):
    values = Mystack()
    print(values.elems)
    for e in data:
        values.push(e)
    res = []
    while not values.empty():
        res.append(values.pop())
    return res


print(reversed_array6([1, 4, 7, 9, 98, 54]))

print()
from collections import deque


class Mystack2:
    def __init__(self):
        self.elems = deque()

    def push(self, e):
        self.elems.append(e)

    def pop(self):
        return self.elems.pop()

    def empty(self):
        return self.size() == 0

    def top(self):
        return self.elems[-1]

    def size(self):
        return len(self.elems)


def reversed_array7(values):
    array = Mystack2()
    for value in values:
        array.push(value)
    res = []
    while not array.empty():
        res.append(array.pop())
    return res


print(reversed_array7([1, 4, 7, 9, 98, 54]))

mystack = Mystack()
mystack.push(100)
mystack.push(200)
print(mystack.size())
print(len(mystack))
