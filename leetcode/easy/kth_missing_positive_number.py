
def findKthPositive(arr: list[int], k: int) -> int:
    # arr = [2,3,4,7,11], k = 5
    # [1,5,6,8,9,10,12,13,...]
    count = 0
    for x in range(1, k + len(arr) + 1):
        if x not in arr:
            count += 1
            if count == k:
                return x
'''
time complexity - O((k + n)*n)
space complexity - O(1)
''' 
def findKthPositive1(arr: list[int], k: int) -> int:
    set_arr = set(arr)
    for x in range(1, k + len(arr) + 1):
        if x not in set_arr:
            k -= 1
            if k <= 0:
                return x




arr = [2,3,4,7,11]
k = 5
kth_number = findKthPositive(arr, k)
print(kth_number)

kth_number = findKthPositive1(arr, k)
print(kth_number)
