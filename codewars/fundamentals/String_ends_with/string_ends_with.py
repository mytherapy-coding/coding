def solution(string, ending):
    return string.endswith(ending)



def solution1(a, b):
    for i in range(len(b)):
        if b[i] != a[-len(b)+i]:
            return False
    return True


tab = (
    ("forever", "ever", True),
    ("endswith", "end", True),
    ("love you", "love", True),
    ("timeshare", "share", [True),
    ("unrealistic", "realistic", True),
    ("copay", "pay", True),
)

for f in solution, solution1:
    for a, b, c in tab:
        assert f(a, b) == c, f'failed test on {f.__name__}({a}, {b}), expected {c}'

