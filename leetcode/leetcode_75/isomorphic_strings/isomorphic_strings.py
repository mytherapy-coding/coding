def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d = {}
    for a, b in zip(s, t):
        if a in d:
            if d[a] != b:
                return False
        else:
            d[a] = b

    d = {}
    for a, b in zip(t, s):
        if a in d:
            if d[a] != b:
                return False
        else:
            d[a] = b

    return True


def isIsomorphic1(s: str, t: str) -> bool:
    def check(s, t):
        d = {}
        for a, b in zip(s, t):
            if a in d:
                if d[a] != b:
                    return False
            else:
                d[a] = b
        return True

    ok1 = check(s, t)
    ok2 = check(t, s)
    return ok1 and ok2


print(isIsomorphic1("egg", "add"))
