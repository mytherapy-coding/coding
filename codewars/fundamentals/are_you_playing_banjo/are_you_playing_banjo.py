def are_you_playing_banjo1(name: str) -> str:
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"


def are_you_playing_banjo2(name: str) -> str:
    s: str
    if name.startswith("R") or name.startswith("r"):
        s = " plays banjo" 
    else:
        s = " does not play banjo"
    return name + s

    
def are_you_playing_banjo3(name: str) -> str:
    s: str = " plays banjo" if name.startswith("R") or name.startswith("r") else " does not play banjo"
    return name + s

    
def are_you_playing_banjo4(name: str) -> str:
    return name + (" plays banjo" if name.startswith("R") or name.startswith("r") else " does not play banjo") 


def are_you_playing_banjo5(name: str) -> str:
    if name[:1] == "R" or name[:1] == "r":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"

    
def are_you_playing_banjo6(name: str) -> str:
    if name[:1] == "R" or name[:1] == "r":
        s = " plays banjo" 
    else:
        s = " does not play banjo"
    return name + s

   
def are_you_playing_banjo7(name: str) -> str:
    s = " plays banjo" if name[:1] == "R" or name[:1] == "r" else " does not play banjo"
    return name + s


def are_you_playing_banjo8(name: str) -> str:
    return name + (" plays banjo" if name[:1] == "R" or name[:1] == "r" else " does not play banjo")


def are_you_playing_banjo9(name: str) -> str:
    return name + (" plays banjo" if name[:1].lower() == "r" else " does not play banjo")

    
def are_you_playing_banjo10(name: str) -> str:
    ok: bool = name.startswith("R") or name.startswith("r")
    d: dict[bool, str] = {
        True: " plays banjo", 
        False: " does not play banjo",
    }
    return name + d[ok]

    
def are_you_playing_banjo11(name: str) -> str:
    ok: bool = name[:1] == "R" or name[:1] == "r"
    d: dict[bool, str] = {
        True: " plays banjo", 
        False: " does not play banjo",
    }
    return name + d[ok]
        

def are_you_playing_banjo12(name: str) -> str:
    ok: bool = name[:1] in ('R', 'r')
    d: dict[bool, str] = {
        True: " plays banjo", 
        False: " does not play banjo",
    }
    return name + d[ok]

    
def are_you_playing_banjo13(name: str) -> str:
    ok: bool = name[:1].lower() == "r"
    d: dict[bool, str] = {
        True: " plays banjo", 
        False: " does not play banjo"
    }
    return name + d[ok]


def are_you_playing_banjo14(name: str) -> str:
    prefix: list[str] = ["R", "r"]
    ok: bool = name[:1] in prefix
    d: dict[bool, str] = {
        True: " plays banjo", 
        False: " does not play banjo"
    }
    return name + d[ok]


def are_you_playing_banjo15(name: str) -> str:
    ok: bool = name[:1] in ("R", "r")
    d: dict[bool, str] = {
        True: " plays banjo", 
        False: " does not play banjo"
    }
    return name + d[ok]


def are_you_playing_banjo16(name: str) -> str:
    ok: bool = name[:1] in "Rr"
    d: dict[bool, str] = {
        True: " plays banjo", 
        False: " does not play banjo"
    }
    return name + d[ok]


def are_you_playing_banjo17(name: str) -> str:
    return name + {
        True: " plays banjo", 
        False: " does not play banjo"
    }[name[:1] in "Rr"]


def are_you_playing_banjo17(name: str) -> str:
    ok: bool = name[:1] in "Rr"
    d: dict[int, str] = {
        1: " plays banjo", 
        0: " does not play banjo"
    }
    return name + d[ok]


def are_you_playing_banjo18(name: str) -> str:
    ok: bool = name[:1] in "Rr"
    d: list[str] = [
        " does not play banjo",
        " plays banjo",
    ]
    return name + d[ok]


def are_you_playing_banjo19(name: str) -> str:
    return name + [
        " does not play banjo",
        " plays banjo",
    ][name[:1] in ('R', 'r')]


def are_you_playing_banjo20(name: str) -> str:
    return name + ' ' + [
        'does not play',
        'plays',
    ][name[:1] in ('R', 'r')] + ' banjo'


def are_you_playing_banjo21(name: str) -> str:
    t: tuple[str, str] = (
        'does not play',
        'plays',
    )
    return f"{name} {t[name[:1] in ('R', 'r')]} banjo"


def are_you_playing_banjo22(name: str) -> str:
    return [
        f'{name} does not play banjo',
        f'{name} plays banjo',
    ][name[:1] in ('R', 'r')]


def test_fare_you_playing_banjo():
    from collections.abc import Callable
    
    tab: tuple[tuple[str, str], ...] = (
        ('', ' does not play banjo'),
        ('J', 'J does not play banjo'),
        ('R', 'R plays banjo'),
        ('Ram', 'Ram plays banjo'),
        ('Sam', 'Sam does not play banjo'),
        ('Slava', 'Slava does not play banjo'), 
    )
    funcs: tuple[Collable[[str], str], ...] = (
        are_you_playing_banjo1,
        are_you_playing_banjo2,
        are_you_playing_banjo3,
        are_you_playing_banjo4,
        are_you_playing_banjo5,
        are_you_playing_banjo6,
        are_you_playing_banjo7,
        are_you_playing_banjo8,
        are_you_playing_banjo9,
        are_you_playing_banjo10,
        are_you_playing_banjo11,
        are_you_playing_banjo12,
        are_you_playing_banjo13,
        are_you_playing_banjo14,
        are_you_playing_banjo15,
        are_you_playing_banjo16,
        are_you_playing_banjo17,
        are_you_playing_banjo18,
        are_you_playing_banjo19,
        are_you_playing_banjo20,
        are_you_playing_banjo21,
        are_you_playing_banjo22,
    )
    skip_if_empty: tuple[Collable[[str], str],...] = (
        are_you_playing_banjo16, 
        are_you_playing_banjo17,
        are_you_playing_banjo18,
    )
    for f in funcs:
        for name, expected in tab:
            if name or f not in skip_if_empty:
                result = f(name)
                assert result == expected, f'test failed on {f.__name__}({name}, {expected=}, {result=}'
        
    print('end of tests')   
    

test_fare_you_playing_banjo()      
