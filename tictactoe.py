
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
        return board
    
    def printOptions(self):    
        #determine size of cells
        cellSize = len(str(self.size * self.size))
        
        #create options table
        options = [[''] * self.size for i in range(self.size)]
        
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != ' ':
                    #add symbol to cell
                    options[i][j] = str.center(self.board[i][j],cellSize)
                else:
                    #add cell number to cell
                    options[i][j] = str.center(str(self.size*i+j+1),cellSize)
        
        rows = list(map(lambda r: " "+" | ".join(r), options))#generates list of rows with |
        #^idk if this is the best/cleanest way to do this
        pboard = ("\n"+(("-"*(cellSize+2))+" ")*self.size+"\n").join(rows)#adds horizontal lines between rows
        print(pboard)
        
        return cellSize
    
    def fillCell(self,cellNum, symbol):
        #find row and col from cellNum
        cellNum = int(cellNum)
        row = (cellNum-1)//self.size
        col = (cellNum-1)%self.size
        
        #make sure cell is in board
        if row >= self.size or col >= self.size:
            return False
        
        #check if cell is empty
        if self.board[row][col] == ' ':
            #if empty add symbol to cell
            self.board[row][col] = symbol
            self.cellsFilled += 1
            return True
        else:
            #else return false w/o adding anything  
            return False             
        
    def checkForWin(self):
        if self.cellsFilled < self.size:
            #no way to win already (technically no win until size*2-1, maybe will change to that)
            return False
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
    
    def isFull(self):
        return (self.cellsFilled == self.size*self.size)

class game:
    def __init__(self):
        self.playerCount = int(input('Input player count: '))
        self.currentPlayerIdx = 0
        self.symbols = self.inputSymbols()
        
        size = int(input('Input board size: '))
        self.board = gameBoard(size)    
    
    def inputSymbols(self):
        symbols = []
        for i in range(self.playerCount):
            symbols.append(input("Input Player "+str(i+1)+"'s symbol: "))
        return symbols   
     
    def play(self):
        gameWon = False
        while gameWon is False and self.board.isFull() is False:
            #show current board + available moves
            self.board.printOptions()
            #get current player's move
            moveValid = False
            while moveValid is False:
                move = input("Player "+str(self.currentPlayerIdx+1)+"'s move: ")
                moveValid = self.board.fillCell(move,self.symbols[self.currentPlayerIdx])
                if moveValid is False:
                    print('Selected move not valid! Please reselect.')
            #check for win
            gameWon = self.board.checkForWin()
            if gameWon is False:
                #move on to next player
                self.currentPlayerIdx = (self.currentPlayerIdx + 1) % self.playerCount
        
        #Game is over
        self.board.printBoard()        
        #Win or tie?
        if gameWon is True:
            print('Player '+str(self.currentPlayerIdx+1)+' wins!')
        elif self.board.isFull() is True:
            print("It's a tie!")
        
        print('GAME OVER')

g = game()
g.play()