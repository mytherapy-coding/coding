def twoSum(numbers: list[int], target: int):
    d = {}
    print(enumerate(numbers))
    for i, n in enumerate(numbers):
        d[n] = i + 1
    print(d)

    for x in d:
        y = target - x
        if y in d:
            return d[x], d[y]

print(twoSum[1, 2, 3, 4, 5])