# Number of Recent Calls

---
### Instructions
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

---

###Example 1:

```
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
```
### Solution

```py
import collections

class RecentCounter:
    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] + 3000 < t:
            self.queue.popleft()
        return len(self.queue)
```

* Time Complexity: 0(1)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75)