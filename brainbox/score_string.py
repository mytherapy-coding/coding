def score_of_string(s: str) -> int:
    total = 0
    for i in range(len(s) - 1):
        total += abs(ord(s[i]) - ord(s[i + 1]))
    return total


def test_score_of_string():
    # Provided example
    assert score_of_string("hello") == 13

    # Basic cases
    assert score_of_string("abc") == 2      # |97-98| + |98-99| = 1 + 1
    assert score_of_string("aaa") == 0      # all same letters
    assert score_of_string("zaz") == 50     # |122-97| + |97-122| = 25 + 25

    # Edge cases
    assert score_of_string("") == 0
    assert score_of_string("a") == 0

    print("All tests passed!")

test_score_of_string()
