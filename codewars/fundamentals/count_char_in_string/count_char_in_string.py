from collections import Counter, defaultdict


def count(s: str) -> dict[str, int]:
    res: dict[str, int] = {}
    for ch in s:
        res[ch] = res.get(ch, 0) + 1
    return res


def count1(s: str) -> defaultdict[str, int]:
    res = defaultdict(int)
    for ch in s:
        res[ch] += 1
    return res


def count2(s: str) -> Counter[str]:
    return Counter(s)


print(count("HeLlo"))
print(count("HeLlo'"))
print(count(""))

print(count1("HeLlo"))
print(count1("HeLlo'"))
print(count1(""))

print(count2("HeLlo"))
print(count2("HeLlo'"))
print(count2(""))
