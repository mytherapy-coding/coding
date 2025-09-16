def opposite(number: float) -> float:
    return -number


def test_opposite():

    tab: tuple[tuple[float, float], ...] = (
        (4, -4),
        (5, -5),
        (3, -3),
        (5, -5),
        (19, -19),
        (0, 0),
        (-16, 16),
        (-4, 4),
        (-45, 45),
        (98, -98),
        (0.87, -0.87),
        (34, -34),
        (-76, 76),
        (-34, 34),
        (-2398, 2398),
        (76.9, -76.9),
        (654, -654),
    )

    for number, expected in tab:
        result = opposite(number)
        assert result == expected, f"failed test on ({number}, {expected=}, {result=}"

    print("end of tests")


test_opposite()
