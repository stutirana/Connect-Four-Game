#STUTI RANA
#ID:85039361
import connectfour
from collections import namedtuple
def printboard(board:[]): #this prints the board after the gameState changes
    print('1  2  3  4  5  6  7'.format())
    r = 0
    while connectfour._is_valid_row_number(r):
        for col in board:
            if col[r] == 0:
               print('.  ',end='')
            elif col[r] == 1:
                print('R  ',end='')
            elif col[r] == 2:
                print('Y  ',end='')
        print()
        r+=1
            
        
def checkWin(gameState:namedtuple)->None or str:# I call on this to check if anyone has won
    isWinner = connectfour.winner(gameState)
    someonewon = 'player'
    if isWinner == 1:
        print('CONGRATS ON THE WIN RED')
        return someonewon
    elif isWinner == 2:
        print('CONGRATS ON THE WIN YELLOW')
        return someonewon
    return None


def gameInput():#It gets the user input and sees if it is valid
    while True:
        i = input('please enter a valid input')
        i=i.strip()
        if (i !='' and (i.isspace() == False) and i[len(i)-1].isdigit())\
           and (int(i[len(i)-1])> 0) and (i[0:(len(i)-1)].upper() == 'POP ' or i[0:(len(i)-1)].upper() == 'DROP '):
            command = i.split(' ')

            return command
        print('ERROR')
        
def userMove(gameState: namedtuple, i)->namedtuple:#this changes the gameState and calls on printboard() 
    i[0]= i[0].strip().upper()
    i[1] = int(i[1].strip())-1
    if i[0] == 'POP':
        gameState = connectfour.pop(gameState,i[1])
        printboard(gameState.board)
    elif i[0] == 'DROP': 
        gameState = connectfour.drop(gameState,i[1])
        printboard(gameState.board)
    return gameState
