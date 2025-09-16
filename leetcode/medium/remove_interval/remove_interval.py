def removeInterval0(
    intervals: list[list[int]], toBeRemoved: list[int]
) -> list[list[int]]:
    # O(n) - time complexity
    # O(1) - space complexity
    # Input: intervals = [[0, 2], [3, 4], [5, 7]], toBeRemoved = [1, 6]
    # Output: [[0, 1], [6, 7]]

    def is_intersect(iv1, iv2):
        return max(iv1[0], iv2[0]) < min(iv1[1], iv2[1])  # 15, 20

    # [10, 20] [15, 30]    -[10, 15]
    # [10, 20] [0, 20]     - []
    # [10, 20], [15, 17]   - [10, 15] [17, 20]
    res = []
    for iv in intervals:
        if is_intersect(iv, toBeRemoved):
            iv1 = [iv[0], toBeRemoved[0]]
            iv2 = [toBeRemoved[1], iv[1]]
            for iv0 in iv1, iv2:
                if iv0[1] > iv0[0]:
                    res.append(iv0)
        else:
            res.append(iv)

    return res


def removeInterval(
    intervals: list[list[int]], toBeRemoved: list[int]
) -> list[list[int]]:
    def is_intersect(iv1, iv2):
        return max(iv1[0], iv2[0]) < min(iv1[1], iv2[1])

    res = []
    for iv in intervals:
        if is_intersect(iv, toBeRemoved):
            iv1 = [iv[0], toBeRemoved[0]]
            iv2 = [toBeRemoved[1], iv[1]]
            res.extend(iv0 for iv0 in (iv1, iv2) if iv0[1] > iv0[0])
        else:
            res.append(iv)

    return res


print(removeInterval([[0, 2], [3, 4], [5, 7]], [1, 6]))
