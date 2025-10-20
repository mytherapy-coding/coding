'''
write min stack that supports push, pop, top, empty and get min 
'''

class MinStack:
    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)

    def pop(self):
        return self.values.pop()
    
    def top(self):
        return self.values[-1]
    
    def empty(self):
        return not bool(self.values)
    
    def __bool__(self):
        return bool(self.values)

  

stack = MinStack()
print(stack)
print(stack.values)
        
stack.push(10)
stack.push(20)
print(stack.values)
print(stack.top())
x = stack.pop()
print(stack.values)
print(x)
print(stack.top())
print(stack.empty())
print(stack.pop())
print(stack.empty())

if stack:
    print("Stack is not empty")
else:
    print("Stack is empty")