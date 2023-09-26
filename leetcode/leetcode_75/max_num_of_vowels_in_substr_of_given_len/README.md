## Maximum Number of Vowels in a Substring of Given Length

---
### Instructions
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

---

###Example 1:

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```
###Example 2:
```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

### Solution

```py
def maxVowels4(s: str, k: int) -> int:
    win_vowels = 0
    win_max = float('-inf')
    for i, ch in enumerate(s):
        win_vowels += voweled(ch)
        if i >= k:
            win_vowels -= voweled(s[i - k])
        if i >= k - 1:
            win_max = max(win_vowels, win_max)

    return win_max
```

* Time Complexity: 0(n)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75)



