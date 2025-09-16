import collections
import dataclasses
import heapq


def topKFrequent0(words: list[str], k: int) -> list[str]:
    count = collections.Counter(words)
    return sorted(count.keys(), key=lambda w: (-count[w], w))[:k]


def topKFrequent1(words: list[str], k: int) -> list[str]:
    count = collections.Counter(words)
    return sorted(sorted(count.keys()), key=count.get, reverse=True)[:k]


def topKFrequent2(words: list[str], k: int) -> list[str]:
    count = collections.Counter(words)
    ordered = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]


@dataclasses.dataclass
class Obj:
    freq: int
    word: str

    def __lt__(self, other):
        """
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.word > other.word
        """
        return (-self.freq, self.word) >= (-other.freq, other.word)


def topKFrequent3(words: list[str], k: int) -> list[str]:
    count = collections.Counter(words)
    ordered = []
    for word, freq in count.items():
        heapq.heappush(ordered, Obj(freq, word))
        if len(ordered) > k:
            heapq.heappop(ordered)
    return [heapq.heappop(ordered).word for _ in range(k)][::-1]  # k log k
    # return [obj.word for obj in sorted(ordered, reverse=True)] # k log k


def topKFrequent4(words: list[str], k: int) -> list[str]:
    count = collections.Counter(words)
    return heapq.nsmallest(k, count.keys(), key=lambda w: (-count[w], w))


def test():
    funcs = [
        topKFrequent0,
        topKFrequent1,
        topKFrequent2,
        topKFrequent3,
        topKFrequent4,
    ]

    tests = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
            4,
            ["the", "is", "sunny", "day"],
        ),
    ]

    for func in funcs:
        for words, k, expected_result in tests:
            result = func(words, k)
            assert (
                result == expected_result
            ), f"{func.__name__}{words, k} => {result} (Expected: {expected_result})"
            print(
                f"{func.__name__}{words, k} => {result} (Expected: {expected_result})"
            )


print(test())
