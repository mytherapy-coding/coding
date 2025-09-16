# list
friend = [1, 3, 5, 7, 7]
friend.clear()

friends2 = friend.copy()

# guessing game

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

"""
while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("ENTER GUESS: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses, YOU LOSE")
else:
    print("You win")
"""


def raise_to_power(base_num, pow_num):
    res = 1
    for i in range(pow_num):
        res *= base_num
    return res


print(raise_to_power(2, 3))
