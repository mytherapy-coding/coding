# Delete the Middle Node of a Linked List 

---
### Instructions

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

---

###Example 1:

```
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
```
###Example 2:
```
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
```
### Solution

```py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val} -> {self.next}'

def linked_list_size(head: ListNode | None) -> int:
    size = 0
    while head:
        size += 1
        head = head.next
    return size

def linked_list_get(head: ListNode | None, ind: int) -> ListNode | None:
    while head:
        if ind == 0:
            break
        head = head.next
        ind -= 1
    return head

def linked_list_remove(prev_node: ListNode | None) -> None:
    prev_node.next = prev_node.next.next

def deleteMiddle(head: ListNode|None) -> ListNode|None:
    size = linked_list_size(head)
    if size <= 1:
        return None
    ind = size // 2 - 1
    middle = linked_list_get(head, ind)
    linked_list_remove(middle)
    return head
```
* Time Complexity: 0(n)
* Space Complexity: O(1)

See other solutions in the Python file.

* [Source from Leetcode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75)