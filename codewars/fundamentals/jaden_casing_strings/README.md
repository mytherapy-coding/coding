# Jaden Casing Strings

---
### Instructions

Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. 
When writing on Twitter, he is known for almost always capitalizing every word. 
For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.
Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

```py
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

```

---

### Solution

```py
import string

def to_jaden_case1(s: str) -> str:
    return string.capwords(s, ' ')
```

* Time Complexity: O(n)
* Space Complexity: O(n) 

The algorithm runs in polynomial time and space (O(the input size)).

See other solutions in the Python file.


* [Code at OnlineDB](https://onlinegdb.com/k06Vhs0jy)
* [Source from Codewars](https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python)
