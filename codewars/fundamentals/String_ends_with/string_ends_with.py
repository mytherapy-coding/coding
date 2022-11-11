def solution1(string, ending):
    return string.endswith(ending)

def solution2(string, ending):
    if len(string) < len(ending):
        return False
    for i in range(len(ending)):
        if ending[i] != string[-len(ending)+i]:
            return False
    return True

tab = (
    ("", "lost", False),
    (";", "", True),
    ("", "", True),
    ("forever", "ever", True),
    ("endswith", "end", False),
    ("love you", "love", False),
    ("timeshare", "share", True),
    ("unrealistic", "realistic", True),
    ("copay", "pay", True),
)

for f in solution1, solution2:
    for string, ending, c in tab:
        assert f(string, ending) == c, f'failed test on {f.__name__}({string}, {ending}), expected {c}'

