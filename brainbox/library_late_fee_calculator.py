def totalPenalty(daysLate):
    total = 0

    for d in daysLate:
        if d == 1:
            total += 1
        elif 2 <= d <= 5:
            total += 2 * d
        else:  # d > 5
            total += 3 * d

    return total

print(totalPenalty([5, 1, 7]))          # 32
print(totalPenalty([1, 1]))             # 2
print(totalPenalty([2, 3, 4, 5]))       # 2*2 + 2*3 + 2*4 + 2*5 = 28
print(totalPenalty([6, 10]))            # 3*6 + 3*10 = 48
print(totalPenalty([]))                 # 0
