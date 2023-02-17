"""
IMPORTS
"""
from random import randint
from math import ceil
from sys import exit

"""
VARIABLES
"""
letters = 'abcdefghijklmnopqrstuvwxyz' # i = 26 i+1
numbers = '0123456789'
bomb = 'B'
flag = 'F'
empty = 'E'
rules = """

Rules Of Bomb Finder :
You dispose of a fully hidden board with cases, each case can or cannot be containing a bomb.
The goal of the game is to find all the bombs without trigering them. You triger a bomb by clicking on a case that hides one.
When you click on a Case, it will reveal what it's hiding.
The case will usually reveal a number, which corresponds to the number of bombs in the 8 surrounding cases.
The case can also reveal an 'E', which means that the 8 surrounding cases don't contain any bomb.

"""


"""
FUNCTIONS
"""
'''
Clears Console
'''



'''
Creates Board
'''
def boardGeneration(difficulty):
    board = []
    for i in range(8*difficulty):
        tempBoard = []
        for j in range(8*difficulty):
            tempBoard.append('X')
        board.append(tempBoard)
    bombs = ceil((8*difficulty)*(8*difficulty)/5)
    randLine = 0
    randCol = 0
    while bombs != 0:
        randLine = randint(0,len(board)-1)
        randCol = randint(0,len(board)-1)
        if board[randLine][randCol] == 'X':
            board[randLine][randCol] = bomb
            bombs -= 1
    tempBoard = []
    for i in range(8*difficulty+2):
        tempTempBoard = []
        for j in range(8*difficulty+2):
            tempTempBoard.append('X')
        tempBoard.append(tempTempBoard)
    for i in range(8*difficulty):
        for j in range(8*difficulty):
            tempBoard[i+1][j+1] = board[i][j]
    counter = 0
    for i in range(1,8*difficulty+1):
        for j in range(1,8*difficulty+1):
            if tempBoard[i][j] != bomb:
                for a in range(i-1,i+2,1):
                    for b in range(j-1,j+2,1):
                        if tempBoard[a][b] == bomb:
                            counter += 1
                tempBoard[i][j] = counter
                counter = 0
    for i in range(8*difficulty):
        for j in range(8*difficulty):
            board[i][j] = tempBoard[i+1][j+1]
    for i in range(8*difficulty):
        for j in range(8*difficulty):
            if board[i][j] == 0:
                board[i][j] = empty
                    
    return board

'''
Prints Board
'''
def printBoard(board):
    if len(board) == 8:
        print("""
    A  B  C  D  E  F  G  H
    ______________________""")
    elif len(board) == 16:
        print("""
    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
    ______________________________________________""")
    else:
        print("""
    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X
    ______________________________________________________________________""")
    for i in range(len(board)):
        if i+1 < 10:    
            line = str(i+1)+'  |'
        else:
            line = str(i+1)+' |'
        for j in range(len(board)):
            line += str(board[i][j])+'  '
        print(line)
    print()
    


'''
Gets, validates and converts to coords an input from player
'''
def getGoodInput(difficulty):
    while 1 == 1:
        move = input("What is your move? ('M' for the move list) > ")
        if move.lower() == 'm':
            print("""
                  
To get the list of Move : 'M'
To Print the Rules : 'R'
To Discorver a Case: '(colomn)(line)', example : 'C7'
To Place a Flag : 'F(colomn)(line)', exmaple : 'FE8'
To Quit : 'Q'
    
                  """)
            return move
        elif move.lower() == 'r':
            print(rules)
            return move
        
        elif move.lower() == 'q':
            quitGame = ''
            while quitGame != 'n' and quitGame != 'N' and quitGame != 'y' and quitGame != 'Y':
                quitGame = input('Do you want to Quit the Game ? (Y/N) > ')
            if quitGame == 'n' or quitGame == 'N':
                return move
            if quitGame == 'y' or quitGame == 'Y':
                print("""
                      
Thank you for playing !
Game Over.
               
                      """)
                exit()
        
        elif (move[0] == 'F' or move[0] == 'f') and (len(move) == 3 or len(move) == 4):
            for i in range(26): 
                if move[1] == letters[i]:
                    for j in range(1,10):
                        if move[2] == numbers[j]:
                            for k in range(10):
                                if len(move) == 4:
                                    if move[3] == numbers[k]:
                                        line = int(move[2]+move[3])-1
                                        col = i
                                        if line >= 0 and line <= difficulty*8:
                                            return [col, line]
                                if len(move) == 3:
                                    line = int(move[2])-1
                                    col = i
                                    if line >= 0 and line <= difficulty*8:
                                        return [col, line]
        elif len(move) == 2 or len(move) == 3:
                for i in range(26): 
                    if move[0] == letters[i]:
                        for j in range(1,10):
                            if move[1] == numbers[j]:
                                for k in range(10):
                                    if len(move) == 3:
                                        if move[2] == numbers[k]:
                                            line = int(move[1]+move[2])-1
                                            col = i
                                            if line >= 0 and line <= difficulty*8:
                                                return [col, line]
                                    if len(move) == 2:
                                        line = int(move[1])-1
                                        col = i
                                        if line >= 0 and line <= difficulty*8:
                                            return [col, line]
                          
                                  
                                            
    
    
      

      
      



"""
GAME
"""
'''
Initialization
'''
move = ''
board = boardGeneration(3)
printBoard(board)

while move == 'r' or move == 'R' or move == 'm' or move == 'M' or move == 'q' or move == 'Q' or move == '':
    move = getGoodInput(3)
    print(move)


'''
Game Loop
'''
