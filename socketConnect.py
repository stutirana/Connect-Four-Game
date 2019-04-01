#STUTI RANA
#ID:85039361
import socket
from collections import namedtuple
locationConnection = namedtuple(
    'locationConnection', ['socket', 'inputt', 'output'])

def username()->str:#gets username
    while True: 
        username = input('what is your username?')
        if username != '' and (username.isspace()==False) and (' ' not in username):
            return (username.strip())
def hostname()->str:#gets hostname
    while True:
        hostname=input('what is the host name?')
        if hostname != '' and (hostname.isspace()==False):
            return(hostname.strip())
def portnumber()->int:#gets port
    while True:
        port = input('What is the port number?')
        if port !='' and (port.isspace() == False) and (port.strip().isdigit() == True):
            return (int(port.strip()))
        
def connect():#tries to connect
    host = hostname()
    port = portnumber()
    gameSocket = socket.socket()
    try:
        gameSocket.connect((host,port))
        gameInput = gameSocket.makefile('r')#reads the current board
        gameOutput = gameSocket.makefile('w')#it writes to the board
        return (locationConnection(socket = gameSocket,inputt = gameInput,output = gameOutput))
    except(OSError):
        print('Game was unable to connect to the specified server. BYE!')
        return
            
def haveconnected(connection:locationConnection, username) -> bool or None:#given you have connected moves onto next steop    writeLine(connection, f"I32CFSP_HELLO {username}")
    writeLine(connection, f"I32CFSP_HELLO {username}")
    response = readLine(connection)
    expected = 'WELCOME ' + username
    if response == expected:
        return requestGame(connection)
    else:
        return printErrorMessage(response)
    
def requestGame(connection: locationConnection)-> bool or None:#requests a game with the AI
    writeLine(connection, 'AI_GAME')
    response = readLine(connection)
    expected = 'READY'
    if response == expected:
        return True
    else:
        return printErrorMessage(response)
    
def printErrorMessage(response: str)->None:
    if response.startswith('NO_USER '):
        print('ERROR')
        return

def close (connection:locationConnection)->None:#closes the connection
    connection.inputt.close()
    connection.output.close()
    connection.socket.close()

def writeLine(connection:locationConnection, line:str)-> str:
    connection.output.write(line + '\r\n')
    connection.output.flush()

def readLine(connection:locationConnection)->str:
    return connection.inputt.readline()[:-1]

def run() -> [bool,locationConnection] or None:# is the one fuction that if called runs the connection all the way through
    conn = connect()
    if conn == None:
        return
    bol = haveconnected(conn,username())
    return [bol,conn]


    
