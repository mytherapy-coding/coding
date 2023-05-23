'''
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
'''

from collections import deque

from collections import deque

def isbalanced0(expr: str) -> bool:
    stack = deque()
    parentheses_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in expr:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map:
            if not stack:
                return False
            left_parenthes = stack.pop()
            if left_parenthes != parentheses_map[char]:
                return False

    return not stack



def isbalanced01(expr: str, mkstack =deque) -> bool:
    stack = mkstack()
    parentheses_map = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for char in expr:
        if char in parentheses_map:
            stack.append(char)
        elif char in parentheses_map.values():
            if not stack:
                return False
            if parentheses_map[stack.pop()] != char:
                return False

    return not stack


def isbalanced(expr: str) -> bool:
    stack = deque()
    opening_parentheses = ["(", "[", "{"]
    closing_parentheses = [")", "]", "}"]

    for char in expr:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack:
                return False
            opening_paren = stack.pop()
            if opening_parentheses.index(opening_paren) != closing_parentheses.index(char):
                return False

    return len(stack) == 0


def isbalanced1(expr: str) -> bool:
    counter = 0

    for char in expr:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1

        if counter < 0:  # More closing parentheses encountered without matching opening parentheses
            return False

    return counter == 0


def isbalanced2(expr: str, stack=None) -> bool:
    if stack is None:
        stack = deque()
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack


def isbalanced3(expr: str, stack=None) -> bool:
    if stack is None:
        stack = deque()
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack


from collections import deque


def isbalanced4(expr: str, mkstack=deque) -> bool:
    stack = mkstack()
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

expr = "[](){}("
print(isbalanced0(expr))


print(isbalanced0("()("))
print(isbalanced01("()("))
print(isbalanced1("()"))
print(isbalanced2("()"))
expr = "()"
print(isbalanced2(expr))

print(isbalanced2(expr, []))
print(isbalanced2(expr, deque()))

print(isbalanced3(expr))
print(isbalanced3(expr, deque()))
print(isbalanced3(expr, list()))

print(isbalanced4(expr))
print(isbalanced4(expr, mkstack=deque))
print(isbalanced4(expr, mkstack=list))


