def check1(expr: str) -> bool:
    counter = 0
    for x in expr:
        if x == "(":
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1
    return counter == 0


print(check1("()"))
print(check1(""))
print(check1("((()"))

print()


def check2(expr: str) -> bool:
    stack = []
    for x in expr:
        if x == "(":
            stack.append(x)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


print(check2("()"))
print(check2(""))
print(check2("((()"))
print(check2(")))"))


class Mystack:
    def __init__(self):
        self.elems = []

    def push(self, x):
        self.elems.append(x)

    def pop(self):
        return self.elems.pop()

    def empty(self):
        return len(self.elems) == 0

    def __len__(self) -> int:
        return len(self.elems)


def check3(expr: str) -> bool:
    st = Mystack()
    for x in expr:
        if x == "(":
            st.push(x)
        else:
            if st.empty():
                return False
            st.pop()
    return st.empty()


print(check3("()"))
print(check3(""))
print(check3("((()"))
print(check3(")))"))


def check4(expr: str) -> bool:
    d = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for x in expr:
        if x in d:
            assert x in d
            stack.append(x)
        else:
            assert x in d.values()
            if not stack:
                return False
            assert x in d.values()
            assert len(stack) > 0
            a = stack[-1]
            assert a in d
            # d[a] is matching a
            assert (a, d[a]) in d.items()
            if x != d[a]:
                # a and x not matched
                return False
            assert x == d[a]
            assert (a, d[a]) in d.items()
            assert (a, x) in d.items()
            # a and x matched
            stack.pop()
    return not stack


print(check4("()"))
print(check4(""))
print(check4("((()"))
print(check4(")))"))


def check5(expr: str) -> bool:
    d = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for x in expr:
        if x in d:
            stack.append(x)
        else:
            if not stack or x != d[stack[-1]]:
                return False
            stack.pop()
    return not stack


def check6(expr: str) -> bool:
    left = ["(", "[", "{", "<"]
    right = [")", "]", "}", ">"]
    stack = []
    for x in expr:
        if x in left:
            stack.append(x)
        else:
            assert x in right
            if not stack or left[right.index(x)] != stack[-1]:
                return False
            stack.pop()
    return not stack


print(check6("()"))
print(check6(""))
print(check6("((()"))
print(check6(")))"))
print()
print()
"""
Implement Counter: implementation 1 is based on integer, implementaion 2 is 
based on Mystack. Methods to be implemented: inc(), dec(), get(), dec_if_exceeds(limit)
def check1(expr: str) -> bool:
    counter = 0
    for x in expr:
        if x == '(':
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1
    return counter == 0


"""


class Mycounter:
    def __init__(self, initial_value: int = 0):
        self.n = initial_value

    def inc(self):
        self.n += 1

    def dec(self):
        self.n -= 1

    def positive(self) -> bool:
        return self.n > 0

    def get(self) -> int:
        return self.n

    def dec_if_exceeds(self, limit: int):
        if self.n > limit:
            self.dec()


def check7(expr: str) -> bool:
    counter = Mycounter()
    for x in expr:
        if x == "(":
            counter.inc()
        else:
            if not counter.positive():
                return False
            counter.dec()
    return not counter.positive()


print(check7("()"))
print(check7(""))
print(check7("((()"))
print(check7(")))"))

print("_______________________________")


class Mycounter2:
    def __init__(self):
        self.elems = Mystack()

    def inc(self):
        self.elems.push(1)

    def dec(self):
        self.elems.pop()

    def positive(self) -> bool:
        return not self.elems.empty()

    def get(self) -> int:
        return len(self.elems)

    def dec_if_exceeds(self, limit: int):
        if self.get() > limit:
            self.dec()


def check8(expr: str) -> bool:
    counter = Mycounter2()
    for x in expr:
        if x == "(":
            counter.inc()
        else:
            if not counter.positive():
                return False
            counter.dec()
    return not counter.positive()


print(check8("()"))
print(check8(""))
print(check8("((()"))
print(check8(")))"))
print(check8("(())"))


def check9(expr: str) -> bool:

    print(check9("()"))
    print(check9(""))
    print(check9("((()"))
    print(check9(")))"))
    print(check9("(())"))
