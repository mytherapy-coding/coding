class MaxStack:
    def __init__(self, iterable=None):
        self.elems = []
        self.max_values = []
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, x):
        self.elems.append(x)
        if not self.max_values:
            self.max_values.append(x)
        else:
            self.max_values.append(max(x, self.max_values[-1]))

    def pop(self):
        if not self.elems:
            raise IndexError("pop from empty stack")
        self.max_values.pop()
        return self.elems.pop()

    def __len__(self):
        return len(self.elems)

    def __bool__(self):
        return bool(self.elems)

    def __iter__(self):
        return iter(self.elems)

    def __repr__(self):
        return f"MaxStack({self.elems})"

    @property
    def max(self):
        if not self.max_values:
            raise ValueError("max from empty stack")
        return self.max_values[-1]


class SumStack:
    def __init__(self, iterable=None):
        self.elems = []
        self.sum_values = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, x):
        self.elems.append(x)
        self.sum_values += x

    def pop(self):
        if not self.elems:
            raise IndexError("pop from empty stack")
        self.sum_values -= self.elems[-1]
        return self.elems.pop()

    def __len__(self):
        return len(self.elems)

    def __bool__(self):
        return bool(self.elems)

    def __iter__(self):
        return iter(self.elems)

    def __repr__(self):
        return f"SumStack({self.elems})"

    @property
    def sum(self):
        return self.sum_values


class AverageStack:
    def __init__(self, iterable=None):
        self.elems = []
        self.sum_values = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, x):
        self.elems.append(x)
        self.sum_values += x

    def pop(self):
        if not self.elems:
            raise IndexError("pop from empty stack")
        self.sum_values -= self.elems[-1]
        return self.elems.pop()

    def __len__(self):
        return len(self.elems)

    def __bool__(self):
        return bool(self.elems)

    def __iter__(self):
        return iter(self.elems)

    def __repr__(self):
        return f"AverageStack({self.elems})"

    @property
    def average(self):
        if not self.elems:
            raise ValueError("average from empty stack")
        return self.sum_values / len(self.elems)


class FullStack:
    def __init__(self, iterable=None):
        self.elems = []
        self.max_values = []
        self.min_values = []
        self.sum_values = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, x):
        self.elems.append(x)
        self.sum_values += x
        if not self.max_values:
            self.max_values.append(x)
            self.min_values.append(x)
        else:
            self.max_values.append(max(x, self.max_values[-1]))
            self.min_values.append(min(x, self.min_values[-1]))

    def pop(self):
        if not self.elems:
            raise IndexError("pop from empty stack")
        self.sum_values -= self.elems[-1]
        self.max_values.pop()
        self.min_values.pop()
        return self.elems.pop()

    def __len__(self):
        return len(self.elems)

    def __bool__(self):
        return bool(self.elems)

    def __iter__(self):
        return iter(self.elems)

    def __repr__(self):
        return f"FullStack({self.elems})"

    @property
    def max(self):
        if not self.max_values:
            raise ValueError("max from empty stack")
        return self.max_values[-1]

    @property
    def min(self):
        if not self.min_values:
            raise ValueError("min from empty stack")
        return self.min_values[-1]

    @property
    def sum(self):
        return self.sum_values

    @property
    def average(self):
        if not self.elems:
            raise ValueError("average from empty stack")
        return self.sum_values / len(self.elems)


# Tests
def test_stacks():
    print("Testing MaxStack...")
    max_stack = MaxStack([10, 20, 30])
    assert max_stack.max == 30
    max_stack.pop()
    assert max_stack.max == 20

    print("Testing SumStack...")
    sum_stack = SumStack([1, 2, 3, 4])
    assert sum_stack.sum == 10
    sum_stack.pop()
    assert sum_stack.sum == 6

    print("Testing AverageStack...")
    avg_stack = AverageStack([10, 20, 30])
    assert avg_stack.average == 20
    avg_stack.pop()
    assert avg_stack.average == 15

    print("Testing FullStack...")
    full_stack = FullStack([1, 2, 3, 4])
    assert full_stack.max == 4
    assert full_stack.min == 1
    assert full_stack.sum == 10
    assert full_stack.average == 2.5
    full_stack.pop()
    assert full_stack.max == 3
    assert full_stack.min == 1

    print("All tests passed!")


# Run tests
test_stacks()


"""
Implement the container UniqArr:
add(x) — append value x if it doesn’t exist.
pop() — remove the last appended value.
x in a — check if x exists in uniq array a.

All operations must work in O(1).

Part 2: support len, bool, iterable, ==, a[i], etc

Part 3: implement:
find(x) — return the index of x or throw exception if does exist. Must work in O(1).

Past 4: implement:
popleft() — remove the first element. How to make it working fast with find(x) and a[i] ?
"""


class UniqArr:
    def __init__(self):
        self.elems = []
        self.index_map = {}

    def add(self, x):
        if x not in self.index_map:
            self.index_map[x] = len(self.elems)
            self.elems.append(x)

    def pop(self):
        if not self.elems:
            raise IndexError("pop from empty UniqArr")
        last_elem = self.elems.pop()
        del self.index_map[last_elem]
        return last_elem

    def __contains__(self, x):
        return x in self.index_map

    # Part 2: Support len, bool, iterable, ==, indexing, etc.
    def __len__(self):
        return len(self.elems)

    def __bool__(self):
        return bool(self.elems)

    def __iter__(self):
        return iter(self.elems)

    def __getitem__(self, index):
        return self.elems[index]

    def __eq__(self, other):
        if not isinstance(other, UniqArr):
            return False
        return self.elems == other.elems

    def __repr__(self):
        return f"UniqArr({self.elems})"

    # Part 3: Implement find(x)
    def find(self, x):
        if x not in self.index_map:
            raise ValueError(f"{x} not found in UniqArr")
        return self.index_map[x]

    # Part 4: Implement popleft
    def popleft(self):
        if not self.elems:
            raise IndexError("popleft from empty UniqArr")
        first_elem = self.elems.pop(0)
        del self.index_map[first_elem]
        # Update indices for remaining elements
        for i, elem in enumerate(self.elems):
            self.index_map[elem] = i
        return first_elem


# Testing UniqArr
def test_uniq_arr():
    print("Testing UniqArr...")
    a = UniqArr()
    a.add(10)
    a.add(20)
    a.add(30)
    assert len(a) == 3
    assert 10 in a
    assert 40 not in a

    a.add(20)  # Duplicate, should not be added
    assert len(a) == 3

    assert a.pop() == 30
    assert len(a) == 2

    a.add(40)
    assert a.find(40) == 2

    assert a.popleft() == 10
    assert len(a) == 2

    assert a[0] == 20
    assert a == UniqArr([20, 40])

    print("All tests passed!")


# Run tests
test_uniq_arr()
