def feast1(beast: str, dish: str) -> bool:
    return beast[0] == dish[0] and beast[-1] == dish[-1]
    
    
def feast2(beast: str, dish: str) -> bool:   
    return (beast[0], beast[-1]) == (dish[0], dish[-1])


def feast3(beast: str, dish: str) -> bool:
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])
 
    
def test_feast():
    tab: tuple[tuple[str, str, bool], ...] = (
        ('peast', 'pit', True),
        ('react', 'rout', True),
        ('from', 'freadom', True),
        ('rome', 'brom', False),
    )
    for f in feast1, feast2, feast3:     
        for beast, dish, expected in tab:
            result = f(beast, dish)
            assert result == expected, f'test failed on {f.__name__}({beast}, {dish}), {expected=}, {result=}'
        
    print('end of tests')   
    
test_feast()       
    
    
