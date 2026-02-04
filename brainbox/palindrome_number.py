def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

def test_is_palindrome_true():
    assert isPalindrome(121)
    assert isPalindrome(0)
    assert isPalindrome(1221)


def test_is_palindrome_false():
    assert not isPalindrome(123)
    assert not isPalindrome(10)
    assert not isPalindrome(-1)