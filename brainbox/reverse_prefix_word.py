def reversePrefix(word: str, ch: str) -> str:
    idx = word.find(ch)
    if idx == -1:
        return word
    return word[:idx+1][::-1] + word[idx+1:]

def test_reversePrefix():
    print(reversePrefix("abcdefd", "d"), "== dcbaefd")
    print(reversePrefix("hello", "l"), "== lleho")
    print(reversePrefix("hello", "z"), "== hello")
    print(reversePrefix("abc", "c"), "== cba")
    print(reversePrefix("a", "a"), "== a")
    print(reversePrefix("xyz", "x"), "== xyz")  # reversing only 'x' does nothing

test_reversePrefix()
