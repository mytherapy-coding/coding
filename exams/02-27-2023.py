import functools
import math


def unique_words(s, k):
    unique = set()
    for w in s.split():
        if len(w) <= k:
            unique.add(w)
    return unique


def unique_words1(s, k):
    return set(w for w in s.split() if len(w) <= k)


# print(unique_words("Hello world hi Bob hi", 3))

def unique_common(words1, words2):
    unique = set()
    unique1 = set(words1)
    unique2 = set(words2)
    for w in unique1:
        if w in unique2:
            unique.add(w)
    return unique


def unique_common1(words1, words2):
    unique1 = set(words1)
    unique2 = set(words2)
    return unique1.intersection(unique2)


def unique_common2(words1, words2):
    return set(words1) & set(words2)


print(unique_common2(['hi', 'love', 'hi', 'you'], ['hi', 'I', 'lov']))


def mult_table(N):
    for n in range(1, N + 1):
        s = ''
        for m in range(1, N + 1):
            s += ' '
            if n * m < 10:
                s += ' '
            s += str(n * m)
        print(s)


def mult_table1(N):
    for n in range(1, N + 1):
        s = ''
        for m in range(1, N + 1):
            s += f'{n * m: 3}'
        print(s)


mult_table1(5)


def mul_tab(N):
    res = []
    for n in range(1, N + 1):
        row = []
        for m in range(1, N + 1):
            row.append(n * m)
        res.append(row)
    return res


def mul_tab1(N):
    return [[n * m for m in range(1, N + 1)] for n in range(1, N + 1)]


print(mul_tab1(5))


def min_of_tab1(nums):
    table = []
    for row in nums:
        for n in row:
            table.append(n)
    return min(table)


def min_of_tab2(nums):
    table = []
    for row in nums:
        table.append(min(row))
    return min(table)


def min_of_tab2(nums):
    table = []
    for row in nums:
        table.append(min(row))
    return min(table)


def min_of_tab3(nums):
    return min([min(row) for row in nums])


for min_of in min_of_tab1, min_of_tab2, min_of_tab3:
    print(min_of([[4, 6, 8, 8, 9], [4, 7, 9, 2]]))

'''
space complexity

min_of_tab1, 
min_of_tab2, 
min_of_tab3

time complexity 

min_of_tab1, 
min_of_tab2, 
min_of_tab3

'''

def list_of_words(words):
    res = []
    for w in words:
        res.append((len(w), w))
    return max(res)[1]

print(list_of_words(['hello', 'world', 'love', 'you']))


def list_of_words1(words):
    return max((len(w), w) for w in words)[1]
print(list_of_words1(['hello', 'world', 'love', 'you']))


def list_of_words2(words):
    return max(words, key=len, default=0)

print(list_of_words2(['hello', 'world', 'love', 'you']))


def common_letters(words):
    res = []
    for word in words:
        for w in word:
            res += w.split()
    return res


print(common_letters(['love', 'you', 'hello']))


def find_common(w1, w2):
    word1 = w1.lower()
    word2 = w2.lower()
    common1 = set(word1)
    common2 = set(word2)
    return common1.intersection(common2)

print(find_common('hello', 'world'))
print(find_common('Hello', 'WorLd'))


def find_common1(w1, w2):
    word1 = w1.lower()
    word2 = w2.lower()
    common1 = set(word1)
    common2 = set(word2)
    return common1 & common2


def find_common2(w1, w2):
    return set(w1.lower()) & set(w2.lower())
print(find_common2('hello', 'world'))
print(find_common2('Hello', 'WorLd'))

print()

def find_common3(words):

    w1 = []
    for word in words:
        w1.append(word.lower())
    common =[]
    for w in w1:
        common.append(set(w))
    return [c & for c in common]


print(find_common3(['hello', 'world']))
