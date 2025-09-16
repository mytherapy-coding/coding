from collections import Counter
from itertools import chain, product


def isValidSudoku(board: list[list[str]]) -> bool:
    def check(elems: list[str]) -> bool:
        return all(k == "." or v <= 1 for k, v in Counter(elems).items())

    return all(
        chain(
            (check(row) for row in board),
            (check(row[i] for row in board) for i in range(9)),
            (
                check(
                    board[3 * a + c][3 * b + d] for d, c in product(range(3), range(3))
                )
                for a, b in product(range(3), range(3))
            ),
        )
    )


print(
    isValidSudoku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
print(
    isValidSudoku(
        [
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
)


def isValidSudoku(self, board: list[list[str]]) -> bool:
    def check(elems: list[str]) -> bool:
        d = Counter(elems)
        return all(v == 1 for k, v in d.items() if k != ".")

        # Check rows
        if any(not check(row) for row in board):
            return False

        # Check columns
        if any(not check([board[row][i] for row in range(9)]) for i in range(9)):
            return False

        # Check 3x3 boxes
        if any(
            not check([board[a + c][b + d] for c in range(3) for d in range(3)])
            for a, b in (
                (0, 0),
                (0, 3),
                (0, 6),
                (3, 0),
                (3, 3),
                (3, 6),
                (6, 0),
                (6, 3),
                (6, 6),
            )
        ):
            return False

        return True
