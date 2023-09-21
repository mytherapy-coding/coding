# Decode String

---
### Instructions
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

---

###Example 1:

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```
###Example 2:
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

### Solution

```py
def decodeString(s: str) -> str:
    st = []
    for ch in s:
        if ch != ']':
            st.append(ch)
        else:
            data = []
            while st[-1] != '[':
                data.append(st.pop())
            # st[-1] == '['
            st.pop()
            number = []
            while st and st[-1].isdigit():
                number.append(st.pop())
            num = int(''.join(reversed(number)))
            d = ''.join(reversed(data))
            st.append(num*d)
    return ''.join(st)

```

* Time Complexity: 0(n^2)
* Space Complexity: O(n^n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75)