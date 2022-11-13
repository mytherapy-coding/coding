# Binary Addition

---
### Instructions

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.
Examples:(Input1, Input2 --> Output (explanation)))

```py
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

```

---

### Solution

```py
def add_binary3(a: int, b: int) -> str:
    return f'{a + b:b}'
```

* Time Complexity: O(log(a+b))
* Space Complexity: O(log(a+b)) 

The algorithm runs in polynomial time and space (O(the input size)).

The solution is linear.
More trivial solutions (see the Python file) are polynomial time.

* [Code at OnlineDB](https://onlinegdb.com/T7UmFCH4Z)
* [Source from Codewars](https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python)
