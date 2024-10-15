import collections


def isSubsequence(s: str, t: str) -> bool:
    i = 0
    for x in t:
        if i == len(s):
            return True
        if x == s[i]:
            i += 1
    return i == len(s)


def isSubsequence1(s: str, t: str) -> bool:
    while s and t:
        if s[0] == t[0]:
            s = s[1:]
        t = t[1:]
    return not s


def isSubsequence2(s: str, t: str) -> bool:
    s_letters = collections.deque(s)
    t_letters = collections.deque(t)
    while s_letters and t_letters:
        if s_letters[0] == t_letters[0]:
            s_letters.popleft()
        t_letters.popleft()
    return not s_letters


def isSubsequence3(s: str, t: str, ) -> bool:
    def check(s: str, t: str):
        if s == '':
            return True
        if t == '':
            return False
        if s[0] == t[0]:
            return check(s[1:], t[1:])
        return check(s, t[1:])

    return check(s, t)


def isSubsequence4(s: str, t: str) -> bool:
    def check(i: int, j: int) -> bool:
        if i == len(s):
            return True
        if j == len(t):
            return False
        if s[i] == t[j]:
            return check(i + 1, j + 1)
        return check(i, j + 1)

    return check(0, 0)


def isSubsequence5(s: str, t: str) -> bool:
    def check(s: str, t: str):
        if not s or not t:
            return not s

        if s[0] == t[0]:
            s = s[1:]
        return check(s, t[1:])

    return check(s, t)


s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))
