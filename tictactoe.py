
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
        for i in range(self.size):
            #horizontal check
            row = self.board[i]
            
            #vertical check
            col = [row[i] for row in self.board]
            
            if self.checkWinSet(row) == True or self.checkWinSet(col) == True:
                return True
            
        #diagonal check
        diagL2R = [self.board[i][i] for i in range(self.size)]
        diagR2L = [self.board[i][self.size-i-1] for i in range(self.size)]
        
        if self.checkWinSet(diagL2R) == True or self.checkWinSet(diagR2L) == True:
            return True
        else:
            return False
    
    def checkWinSet(self,values):
        s = set(values)
        
        if len(s) == 1 and ' ' not in s:
            return True
        else:
            return False

class game:
    def __init__(self) -> None:
        pass
    