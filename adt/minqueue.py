class MinQeue0:
    def __init__(self, seq=()):
        self.items = []
        self.extend(seq)

    def extend(self, iterable):
        self.items.extend(iterable)

    def add(self, x):
        self.items.append(x)

    def get_min(self):
        return min(self.items)

    def remove_min(self):
        min_item = self.get_min()
        self.items.remove(min_item)
        return min_item

    def __repr__(self):
        return f'{type(self).__qualname__}({self.items})'

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self:
            raise StopIteration()
        return self.remove_min()

class MinQeue1:
    def __init__(self, seq=()):
        self.items = []
        self.min_item = None
        self.extend(seq)

    def extend(self, iterable):
        self.items.extend(iterable)
        self.min_item = min(self.items, default=None)

    def add(self, x):
        self.items.append(x)
        if self.min_item is None or x < self.min_item:
            self.min_item = x

    def get_min(self):
        if not self.items:
            raise ValueError("the container is empty")
        return self.min_item

    def remove_min(self):
        min_item = self.get_min()
        self.items.remove(min_item)
        self.min_item = min(self.items, default=None)
        return min_item

    def __repr__(self):
        return f'{type(self).__qualname__}({self.items})'

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self:
            raise StopIteration()
        return self.remove_min()


class MinQeue2:
    def __init__(self, seq=()):
        self.items = []
        self.extend(seq)

    def extend(self, iterable):
        self.items.extend(iterable)
        self.items.sort(reverse=True)

    def add(self, x):
        self.items.append(x)
        self.items.sort(reverse=True)

    def get_min(self):
        return self.items[-1]

    def remove_min(self):
        return self.items.pop()

    def __repr__(self):
        return f'{type(self).__qualname__}({self.items})'

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self:
            raise StopIteration()
        return self.remove_min()


import heapq


class MinQueue3:
    def __init__(self, seq):
        self.items = []
        self.extend(seq)

    def extend(self, iterable):
        self.items.extend(iterable)
        heapq.heapify(self.items)


    def add(self, x):
        heapq.heappush(self.items, x)

    def get_min(self):
        return self.items[0]

    def remove_min(self):
        return heapq.heappop(self.items)

    def __repr__(self):
        return f'{type(self).__qualname__}({self.items})'

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self:
            raise StopIteration()
        return self.remove_min()


def mysorted(values, mkqueue=MinQeue0):
    my_queue = MinQeue0(values)
    res = []
    while my_queue:
        res.append(my_queue.remove_min())
    return res


def test():
    for min_queue in MinQeue0, MinQeue1, MinQeue2, MinQueue3:
        que = min_queue([20, 10, 30, 20])
        print('queue: ', que)
        for _ in range(2):
            print('get:   ', que.get_min())
            print('remove:', que.remove_min())
        que.add(5)
        print('queue: ', que)
        print('get:   ', que.get_min())
        for _ in range(3):
            print('remove:', que.remove_min())

        print()

def test1():
    values = [70,50,30]
    expected = sorted(values)
    print(expected)
    print()
    for min_queue in MinQeue0, MinQeue1, MinQeue2, MinQueue3:
        print(mysorted(values, min_queue))






test()
print()
test1()

