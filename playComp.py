#STUTI RANA
#ID: 85039361
import socketConnect
import sharedFile
import connectfour
from collections import namedtuple
def validConnection(gameState:namedtuple)->bool or None:#checks if you connected and then starts the game or ends it
    result = socketConnect.run()
    if result == None:
       return
    elif result[0]:
        print('Please enter your command(pop or drop) followed by a space and then a column number between 1 -{}.'.format(connectfour.BOARD_COLUMNS))
        playing(gameState,result)
        socketConnect.close(result[1])
        
def playing(gameState:namedtuple,result):#this alternates the moves and is the general method for playing with the computer
    while True:
        if gameState.turn == 1:
            try:
                i = sharedFile.gameInput()
                gameState = sharedFile.userMove(gameState,i)
                inpt = str(i[0]) + ' '+ str(i[1]+1)
                if sharedFile.checkWin(gameState) != None:
                    return
            except (connectfour.InvalidMoveError, ValueError):
                print('ERROR')
                pass
            except (connectfour.GameOverError):
                print('THE GAME IS OVER')
                return
       
        if gameState.turn == 2:
            try:
                move = compResponse(inpt,result)
                if move == 'RED':
                    print('CONGRATS ON THE WIN RED')
                    return
                elif move == 'YELLOW':
                    print('CONGRATS ON THE WIN YELLOW')
                    return
                elif move == 'INVALID':
                    print('ERROR')
                    return
                else:
                    move = move.split(' ')
                    gameState = moveInturp(move, gameState)#print move and change the board
                    if sharedFile.checkWin(gameState) != None:
                        return
            except (connectfour.GameOverError):
                print('THE GAME IS OVER')
                return
            except (connectfour.InvalidMoveError, ValueError):
                print('The computer made an invalid move.')
                return


def compResponse(inpt,result):#this give the user move to the server and gets back response
    connection = result[1]
    socketConnect.writeLine(connection, inpt)
    firstLine = socketConnect.readLine(connection)
    if firstLine == 'OKAY':
        move = socketConnect.readLine(connection)
        ready = socketConnect.readLine(connection)
        return move
    elif firstLine == 'INVALID':
        ready = socketConnect.readLine(connection)
        return firstLine
    elif 'WINNER' in firstLine:
        winner = firstLine.split('_')[1]
        return winner

def moveInturp(move, gameState:namedtuple)->namedtuple:#given that the computer made a move we print and change the gameState 
    gameState = sharedFile.userMove(gameState,move)
    return gameState
    
  
if __name__ == '__main__':
    gameState = sharedFile.connectfour.new_game()# makes a new board
    validConnection(gameState)# checks if the you connected to the server
    
