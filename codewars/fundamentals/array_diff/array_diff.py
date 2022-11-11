
def array_diff1(a: list, b: list) -> list:
    b = set(b)
    return [x for x in a if x not in b]

def array_diff2(a: list, b: list) -> list:
    c = []
    for x in a:
        if x not in b:
            c.append(x)

    return c

def array_diff3(a, b):
    c = []
    b = set(b)
    for x in a:
        if x not in b:
            c.append(x)
    return c
            
tab = (
    ([], [], []),
    ([], [1, 2], []),
    ([10, 20], [], [10, 20]),
    ([3, 6, 7], [7], [3, 6]),
    ([9, 9, 7], [7], [9, 9]),
)

for f in array_diff1, array_diff2, array_diff3:
    for a, b, c in tab:
        assert f(a, b) == c
        print(a,b,c)


