# 1.Reverse Integer
# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.
def solution(x):
    string = str(x)

    if string[0] == "-":
        return int("-" + string[:0:-1])
    else:
        return int(string[::-1])


print(solution(-231))
print(solution(345))

# 2.Average Words Length
# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.


def average(s):
    remove
