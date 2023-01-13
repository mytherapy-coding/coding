# Find the unique number

---
### Instructions

There is an array with some numbers. All numbers are equal except for one. Try to find it!

For example: 

```py
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.

### Solution

```py
def find_uniq(arr):
    skip = arr[2] if arr[0] != arr[1] else arr[0]
    return next(e for e in arr if e != skip)

```
Worst Case:
* Time Complexity: O(n)
* Space Complexity: O(1) 

Best Case:
* Time Complexity: O(1)
* Space Complexity: O(1) 

Where n is the size of input.

The solution is linear.
You may find other solutions in the Python file.

* [Source from Codewars](https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python)
