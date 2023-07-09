### Smallest Number in Infinite Set

---
### Instructions

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

### Example 1:

```
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

```

### Solution

```py
import heapq

class SmallestInfiniteSet6:
    def __init__(self):
        self.smallest = 0
        self.added_back = []
        self.unique = set()
        
    def popSmallest(self) -> int:
        if self.added_back:
            self.unique.remove(self.added_back[0])
            return heapq.heappop(self.added_back)  # O(log n)
        self.smallest += 1
        return self.smallest

    def addBack(self, num):  # O(log n)
        if num <= self.smallest and num not in self.unique:
            heapq.heappush(self.added_back, num)  # O(log n)
            self.unique.add(num)  # O(1)
        
```
Time Complexity: O(n log n) for n calls
* __init__: O(1)
* popSmallest: O(log n)
* addBack: O(log n)

Space Complexity: O(n) for n calls

Where n is the number of addBack calls (or added_back size).

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/smallest-number-in-infinite-set/)




































