from collections import Counter
def hasDuplicate(nums: list[int]) -> bool:
        c = Counter(nums)
        return any(n > 1 for n in c.values())

print(hasDuplicate([1,2,2,5,7,5]))