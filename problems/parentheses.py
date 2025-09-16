"""
Write function that detects if the given expression contains balanced parentheses

def  isbalanced(expr: str) -> bool
Valid:
((())())
((()))
()()(())

Invalid:
()))
(
))
()(
((()
"""


def isbalanced0(expr: str) -> bool:
    counter = 0

    for char in expr:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1

        if counter < 0:
            # More closing parentheses encountered without matching opening parentheses
            return False

    return counter == 0


def isbalanced1(expr: str, stack=None) -> bool:
    if stack is None:
        stack = []
    for char in expr:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


def isbalanced2(expr: str, mkstack=list) -> bool:
    stack = mkstack()
    for char in expr:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


def isbalanced3(expr: str, mkstack=list) -> bool:
    stack = mkstack()
    opening_parentheses = ("(", "[", "{")  # "([{"
    closing_parentheses = (")", "]", "}")

    for char in expr:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack:
                return False
            opening_paren = stack.pop()
            if opening_parentheses.index(opening_paren) != closing_parentheses.index(
                char
            ):
                return False

    return not stack


def isbalanced4(expr: str, mkstack=list) -> bool:
    stack = mkstack()
    parentheses_map = {"(": ")", "[": "]", "{": "}"}

    for char in expr:
        if char in parentheses_map:
            stack.append(char)
        elif char in parentheses_map.values():
            if not stack:
                return False
            if parentheses_map[stack.pop()] != char:
                return False

    return not stack


def test():
    from collections import deque

    class Stack:
        def __init__(self):
            self.items = []

        def append(self, x: any):
            self.items.append(x)

        def pop(self) -> any:
            return self.items.pop()

        def __bool__(self) -> bool:
            return bool(self.items)

    for expr in "()()()", "()(", "()":
        for isbalanced in isbalanced0, isbalanced1, isbalanced2:
            print(expr, isbalanced(expr))
            print()

    for expr in "[](){}(", "()(", "()":
        for isbalanced in isbalanced3, isbalanced4:
            print(expr, isbalanced(expr))
            for mkstack in deque, list, Stack:
                print(expr, isbalanced(expr, mkstack=mkstack))
            print()


test()
