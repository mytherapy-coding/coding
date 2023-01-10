# Write Number in Expanded Form

---
### Instructions

You will be given a number and you will need to return it as a string in Expanded Form. For example:

```py 
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```

NOTE: All numbers will be whole numbers greater than 0.

### Solution

```py
def expanded_form4(num: int) -> str:
    return ' + '.join(digit + '0' * k for k, digit in zip(range(len(str(num)) - 1, -1, -1), str(num)) if digit != '0')
```

* Time Complexity: O(n^2)
* Space Complexity: O(n^2) 

Where n is the size of input, number of digits of num.

The solution is quadratic.
You may find other solutions in the Python file.

* [Source from Codewars](https://www.codewars.com/kata/5842df8ccbd22792a4000245/solutions/python)
