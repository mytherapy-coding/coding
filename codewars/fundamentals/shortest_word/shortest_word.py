def find_short1(s: str) -> int:
    words = s.split()
    res = []
    for w in words:
        res.append(len(w))   
    return min(res, default=0)

def find_short2(s: str) -> int:
    res = []
    for w in s.split():
        res.append(len(w))   
    return min(res, default=0)

def find_short3(s: str) -> int:
    return min((len(w) for w in s.split()), default=0)
    
    
def test_find_short():
    tab: tuple[tuple[str, int], ...] = (
        ('', 0),
        (' ', 0),
        ('Hello world', 5),
        ('Hi', 2),
        (' love you', 3),
        ('.', 1),
        ('    hi  ', 2),
        ('Return the smallest item in an iterable or the smallest of two or more arguments.', 2),
        (' Hello , my friend', 1),
    )
    for f in find_short1, find_short2, find_short3:     
        for s, expected in tab:
            result = f(s)
            assert result == expected, f'test failed on {f.__name__}({s}), {expected=}, {result=}'
        
    print('end of tests')   
    
test_find_short()       
    
