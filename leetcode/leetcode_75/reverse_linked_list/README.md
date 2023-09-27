# Reverse Linked List

---
### Instructions

Given the head of a singly linked list, reverse the list, and return the reversed list.

---

###Example 1:
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

```
###Example 2:
```
Input: head = [1,2]
Output: [2,1]
```


### Solution

```py
def reverseList2(head: ListNode | None) -> ListNode | None:
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node

```

* Time Complexity: 0(n)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75)