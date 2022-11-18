# Reverse words

---
### Instructions

Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

---

Example:

```py
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

```

---

### Solution

```py
def reverse_words2(text):
    return " ".join(w[::-1] for w in text.split(" "))
    
```

* Time Complexity: O(n)
* Space Complexity: O(n) 


See other solutions in the Python file.


* [Code at OnlineDB](https://onlinegdb.com/iWIEaIRXR)
* [Source from Codewars](https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python)
