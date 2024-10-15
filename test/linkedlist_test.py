from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    data: any
    next: 'Node' = None

    def __len__(self):
        head: Node = self
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

    def __iter__(self):
        def gen(head: Node):
            while head is not None:
                yield head.data
                head = head.next
        return gen(self)
head = Node(100, Node(200, Node(300, Node(400, Node(500)))))


def test():

    for e in enumerate(head):
        print(e)

    print(list(enumerate(head)))


    for e in enumerate(head):
        print(e)

    head = Node(100, Node(200, Node(300, Node(400, Node(500)))))
    print(head)
    head = Node(1000, head)

    for i in range(10):
        head = Node(i, head)


    print(head)
    print(list(head))
    print(len(list(head)))
    print(len(head))

    print("iterator")
    for e in head:
        print(e)
    print(list(head))
    print([e for e in head])

    if 200 in (e for e in head):
        print("found")
    print((e for e in head))


test()


