from collections import Counter

def isValidSudoku(board: list[list[str]]) -> bool:
    def check(elems: list[str]) -> bool:
        d = Counter(elems)
        def ref():
            for k, v in d.items():
                if k == ".":
                    yield True
                else:
                    yield v<=1

        return all(ref())    

    for row in board:
        if not check(row):
            return False 
    
    for row in board:
        column = []
        for i in range(9):
            column.append(row[i])
        if not check(column):
            return False 
        
    for a, b in ((0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)):
        box = []
        for c in range(3):
            for d in range(3):
                box.append(board[a+c][b+d])
        if not check(box):
            return False 
    return True

        

print(isValidSudoku([["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]))


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
            not check(
                [board[a + c][b + d] for c in range(3) for d in range(3)]
            ) for a, b in ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6))
        ):
            return False
        
        return True
