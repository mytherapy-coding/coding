def lexicalOrder(n):
    return [int(ch) for ch in sorted(str(e) for e in range(1, n + 1))]


def lexicalOrder1(n):
    return list(map(int, sorted(map(str, range(1, n + 1)))))


print(lexicalOrder1(13))
