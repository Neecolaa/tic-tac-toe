
class gameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[' '] * size for i in range(size)]
        self.cellsFilled = 0
        
    def printBoard(self):
        rows = list(map(lambda r: " "+" | ".join(r), self.board))#generates list of rows with |
        #^idk if this is the best/cleanest way to do this
        board = ("\n"+("--- "*self.size)+"\n").join(rows)#adds horizontal lines between rows
        print(board)
    
    def checkForWin(self):
        #horizontal check
        self.board[0][0] = '3'
        self.board[1][1] = '4'
        self.board[2][2] = '6'
        #vertical check
        col = [row[1] for row in self.board]
        print(col)
        #diagonal check
    
    #def checkRow(row):
        s = set(self.board[0])
        print(s)
        if len(s) == 1 and ' ' not in s:
            print(True)
        else:
            print(False)

class game:
    def __init__(self) -> None:
        pass
    
board = gameBoard(3)
board.printBoard()
board.checkForWin()
board.printBoard()
