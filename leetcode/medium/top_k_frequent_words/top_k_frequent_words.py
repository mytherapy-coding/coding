import collections
import heapq
import dataclasses


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
        '''
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.word > other.word
        '''
        return (-self.freq, self.word) >= (-other.freq, other.word)



def topKFrequent3(words: list[str], k: int) -> list[str]:
    count = collections.Counter(words)
    ordered = []
    for word, freq in count.items():
        heapq.heappush(ordered, Obj(freq, word))
        if len(ordered) > k:
            heapq.heappop(ordered)
    return [heapq.heappop(ordered).word for _ in range(k)][::-1] # k log k
    #return [obj.word for obj in sorted(ordered, reverse=True)] # k log k



def topKFrequent4(words: list[str], k: int) -> list[str]:
    count = collections.Counter(words)
    return heapq.nsmallest(k, count.keys(), key=lambda w: (-count[w], w))


'''
def test():
    funcs = [
        topKFrequent0,
        topKFrequent1,
        topKFrequent2,
        topKFrequent3,
        topKFrequent4,
        ]

    tests = [

    ]
    for func in funcs:
        for nums, k, expected_result in tests:
            result = func(nums, k)
            assert result == expected_result, f"{func.__name__}{nums, k} => {result} (Expected: {expected_result})"
            print(f"{func.__name__}{nums, k} => {result} (Expected: {expected_result})")

print(test())
'''


words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(topKFrequent3(words, k))
'''
words = ["love", "i", "leetcode", "i", "love", "coding"]


k = 2
print(topKFrequent3(words, k))

print(topKFrequent0(words, k))
print(topKFrequent1(words, k))
print()
print(topKFrequent2(words, k))
print(topKFrequent3(words, k))
print(topKFrequent4(words, k))
'''


'''
def test():
    funcs = [
        topKFrequent0,
        topKFrequent1,
        

        ]

    tests = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2),
        (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
        

    ]
    for func in funcs:
        for nums, k, expected_result in tests:
            result = func(nums, k)
            assert result == expected_result, f"{func.__name__}{nums, k} => {result} (Expected: {expected_result})"
            print(f"{func.__name__}{nums, k} => {result} (Expected: {expected_result})")

print(test())

'''
