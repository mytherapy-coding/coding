def remove_outermost_parentheses(s: str) -> str:
    result = []
    balance = 0

    for ch in s:
        if ch == '(':
            if balance > 0:
                result.append(ch)
            balance += 1
        else:  # ch == ')'
            balance -= 1
            if balance > 0:
                result.append(ch)

    return "".join(result)


def test_remove_outermost_parentheses():
    print(remove_outermost_parentheses("(()())(())"), "== ()()()")
    print(remove_outermost_parentheses("(()())(())(()(()))"), "== ()()()()(())")
    print(remove_outermost_parentheses("()()"), "== ")
    print(remove_outermost_parentheses("((()))"), "== (())")
    print(remove_outermost_parentheses("(()(()))"), "== ()(())")

test_remove_outermost_parentheses()
