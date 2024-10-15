class List:

    def __init__(self):
        self.elems = tuple()

    def append(self, x):
        self.elems = self.elems + (x,)

    def pop(self, i=None):
        if i == None:
            i = len(self.elems) - 1
        x = self.elems[i]
        self.elems = self.elems[:i] + self.elems[i + 1:]
        return x

    def __len__(self):
        return len(self.elems)

    def __getitem__(self, i):
        return self.elems[i]

    def __setitem__(self, i, x):
        self.elems = self.elems[:i] + (x,) + self.elems[i + 1:]

    def __str__(self):
        return str(self.elems)

    def __delitem__(self, i):
        self.pop(i)


def test_list():
    l1 = List()
    l1.append(100)
    l1.append(200)
    l1.append(300)
    print(len(l1))
    print(l1)
    print(l1.pop())
    print(len(l1))
    l1.append(1000)
    l1.append(3000)
    l1.append(5000)
    print(l1)
    print(l1.pop(1))
    print(l1)
    print(l1.pop(0))
    print(l1)
    l1[0] = 10000
    print(l1[0])
    print(l1)
    del l1[1]
    print(l1)
    for x in l1:
        print(x)


test_list()
