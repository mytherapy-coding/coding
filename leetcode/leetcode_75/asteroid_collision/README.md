# Asteroid Collision

---
### Instructions

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

---

### Example 1:

```
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
```
### Example 2:
```
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```


### Solution

```py
def asteroidCollision(asteroids: list[int]) -> list[int]:
    st = []
    for a in asteroids:
        while st and 0 < st[-1] < -a:
            st.pop()
        if not st or a > 0 or st[-1] < 0:
            st.append(a)
        elif st[-1] == -a:
            st.pop()

    return st
```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75)