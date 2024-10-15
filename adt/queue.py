import collections


class ArrQueue:
    def __init__(self, seq=None):
        self.elems = []
        if seq:
            for x in seq:
                self.enqueue(x)

    def enqueue(self, x):
        self.elems.append(x)

    def dequeue(self):
        return self.elems.pop(0)

    def __len__(self) -> int:
        return len(self.elems)

    def head(self):
        return self.elems[0]

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


class DequeQueue:
    def __init__(self, seq=None):
        self.elems = collections.deque()
        if seq:
            for x in seq:
                self.enqueue(x)

    def enqueue(self, x):
        self.elems.append(x)

    def dequeue(self):
        return self.elems.popleft()

    def __len__(self) -> int:
        return len(self.elems)

    def head(self):
        return self.elems[0]

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


class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedListQueue:
    def __init__(self, seq=None):
        self.tail: Node | None = None
        self.head: Node | None = None
        self.count: int = 0
        if seq:
            for x in seq:
                self.enqueue(x)

    def enqueue(self, x):
        self.count += 1
        if self.tail is None:
            cur = Node()
            cur.value = x
            self.tail = cur
            self.head = cur
            return
        cur = Node()
        cur.value = x
        cur.prev = self.tail
        self.tail.next = cur
        self.tail = cur

    def dequeue(self):
        value = self.first()
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.count -= 1

        return value

    def __len__(self) -> int:
        return self.count

    def first(self):
        return self.head.value

    def __repr__(self):
        cur = self.head
        res = []
        while cur:
            res.append(cur.value)
            cur = cur.next
        return f'{self.__class__.__name__}({res})'

    def _get_node(self, index: int):
        if index >= len(self) or index < 0:
            raise IndexError(f"invalid {index=}")
        if index < len(self) // 2:
            cur = self.head
            cur_index = 0
            while cur and cur_index < index:
                cur = cur.next
                cur_index += 1
        else:
            cur = self.tail
            cur_index = len(self) - 1
            while cur and cur_index > index:
                cur = cur.prev
                cur_index -= 1
        return cur

    def __getitem__(self, index: int):
        return self._get_node(index).value

    def __setitem__(self, index, value):
        self._get_node(index).value = value

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        cur0 = self.head
        cur1 = other.head
        while cur0 and cur1:
            cur0 = cur0.next
            cur1 = cur1.next
            if cur0.value != cur1.value:
                return False
        return True

    def __contains__(self, item):
        cur = self.head
        while cur:
            if cur.value == item:
                return True
            cur = cur.next
        return False

    def __iter__(self):






def test_queue():
    queue = LinkedListQueue(range(1001))
    it = iter(queue)
    print(len(queue))
    print(queue[1000])
    sum1 = sum(queue)

    sum2 = 0
    for i in range(len(queue)):
        sum2 += queue[i]
    print(sum2)

    s = []
    for x in queue:
        s.append(x)

    sum3 = sum(s)
    print(sum3)

    sum4 = sum(x for x in queue)
    print(sum4)

    sum5 = 0
    while queue:
        removed = queue.dequeue()
        sum5 += removed
    print(sum5)
    print(len(queue))
    sum0 = sum(range(1001))
    print(sum0, sum1, sum2, sum3, sum4, sum5)


test_queue()
