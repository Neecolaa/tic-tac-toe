class gameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[' ']*size]*size
        
    #def printBoard(self):
    
        
        
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