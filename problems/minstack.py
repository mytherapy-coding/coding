'''
write min stack that supports push, pop, top, empty and get min 
'''

class MinStack:
    def __init__(self):
        self.values = []
        self.minval = []

    def push(self, x):
        self.values.append(x)
        if self.minval:
            self.minval.append(min(self.minval[-1], x))
        else:
            self.minval.append(x)

    def pop(self):
        self.minval.pop()
        return self.values.pop()
    
    
    def top(self):
        return self.values[-1]
    
    def empty(self):
        return not bool(self.values)
    
    def __bool__(self):
        return bool(self.values)
    
    def getmin(self):
        return self.minval[-1]
        

  

stack = MinStack()
print(stack)
print(stack.values)
        
stack.push(10)
stack.push(20)
stack.push(5)
print(stack.values)
print(stack.top())
print(stack.getmin(), "getmin")
x = stack.pop()
print(stack.values)
print(x)
print(stack.getmin(), "getmin")
print(stack.top())
print(stack.empty())
print(stack.pop())
print(stack.empty())

if stack:
    print("Stack is not empty")
else:
    print("Stack is empty")

