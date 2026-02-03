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
