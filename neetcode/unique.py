import bisect


def unique_numbers(array):
    if not array:
        return []
    x = array[0]
    unique = [x]
    while True:
        ind = bisect.bisect_left(array, x + 1)
        if ind >= len(array):
            break
        x = array[ind]
        unique.append(x)
    return unique


print(unique_numbers([7, 7, 7, 7, 8, 9, 10, 10, 11, 12]))


def unique_numbers1(array):
    if not array:
        return []
    x = array[0]
    unique = [x]
    while True:
        ind = bisect.bisect_left(array, x + 1)
        if ind >= len(array):
            break
        x = array[ind]
        unique.append(x)
    return unique


print(unique_numbers1([7, 7, 7, 7, 8, 9, 10, 10, 11, 12]))
