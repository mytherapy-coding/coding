from collections import Counter


def equalPairs(grid: list[list[int]]) -> int:
    grid_tuple = (tuple(row) for row in grid)
    count1 = Counter(grid_tuple)
    column_list = [tuple(row[i] for row in grid) for i in range(len(grid))]
    count2 = Counter(column_list)
    total = 0
    for k in count1:
        total += count2[k] * count1[k]
    return total


def equalPairs1(grid: list[list[int]]) -> int:
    count1 = Counter(tuple(row) for row in grid)
    count2 = Counter([tuple(row[i] for row in grid) for i in range(len(grid))])
    total = 0
    for k in count1:
        total += count2[k] * count1[k]
    return total


def equalPairs2(grid: list[list[int]]) -> int:
    count1 = Counter(tuple(row) for row in grid)
    count2 = Counter(tuple(row[i] for row in grid) for i in range(len(grid)))
    return sum(count2[k] * count1[k] for k in count1)


def equalPairs3(grid: list[list[int]]) -> int:
    count1 = Counter(tuple(row) for row in grid)
    return sum(count1[tuple(row[i] for row in grid)] for i in range(len(grid)))


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print(equalPairs3(grid))
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(equalPairs3(grid))
