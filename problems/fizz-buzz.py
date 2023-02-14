for e in range(20):
    if e%3 == 0 and e%5 == 0:
        print(f'fizz-buzz = {e}')
    elif e%3 == 0:
        print(f'fizz = {e}')
    elif e%5 == 0:
        print(f'buzz = {e}')
