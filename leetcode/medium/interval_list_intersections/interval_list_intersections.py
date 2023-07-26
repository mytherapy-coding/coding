def intervalIntersection0(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    def intersect(iv1, iv2):
        start1, end1 = iv1
        start2, end2 = iv2
        start = max(start1, start2)
        end = min(end1, end2)
        return [start, end]

    res = []
    for iv1 in firstList:
        for iv2 in secondList:
            iv = intersect(iv1, iv2)
            if iv[1] >= iv[0]:
                res.append(iv)

    return res


def intervalIntersection1(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    def intersect(iv1, iv2):
        return [max(iv1[0], iv2[0]), min(iv1[1], iv2[1])]

    return [iv for iv1 in firstList for iv2 in secondList if (iv := intersect(iv1, iv2))[1] >= iv[0]]


def intervalIntersection2(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    return [iv for iv1 in firstList for iv2 in secondList if (iv := [max(iv1[0], iv2[0]), min(iv1[1], iv2[1])])[1] >= iv[0]]


def intervalIntersection3(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    def intersect(iv1, iv2):
        return [max(iv1[0], iv2[0]), min(iv1[1], iv2[1])]

    res = []
    for iv1 in firstList:
        for iv2 in secondList:
            if iv2[0] > iv1[1]:
                break
            if (iv := intersect(iv1, iv2))[1] >= iv[0]:
                res.append(iv)

    return res


def intervalIntersection4(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    def intersect(iv1, iv2):
        return [max(iv1[0], iv2[0]), min(iv1[1], iv2[1])]

    res = []
    it1 = iter(firstList)
    it2 = iter(secondList)
    try:
        iv1 = next(it1)
        iv2 = next(it2)
        while True:
            iv = intersect(iv1, iv2)
            if iv[1] >= iv[0]:
                res.append(iv)
            if iv2[1] <= iv1[1]:
                iv2 = next(it2)
            else:
                iv1 = next(it1)
    except StopIteration:
        pass

    return res


def intervalIntersection5(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    def intersect(iv1, iv2):
        return [max(iv1[0], iv2[0]), min(iv1[1], iv2[1])]

    res = []
    i = 0
    j = 0
    while i < len(firstList) and j < len(secondList):
        iv1 = firstList[i]
        iv2 = secondList[j]
        iv = intersect(iv1, iv2)
        if iv[1] >= iv[0]:
            res.append(iv)
        if iv2[1] <= iv1[1]:
            j += 1
        else:
            i += 1

    return res


firstList = [[1,3],[5,9]]
secondList = [[3, 5]]
print(intervalIntersection5(firstList, secondList))