class gameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[' '] * size for i in range(size)]
        
    def printBoard(self):
        rows = list(map(lambda r: " "+" | ".join(r), self.board))#generates list of rows with |
        #^idk if this is the best/cleanest way to do this
        board = ("\n"+("--- "*self.size)+"\n").join(rows)#adds horizontal lines between rows
        print(board)
        
class playerCells:
    def __init__(self,symbol):
        self.symbol = symbol
        self.spaces = [] #starts off w/o claimed spaces
        
    def claimCell(self,idx):
        self.spaces.append(idx);
    
    #def checkWin(self, winSets):
    #check if any of the win sets are in the player's spaces set
    

class game:
    def __init__(self) -> None:
        pass
    