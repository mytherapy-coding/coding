import collections


def firstUniqChar0(s):
    count = collections.Counter(s)
    print(count)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


def firstUniqChar1(s):
    count = collections.Counter(s)
    return next((i for i, ch in enumerate(s) if count[ch] == 1), -1)


print(firstUniqChar1("loveleetcode"))
print(firstUniqChar1("leetcode"))
print(firstUniqChar1("445669357203525"))
