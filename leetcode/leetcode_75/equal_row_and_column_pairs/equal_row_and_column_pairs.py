from collections import Counter


def equalPairs(grid: list[list[int]]) -> int:
    grid_tuple = (tuple(row) for row in grid)
    counter1 = Counter(grid_tuple)
    column_list = [tuple(row[i] for row in grid) for i in range(len(grid))]
    counter2 = Counter(column_list)
    total = 0
    for k in counter1:
        total += counter2[k] * counter1[k]
    return total


def equalPairs1(grid: list[list[int]]) -> int:
    counter1 = Counter(tuple(row) for row in grid)
    counter2 = Counter([tuple(row[i] for row in grid) for i in range(len(grid))])
    total = 0
    for k in counter1:
        total += counter2[k] * counter1[k]
    return total


def equalPairs2(grid: list[list[int]]) -> int:
    counter1 = Counter(tuple(row) for row in grid)
    counter2 = Counter(tuple(row[i] for row in grid) for i in range(len(grid)))
    return sum(counter2[k] * counter1[k] for k in counter1)


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print(equalPairs2(grid))
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(equalPairs2(grid))
