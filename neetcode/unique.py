import bisect


def unique_numbers(array):
    unique = []
    x = array[0]
    unique.append(x)
    while True:
        ind = bisect.bisect_left(array, x + 1)
        if ind >= len(array):
            break
        unique.append(array[ind])
        x = array[ind]
    return unique


print(unique_numbers([7, 7, 7, 7, 8, 9, 10, 10, 11, 12]))
