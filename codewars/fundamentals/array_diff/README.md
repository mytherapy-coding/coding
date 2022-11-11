
# Array.diff

---

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.
```py
array_diff([1,2],[1]) == [2]
```
If a value is present in b, all of its occurrences must be removed from the other:

```py
array_diff([1,2,2,2,3],[2]) == [1,3]
```
---

### Solution

```py
def array_diff3(a: list, b: list) -> list:
    b = set(b)
    return [x for x in a if x not in b]
```
[Code at OnlineDB](https://onlinegdb.com/mudUBK1Mq)

[Source from Codewars](https://www.codewars.com/kata/523f5d21c841566fde000009/train/python)

Time Complexity: O(n)
Space Complexity: O(n) 

Where n is the size of input (lists a and b).

The solution is linear.
More trivial solutions (see the Python file) are polynomial time.
