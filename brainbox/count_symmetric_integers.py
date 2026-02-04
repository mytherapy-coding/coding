def countSymmetricIntegers(low, high):
    count = 0
    
    for num in range(low, high + 1):
        s = str(num)
        length = len(s)
        
        # Skip odd-length numbers
        if length % 2 != 0:
            continue
        
        mid = length // 2
        left_sum = sum(int(c) for c in s[:mid])
        right_sum = sum(int(c) for c in s[mid:])
        
        if left_sum == right_sum:
            count += 1
    
    return count

print(countSymmetricIntegers(1, 100))        # 9
print(countSymmetricIntegers(10, 99))        # 9
print(countSymmetricIntegers(100, 200))      # 0
print(countSymmetricIntegers(1, 1000))       # 9
print(countSymmetricIntegers(1200, 1300))    # 4
print(countSymmetricIntegers(1000, 9999))    # 615
print(countSymmetricIntegers(11, 11))        # 1
print(countSymmetricIntegers(12, 12))        # 0
print(countSymmetricIntegers(0, 0))          # 0
