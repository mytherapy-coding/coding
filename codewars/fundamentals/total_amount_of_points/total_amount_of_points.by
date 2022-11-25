def points1(games: list[str]) -> int:
    total = 0
    for game in games:
        x = int(game[0])
        y = int(game[2])
        if x > y:
            total += 3
        elif x == y:
            total += 1

    return total


def points2(games: list[str]) -> int:
    total = 0
    for sx, _, sy in games:
        x, y = int(sx), int(sy)
        if x > y:
            total += 3
        elif x == y:
            total += 1

    return total


def points3(games: list[str]) -> int:
    res: list[tuple[int, int]] = []
    for game in games:
        x = int(game[0])
        y = int(game[2])
        res.append((x, y))

    total = 0
    for x, y in res:
        if x > y:
            total += 3
        elif x == y:
            total += 1

    return total


def points4(games: list[str]) -> int:
    res = ((int(game[0]), int(game[2])) for game in games)
    return sum(3 if x > y else 1 if x == y else 0 for x, y in res)


def points5(games: list[str]) -> int:
    res = ((int(sx), int(sy)) for sx, _, sy in games)
    return sum(3 if x > y else 1 if x == y else 0 for x, y in res)


def points6(games: list[str]) -> int:
    res = ([int(e) for e in game.split(':')] for game in games)
    return sum(3 if x > y else 1 if x == y else 0 for x, y in res)


def points7(games: list[str]) -> int:
    return sum(3 if x > y else 1 if x == y else 0 for x, y in ((int(game[0]), int(game[2])) for game in games))


def points8(games: list[str]) -> int:
    return sum(3 if x > y else 1 if x == y else 0 for x, y in ([int(e) for e in game.split(':')] for game in games))


def points9(games: list[str]) -> int:
    return sum(3 * (x > y) + (x == y) for x, y in ([int(e) for e in game.split(':')] for game in games))


def points10(games: list[str]) -> int:
    return sum(3 * (int(x) > int(y)) + (x == y) for x, y in (game.split(':') for game in games))


def points11(games: list[str]) -> int:
    return sum(3 * (sx > sy) + (sx == sy) for sx, _, sy in games)


def test_points():
    from collections.abc import Callable

    tab: tuple[tuple[list[str], int], ...] = (
        ([], 0),
        (["0:0"], 1),
        (["1:0"], 3),
        (["0:1"], 0),
        (["2:1"], 3),
        (["1:2", "0:0"], 1),
        (["2:1", "2:2", "0:1"], 4),
        (["1:3", "3:2", "3:1"], 6),
        (["10:5", "3:7", "8:4"], 6),
    )
    funcs: tuple[Callable[list[str], int], ...] = (
        points1,
        points2,
        points3,
        points4,
        points5,
        points6,
        points7,
        points8,
        points9,
        points10,
    )
    skip_if_high_score: tuple[Callable[list[str], int], ...] = (
        points1,
        points2,
        points3,
        points4,
        points5,
        points7,
    )

    def is_score_high(games: list[str]) -> bool:
        for game in games:
            if len(game) > 3:
                return True
        return False

    #  return any(len(game) > 3 for game in games)

    for f in funcs:
        for games, expected in tab:
            if not is_score_high(games) or f not in skip_if_high_score:
                result = f(games)
                assert result == expected, f'test failed on {f.__name__}({games}, {expected=}, {result=}'


test_points()

