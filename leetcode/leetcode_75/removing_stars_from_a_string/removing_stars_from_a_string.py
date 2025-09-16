def removeStars1(s: str) -> str:
    new_s = list(s)
    i = 1
    while i < len(new_s):
        if new_s[i] == "*":
            del new_s[i - 1 : i + 1]
            i -= 1
        else:
            i += 1
    return "".join(new_s)


def removeStars2(s: str) -> str:
    res = []
    for ch in s:
        if ch != "*":
            res.append(ch)
        else:
            res.pop()
    return "".join(res)


s = "leet**cod*e"
print(removeStars2(s))
