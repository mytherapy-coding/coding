# Odd Even Linked List

---
### Instructions
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



---

###Example 1:
```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```
###Example 2:
```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```


### Solution

```py
def oddEvenList2(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
    even_last: ListNode|None = None
    odd_last: ListNode|None = None
    even_head = head
    odd_head = head.next
    while head:
        if even_last:
            even_last.next = head
        even_last = head
        head = head.next
        if not head:
            break
        if odd_last:
            odd_last.next = head
        odd_last = head
        head = head.next

    even_last.next = odd_head
    if odd_last:
        odd_last.next = None
    return even_head
```

* Time Complexity: 0(n)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/odd-even-linked-list/)