from collections import Counter


def uniqueOccurrences(arr: list[int]) -> bool:
    res = Counter(arr)
    set_vals = set(res.values())
    return len(set_vals) == len(res)


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))