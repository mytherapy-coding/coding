Is this a triangle?

---
### Instructions

Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).



---

### Solution

```py
def is_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a

```

* Time Complexity: O(1)
* Space Complexity: O(1) 

The algorithm runs in polynomial time and space (O(the input size)).

See other solutions in the Python file.


* [Code at OnlineDB](https://onlinegdb.com/RQDkFHrZso)
* [Source from Codewars](https://www.codewars.com/kata/56606694ec01347ce800001b/train/python)
