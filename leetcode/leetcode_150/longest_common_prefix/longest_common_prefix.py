def longestCommonPrefix(strs: list[str]) -> str:
    for k, t in enumerate(zip(*strs)):
        t_set = set(t)
        print(t_set)
        if len(t_set) != 1:
            return strs[0][:k]
    return min(strs, key=lambda w: len(w))


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))
