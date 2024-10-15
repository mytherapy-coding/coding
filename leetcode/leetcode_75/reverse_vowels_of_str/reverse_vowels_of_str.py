def reverseVowels0(s: str) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u')
    s_vowels = []
    for ch in s:
        if ch.lower() in vowels:
            s_vowels.append(ch)
    res = []
    for ch in s:
        if ch.lower() in vowels:
            res.append(s_vowels.pop())
        else:
            res.append(ch)
    return ''.join(res)


def reverseVowels1(s: str) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u')
    s_vowels = [ch for ch in s if ch.lower() in vowels]
    return ''.join(s_vowels.pop() if ch.lower() in vowels else ch for ch in s)


def reverseVowels2(s: str) -> str:
    vowels = 'aeiou'
    vowels += vowels.upper()
    s_vowels = [ch for ch in s if ch in vowels]
    it = reversed(s_vowels)
    return ''.join(next(it) if ch in vowels else ch for ch in s)


print(reverseVowels0('Hello'))
print(reverseVowels1('Hello'))
print(reverseVowels2('Hello'))
