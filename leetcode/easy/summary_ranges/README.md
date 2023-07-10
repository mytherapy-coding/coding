### Summary Ranges

### Instructions

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

### Example:

```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

### Solution

```py
def summaryRanges(nums: list[int]) -> list[str]:

    def find_intervals(nums: list[int]):
        if not nums:
            return
        start = end = nums[0]
        for num in nums:
            if num <= end + 1:
                end = num
            else:
                yield start, end
                start = end = num
        yield start, end

    return [str(start) if start == end else f'{start}->{end}' for start, end in find_intervals(nums)]

```
* Time Complexity: O(n)
* Space Complexity: O(1) 

Where n is nums size (size of input).

Algorithm is linear in time and constant in space

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/summary-ranges/description/)



