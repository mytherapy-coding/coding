def truncateSentence(s: str, k: int) -> str:
    return " ".join(s.split()[:k])

def test_truncateSentence():
    print(truncateSentence("Hello world", 1), "== Hello")
    print(truncateSentence("Hello world", 2), "== Hello world")
    print(truncateSentence("What is your name", 3), "== What is your")
    print(truncateSentence("This is a test sentence", 4), "== This is a test")
    print(truncateSentence("Single", 1), "== Single")

test_truncateSentence()
