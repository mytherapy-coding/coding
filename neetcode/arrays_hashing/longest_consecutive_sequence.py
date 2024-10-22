def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    s = sorted(set(nums))
    res = [1]
    count = 1    
    for i in range(1, len(s)):
        if s[i] == s[i-1] + 1:
            count += 1
        else:
            count = 1
        res.append(count)
        
        return max(res)
    

            


print(longestConsecutive([0,3,2,5,4,6,1,1]))