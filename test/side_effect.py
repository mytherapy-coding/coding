import itertools
import collections

x = 10
y = 20

x, y = y, x

print(x, y)
print()


def mul_2(values: list[int]) -> list[int]:
    return [value * 2 for value in values]


def find_short_words(words):
    i = 0
    while i < len(words):
        if len(words[i]) >= 4:
            words.pop(i)
        else:
            i += 1
    return words


def find_short_words2(words: list[str]) -> list[str]:
    res = []
    for word in words:
        if len(word) <= 3:
            res.append(word)
    return res


print(find_short_words2(['hello', 'cat', 'hui', 'love', 'you']))


def prefix(k: int, values: list) -> list:
    del values[k:]
    return values


def prefix1(k: int, values: list) -> list:
    res = []
    for i, value in zip(range(1, len(values)), values):
        if i <= k:
            res.append(value)
    return res


def prefix2(k: int, values: list) -> list:
    return [value for _, value in zip(range(k), values)]


def prefix4(k: int, values: list) -> list:
    return [value for i, value in enumerate(values) if i < k]


def prefix5(k: int, values: list) -> list:
    return values[:k]


print(prefix5(2, ["you", "love", "world"]))


def uniq_values(values: list) -> list:
    i = 0
    while i < len(values):
        if values.count(values[i]) > 1:
            values.remove(values[i])
        else:
            i += 1
    return values


def uniq_values1(values: list) -> list:
    res = []
    for value in values:
        if values.count(value) <= 1:
            res.append(value)
    return res


def uniq_values2(values: list) -> list:
    return [value for value in values if values.count(value) <= 1]


print(uniq_values2(['you', 'love', 'you']))
print(uniq_values2(['a', 'b', 'c', 'b']))

print('counter')


def uniq_values3(values: list) -> list:
    count = collections.Counter(values)
    res = []
    for value in values:
        if count[value] == 1:
            res.append(value)
    return res


print(uniq_values3(['you', 'love', 'you']))
print(uniq_values3(['a', 'b', 'c', 'b']))


def uniq_values4(values: list) -> list:
    count = collections.Counter(values)
    res = []
    for value in count:
        if count[value] == 1:
            res.append(value)
    return res


print(uniq_values4(['you', 'love', 'you']))
print(uniq_values4(['a', 'b', 'c', 'b']))


def uniq_values5(values: list) -> list:
    count = collections.Counter(values)
    res = []
    for value, c in count.items():
        if c == 1:
            res.append(value)
    return res


print(uniq_values5(['you', 'love', 'you']))
print(uniq_values5(['a', 'b', 'c', 'b']))

def uniq_values6(values: list) -> list:
    return [value for value, c in collections.Counter(values).items() if c == 1]


print(uniq_values6(['you', 'love', 'you']))
print(uniq_values6(['a', 'b', 'c', 'b']))

def mk_love(words: list[str]) -> str:
    words.append('love')
    words.append('me')
    return ' '.join(words)


words = ['my', 'parents']
print(words)
print(mk_love(words))
print(words)
print()


def mk_love1(words: list[str]) -> str:
    res = []
    for word in words:
        res.append(word)
    res.append('love')
    res.append('me')
    return ' '.join(res)


words = ['my', 'parents']
print(words)
print(mk_love1(words))
print(words)
print()

print('update')


def mk_love2(words: list[str]) -> str:
    res = []
    res.extend(words)
    res.append('love')
    res.append('me')
    return ' '.join(res)


words = ['my', 'parents']
print(words)
print(mk_love2(words))
print(words)
print()


def mk_love3(words: list[str]) -> str:
    return ' '.join(words + ['love', 'me'])


words = ['my', 'parents']
print(words)
print(mk_love3(words))
print(words)
print('chain')


def mk_love4(words: list[str]) -> str:
    return ' '.join(itertools.chain(words, ['love', 'me']))


words = ['my', 'parents']
print(words)
print(mk_love4(words))
print(words)
print()
