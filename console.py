#STUTI RANA
#ID: 85039361
import sharedFile
import connectfour

def playing():
    #this gets your input and changes the game state until someone wins
    gameState = sharedFile.connectfour.new_game()#makes a new new game board
    while sharedFile.checkWin(gameState) == None:
        i = sharedFile.gameInput()
        try:
            gameState = sharedFile.userMove(gameState,i)
        except (connectfour.InvalidMoveError, ValueError):
            print('ERROR')
            pass
if __name__ == '__main__':
    print('Please enter your command(pop or drop) followed by a space and then a column number between 1 -{}.'.format(connectfour.BOARD_COLUMNS))
    playing()#calls on the playing method
