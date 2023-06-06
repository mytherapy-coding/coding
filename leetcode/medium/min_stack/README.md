# Min Stack

---
### Instructions
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

* MinStack() initializes the stack object.
* void push(int val) pushes the element val onto the stack.
* void pop() removes the element on the top of the stack.
* int top() gets the top element of the stack.
* int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

### Example
```py
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```
---

### Solution

```py
class MinStack:
    def __init__(self):
        self.items = []
        self.minvals = []

    def push(self, val: int) -> None: 
        self.items.append(val) #[1, 4]
        if self.minvals:
            self.minvals.append(min(self.minvals[-1], val)) 
        else:
            self.minvals.append(val)
        
    def pop(self) -> None:
        self.items.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minvals[-1]
```

* Time Complexity: O(1) for each operation.
* Space Complexity: O(1) for each operation.

* [Source from Leetcode](https://leetcode.com/problems/min-stack/)


