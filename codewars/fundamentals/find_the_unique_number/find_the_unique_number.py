def find_uniq(arr):
    
    if arr[0] == arr[1]:
        cat = arr[1]
    elif arr[1] == arr[2]:
        cat = arr[1]  
    else:
        cat = arr[0]
    for x in arr:
        if x != cat:
            return x

print(find_uniq([1,1,1,3]))            
 
 
# def find_uniq(arr):
#     cat = sorted(arr[:3])[1]
#     return next(x for x in arr if x != cat)
