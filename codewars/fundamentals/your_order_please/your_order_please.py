def order0(sentence: str) -> str:
    def getdigit(word: str) -> int:
        for ch in word:
            if ch.isdigit():
                return int(ch)

    res: list[str|None] = [None] * 9
    for word in sentence.split():
        index = getdigit(word)
        res[index - 1] = word
    res = [word for word in res if word is not None]
    return " ".join(res)


def order1(sentence: str) -> str:
    def getdigit(word: str) -> int:
        return next(int(ch) for ch in word if ch.isdigit())

    res: list[str|None] = [None] * 9
    for word in sentence.split():
        res[getdigit(word) - 1] = word
    return " ".join(word for word in res if word is not None)


def order2(sentence: str) -> str:
    def getdigit(word: str) -> int:
        return next(int(ch) for ch in word if ch.isdigit())

    res = {}
    for word in sentence.split():
        res[getdigit(word)] = word
    return " ".join(res[i] for i in range(1, len(res) + 1))


def order3(sentence: str) -> str:
    def getdigit(word: str) -> int:
        return next(int(ch) for ch in word if ch.isdigit())

    res = {getdigit(word): word for word in sentence.split()}
    return " ".join(res[i] for i in range(1, len(res) + 1))


def order4(sentence: str) -> str:
    def getdigit(word: str) -> int:
        return next(int(ch) for ch in word if ch.isdigit())

    res = sentence.split()
    res.sort(key=getdigit)
    return " ".join(res)


def order5(sentence: str) -> str:
    def getdigit(word: str) -> int:
        return next(int(ch) for ch in word if ch.isdigit())

    return " ".join(sorted(sentence.split(), key=getdigit))


def order6(sentence: str) -> str:
    return " ".join(sorted(sentence.split(), key=lambda word: next(ch for ch in word if ch.isdigit())))


def order7(sentence: str) -> str:
    return " ".join(sorted(sentence.split(), key=lambda word: next(filter(str.isdigit, word))))


def test():
    for sentence in "is2 Thi1s T4est 3a", "4of Fo1r pe6ople g3ood th5e the2":
        for order in order0, order1, order2, order3, order4, order5, order6, order7:
            print(order(sentence))
        print()


test()
