from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    data: any
    next: "Node" = None


def appendleft(head: Node, value: any) -> Node:
    return Node(value, head)


def sum_of(head: Node) -> int:
    return head.data + sum_of(head.next) if head else 0


def popleft(head: Node) -> Node:
    return head.next


def updateleft(head: Node, value) -> Node:
    head = popleft(head)
    head = appendleft(head, value)
    return head


def append(head: Node, data: int) -> Node:
    return Node(head.data, append(head.next, data)) if head else Node(data)


def pop(head: Node) -> Node:
    return Node(head.data, pop(head.next)) if head.next else None


def generate(head: Node):
    if not head:
        return
    for value in generate(head.next):
        yield value
    yield head.data


def yield_all(head: Node):
    while head:
        yield head.data
        head = head.next


def map_to(head: Node, f) -> Node:
    return Node(f(head.data), map_to(head.next)) if head else None


def filter_all(head: Node, p) -> Node:
    if not head:
        return None
    tail = filter_all(head.next, p)
    if p(head.data):
        tail = appendleft(tail, head.data)
    return tail


def reduce_to(head: Node, f) -> Node:
    acc = head.data
    head = head.next
    while head:
        acc = f(acc, head.data)
    return acc


head = None
for value in range(1000, 6000, 1000):
    head = appendleft(value, head)
head = appendleft(head, 0)
print(head)

from collections import deque

my_deque = deque([1000, 2000, 3000, 4000, 5000])
my_deque.appendleft(0)
print(my_deque)


def updateleft1(head: Node, value) -> Node:
    return appendleft(popleft(head), value)


def appendleft_from(head: Node, iterable) -> Node:
    for value in iterable:
        head = appendleft(head, value)
    return head


print(appendleft_from(head, [1, 2, 3]))

head = None
for value in range(1000, 6000, 1000):
    head = Node(value, head)
head = Node(0, head)


def reverse_all(head: Node) -> Node:
    res = None
    while head:
        res = appendleft(res, head.data)
        head = head.next
    return res


print()
print(reverse_all(head))


def print0(node: Node) -> Node:
    while node:
        print(node.data)
        node = node.next


print("linked list recursion")

head = None
for value in range(0, 50, 10):
    head = Node(value, head)

print("#print")


def print1(head: Node) -> Node:
    if head is None:
        return
    print(head.data)
    print1(head.next)


print1(head)
head = popleft(head)
print1(head)
head = appendleft(head, 1000)
head = appendleft(head, 1000)
head = appendleft(head, 1000)
head = popleft(head)
print1(head)
head = updateleft(head, 2000)
print1(head)
print(head)

print("-------")


def remove(head: Node, x: any) -> Node:
    if head is None:
        return None
    if head.data == x:
        return head.next
    tail = remove(head.next, x)
    # if tail == head.next:
    # return head
    return Node(head.data, tail)


res = remove(head, 70)

print1(remove(head, 70))


def dup(head: Node) -> Node:
    if head is None:
        return None
    return appendleft(appendleft(dup(head.next), head.data), head.data)


print1(dup(head))


def map_to(f, head: Node) -> Node:
    if not head:
        return None
    tail = map_to(f, head.next)
    head = appendleft(tail, f(head.data))
    return head


print("map_to")
print1(map_to(lambda x: 2 * x, head))


def filter_it(p, head: Node) -> Node:
    if not head:
        return None
    tail = filter_it(p, head.next)
    if p(head.data):
        return appendleft(tail, head.data)
    return tail


print("filter")

print1(filter_it(lambda x: x >= 1000, head))


def size(head: Node) -> int:
    if not head:
        return 0
    tail_size = size(head.next)
    return tail_size + 1


print(size(head))


def sum_node(head: Node) -> int:
    if not head:
        return 0
    tail = sum_node(head.next)
    return tail + head.data


print(sum_node(head))


def reduce(f, head: Node, initial: any = None) -> any:
    if not head:
        return initial
    if not head.next:
        if initial:
            return f(initial, head.data)
        return head.data
    tail = reduce(f, head.next)
    return f(tail, head.data)


print("reduce")
print(reduce(lambda x, y: x + y, head))

print("reduce1")
print(reduce(max, head))

print("reduce2")
print(reduce(lambda x, y: x * y, remove(head, 0)))

print("reduce3")
print(reduce(lambda x, y: x + y, map_to(str, head)))


def pop(head: Node) -> Node:
    if not head.next:
        return None
    tail = pop(head.next)
    return Node(head.data, tail)


print("pop")
print1(pop(head))

"""
accumulate_it
merge
remove_all
concatenate
merge_sorted
def skip_k(head: Node, k: int) -> Node
def take_k(head: Node, k: int) -> Node
def slice(head: Node, beg: int, end: int) -> Node
def zig_zag(head1, head2) -> Node
Один node первого списка, потом со второго и т.д
def reverse_it(head) -> Node
def chain(head1, head2) -> Node

Это concatenation.
def merge_ordered(head1, head2) -> Node
def accumulate(f, head) -> Node
def appendleft_from(head, iterable) -> Node
def append_from(head, iterable) -> Node
def yield_all(head)
"""


def accumulate_it(head: Node, f, initial: any = None) -> Node:
    if not head:
        return initial
    if not head.next:
        if initial:
            return f(initial, head.data)
    tail = accumulate_it(head.next, f)
    return f(tail, head.data)


"""
print("accumulate")
print1(accumulate_it(head, lambda x, y: x + y))
"""
