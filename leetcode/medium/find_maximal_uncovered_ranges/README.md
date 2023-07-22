### Find Maximal Uncovered Ranges

### Instructions
You are given an integer n which is the length of a 0-indexed array nums, and a 0-indexed 2D-array ranges, which is a list of sub-ranges of nums (sub-ranges may overlap).

Each row ranges[i] has exactly 2 cells:

	•	ranges[i][0], which shows the start of the ith range (inclusive)
	•	ranges[i][1], which shows the end of the ith range (inclusive)

These ranges cover some cells of nums and leave some cells uncovered. Your task is to find all of the uncovered ranges with maximal length.

Return a 2D-array answer of the uncovered ranges, sorted by the starting point in ascending order.
By all of the uncovered ranges with maximal length, we mean satisfying two conditions:

	•	Each uncovered cell should belong to exactly one sub-range
	•	There should not exist two ranges (l1, r1) and (l2, r2) such that r1 + 1 = l2


### Example 1:

```
Input: n = 10, ranges = [[3,5],[7,8]]
Output: [[0,2],[6,6],[9,9]]

Explanation: The ranges (3, 5) and (7, 8) are covered, so if we simplify the array nums to a binary array where 0 shows an uncovered cell and 1 shows a covered cell, the array becomes [0,0,0,1,1,1,0,1,1,0] in which we can observe that the ranges (0, 2), (6, 6) and (9, 9) aren't covered.
```
### Example 2:

```
Input: n = 3, ranges = [[0,2]]
Output: []

Explanation: In this example, the whole of the array nums is covered and there are no uncovered cells so the output is an empty array.
```
### Solution

```py

```
* Time Complexity: O()
* Space Complexity: O() using itertools.chain

Where n is the size of range.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/find-maximal-uncovered-ranges/)





































