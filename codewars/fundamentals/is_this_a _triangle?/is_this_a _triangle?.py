def is_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a

def test_is_triangle():
    
    tab: tuple[tuple[float, float, float, bool], ...] = (
        (4, 3, 7, False),
        (2, 6, 7, True),
        (7, 4, 4, True),
        (0, 0, 0, False),
        (0, 1, 87, False),
        (20, 80, 0, False),
        (3, 6, 9, False),
        (3, 7, 87, False),
        (51, 42, 90, True),
        (4, 76, 5, False),
        (24, 90, 4, False),
        (45, 67, 32, True),
        (0, 8, 0, False),
        (10, -1, -1, False),
        (7, 8, 7, True),
        (9, 10, 4, True),
        (3, 7, 2, False),
        (8, 10, 2, False),
        (4, 10, 9, True),
        (5, -2, -2, False),
        (6, 8, 8, True),
        (2, 7, 8, True),
        (2, 7, -2, False ),
        (0, 4, 3, False),
        (5, 6, 7, True),
        (6, 0, 0, False),
    )

    for a, b, c, expected in tab:
        result = is_triangle(a, b, c)
        assert result == expected, f'failed test on ({a}, {b}, {c}), {expected=}'
    print("end of tests")   
       
    
test_is_triangle()
    
