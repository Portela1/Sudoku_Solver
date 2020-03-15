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
        
     
        l = i - i%3
        r = j - j%3

        for x in range (l,l+3):
                for y in range(r,r+3):
                        if not Board[x][y] == 0:
                                possiblesArray[Board[x][y]] = 1

        for x in range (1,10):
                if possiblesArray[x] == 0:
                        possiblesArray[x] = x
                else:
                        possiblesArray[x] = 0

        return possiblesArray


def solve(Board):
        i = 0
        j = 0
        possi = {}
        if fullBoard(board):
                printPretty.pprint(board)
                return
        else:
                for x in range (0,9):
                        for y in range(0,9):
                                if board[x][y] == 0:
                                        i = x
                                        j = y
                                        break
                        else:
                                continue
                        break

                possi = possibleNum(board,i,j)


                for x in range(1,10):
                        if not possi[x] == 0:
                                board[i][j] = possi[x]
                                solve(board)

                board[i][j] = 0




board = [
        [7, 8, 0,   4, 0, 0,   1, 2, 0],
        [6, 0, 0,   0, 7, 5,   0, 0, 9],
        [0, 0, 0,   6, 0, 1,   0, 7, 8],

        [0, 0, 7,   0, 4, 0,   2, 6, 0],
        [0, 0, 1,   0, 5, 0,   9, 3, 0],
        [9, 0, 4,   0, 6, 0,   0, 0, 5],

        [0, 7, 0,   3, 0, 0,   0, 1, 2],
        [1, 2, 0,   0, 0, 7,   4, 0, 0],
        [0, 4, 9,   2, 0, 6,   0, 0, 7],
        ]


printPretty = pprint.PrettyPrinter(width=41,compact=True)
solve(board)

