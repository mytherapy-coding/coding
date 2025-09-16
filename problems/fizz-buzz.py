for e in range(20):
    if e % 3 == 0 and e % 5 == 0:
        print(f"fizz-buzz = {e}")
    elif e % 3 == 0:
        print(f"fizz = {e}")
    elif e % 5 == 0:
        print(f"buzz = {e}")

for num in range(1, 21):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)

import itertools as its


def fizz_buzz():
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle(["", "", "", "", "Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    print(list(fizzes_buzzes))


fizz_buzz()
