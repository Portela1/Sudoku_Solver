import pprint

def fullBoard(Board):
        for i in range(0,9):
                for j in range(0,9):
                        if Board[i][j] == 0:
                                return False
        return True


def possibleNum(Board, i, j):

        possiblesArray = {}

        for p in range (1,10):
                possiblesArray[p] = 0

        for y in range (0,9):
                if not Board[i][y] == 0:
                        possiblesArray[Board[i][y]] = 1
        
        for x in range (0,9):
                if not Board[x][j] == 0:
                        possiblesArray[Board[x][j]] = 1
        
        
        l = i - (i%3)
        r = j - (j%3)

        for c in range (l,l+3):
                for v in range(r,r+3):
                        if not Board[c][v] == 0:
                                possiblesArray[Board[c][v]] = 1

        for p in range (1,10):
                if possiblesArray[p] == 0:
                        possiblesArray[p] = p
                else:
                        possiblesArray[p] = 0

        return possiblesArray






board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7],
        ]


printPretty = pprint.PrettyPrinter(width=41,compact=True)
printPretty.pprint(board)

