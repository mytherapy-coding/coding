### Relative Ranks

### Instructions

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.


### Example:

```
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
```

### Solution

```py
def findRelativeRanks4(score: list[int]) -> list[str]:
    rank = {x: i + 1 for i, x in enumerate(sorted(score, reverse=True))}
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}  # O(1)
    return [d.get(rank[x], str(rank[x])) for x in score]
```
* Time Complexity: O(n log n)
* Space Complexity: O(n) 

Where n is the size of score.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/relative-ranks/)




























https://leetcode.com/problems/relative-ranks/