def kidsWithCandies0(candies: list[int], extraCandies: int) -> list[bool]:
    res = []
    for i in range(len(candies)):
        max_candies = max(candies)
        if candies[i] + extraCandies >= max_candies:
            res.append(True)
        else:
            res.append(False)
    return res


def kidsWithCandies1(candies: list[int], extraCandies: int) -> list[bool]:
    res = []
    max_candies = max(candies)
    for i in range(len(candies)):
        res.append(candies[i] + extraCandies >= max_candies)
    return res


def kidsWithCandies2(candies: list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    return [candies[i] + extraCandies >= max_candies for i in range(len(candies))]


def kidsWithCandies3(candies: list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    return [c + extraCandies >= max_candies for c in candies]


print(kidsWithCandies3([2, 3, 5, 1, 3], 3))
