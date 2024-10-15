def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))


def find(s, t, start):
    if start + len(t) > len(s):
        return False
    for i in range(len(t)):
        if s[i + start] != t[i]:
            return False
    return True


def strStr(haystack: str, needle: str) -> int:
    for start in range(len(haystack)):
        if find(haystack, needle, start):
            return start
    return -1

