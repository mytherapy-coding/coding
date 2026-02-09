def findCenter(edges):
    a, b = edges[0]
    c, d = edges[1]

    if a == c or a == d:
        return a
    return b


def test_findCenter():
    # basic examples
    print(findCenter([[1, 2], [2, 3], [4, 2]]), "== 2")
    print(findCenter([[1, 3], [2, 3], [3, 4]]), "== 3")

    # center is the first number in all edges
    print(findCenter([[5, 1], [5, 2], [5, 3], [5, 4]]), "== 5")

    # minimal case (only two edges)
    print(findCenter([[10, 7], [7, 2]]), "== 7")

    # larger values
    print(findCenter([[100, 1], [50, 100], [100, 3]]), "== 100")

    # symmetric edges (order doesn't matter)
    print(findCenter([[8, 9], [9, 1], [2, 9]]), "== 9")


test_findCenter()
