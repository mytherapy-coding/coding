from collections import Counter

def hasDuplicate(nums: list[int]) -> bool:
    
        d = Counter()
        for v in nums:
                d[v] += 1
                if d[v] == 2:
                        return True
        

print(hasDuplicate([1,2,2,5,7,5]))
