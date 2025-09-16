def test():
    tab = (([0] * 10, 4, True),)

    funcs = (canPlaceFlowers0,)
    for func in funcs:
        for flowerbed, n, expected in tab:
            # print(flowerbed, n, expected)
            result = func(flowerbed, n)
            assert (
                result == expected
            ), f"{func.__qualname__}({flowerbed}, {n}): {result=}, {expected=}"


test()
