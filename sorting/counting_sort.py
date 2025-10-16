def counting_sort(balls: list):
    i = 0
    n = len(balls)
    j = n - 1
    while i < j:
        if balls[i] == 1 and balls[j] == 0:
            balls[i], balls[j] = balls[j], balls[i]
            i += 1
            j -= 1
        if balls[i] == 0 and balls[j] == 0:
            i +=1
        if balls[i] == 1 and balls[j] == 1:
            j -= 1
        if balls[i] == 0 and balls[j] == 1:
            i += 1
            j -= 1
balls = [0, 1, 1, 1, 1, 1, 0, 0]
counting_sort(balls)
print(balls)

def sort_012(arr):
    low = 0           # next position for 0
    mid = 0           # current element
    high = len(arr) - 1  # next position for 2

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example usage
arr = [0, 2, 1, 2, 0, 1, 0]
sorted_arr = sort_012(arr)
print(sorted_arr)


