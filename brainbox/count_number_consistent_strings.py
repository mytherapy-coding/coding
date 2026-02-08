def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)
    count = 0

    for w in words:
        if all(ch in allowed_set for ch in w):
            count += 1

    return count


import unittest

def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)
    count = 0
    for w in words:
        if all(ch in allowed_set for ch in w):
            count += 1
    return count


class TestCountConsistentStrings(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]),
            2
        )

    def test_all_consistent(self):
        self.assertEqual(
            countConsistentStrings("abc", ["a", "bb", "ccc", "abc"]),
            4
        )

    def test_none_consistent(self):
        self.assertEqual(
            countConsistentStrings("a", ["b", "c", "d"]),
            0
        )

    def test_empty_allowed(self):
        self.assertEqual(
            countConsistentStrings("", ["a", "b", ""]),
            1  # only "" is consistent
        )

    def test_empty_words(self):
        self.assertEqual(
            countConsistentStrings("abc", []),
            0
        )

    def test_mixed(self):
        self.assertEqual(
            countConsistentStrings("xyz", ["x", "xy", "yxz", "abc", "zzz"]),
            4
        )

    def test_repeated_characters(self):
        self.assertEqual(
            countConsistentStrings("ab", ["aaaa", "bbbb", "abab", "baba", "ccc"]),
            4
        )


if __name__ == "__main__":
    unittest.main()
