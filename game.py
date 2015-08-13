'''
Created on Apr 23, 2015

@author: SARAH NATHANSON
'''
import pygame, sys
from pygame.locals import *
import random

#initialize screen
pygame.init()
HEIGHT=300
WIDTH=400
MARGIN=20
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
rainbow=((255, 0, 0),(255, 127, 0),(255, 255, 0),(0, 255, 0),(0, 0, 255),(255, 0, 0),(255, 127, 0))
RED = (255,0,0)
#fonts
fontObj = pygame.font.Font('freesansbold.ttf', 48)

#game elements

board=["","","","","","","","",""]#X's and O's are capital
#""=blank square
#0|1|2
#3|4|5
#6|7|8
isPlayerTurn=random.choice([True, False]) # is computer turn is not isPlayerTurn #maybe allow user to choose later
playerPiece=random.choice(["X", "O"]) #maybe allow user to choose later
computerPiece= "O" if playerPiece=="X" else "X" #choose opposite of playerPiece

def mainMenu():
    """displays main menu:
    start button
    settings button
    instructions button
    """
    global board
    while True:
        fpsClock.tick(FPS)
        DISPLAYSURF.fill(WHITE)
        drawText("Tic Tac Toe",WIDTH//2,HEIGHT//3,24)
        Rect=drawText("Start",WIDTH//2,HEIGHT//3*2,24,True)
        if pygame.mouse.get_pressed()[0]==True and Rect.top<pygame.mouse.get_pos()[1]<Rect.bottom and Rect.left<pygame.mouse.get_pos()[0]<Rect.right:
            for i in range(30):
                fpsClock.tick(FPS)
            main()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
def settings():
    """display settings
    allows user to pick 'X' 'O' or random
    allows user to pick go first, second or random
    menu button
    """
    
def instructions():
    """display instructions
    menu button
    """
    
def endmenu(won):
    MESSAGES=("You win!","You lose!","It's a tie!")
    global board
    while True:
        fpsClock.tick(FPS)
        DISPLAYSURF.fill(WHITE)
        drawText(MESSAGES[won],WIDTH//2,HEIGHT//3,24)
        Rect=drawText("Play again?",WIDTH//2,HEIGHT//3*2,24,True)
        if pygame.mouse.get_pressed()[0]==True and Rect.top<pygame.mouse.get_pos()[1]<Rect.bottom and Rect.left<pygame.mouse.get_pos()[0]<Rect.right:
            board=["","","","","","","","",""]
            for i in range(30):
                fpsClock.tick(FPS)
            main()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
def drawboard():
    for i in range(WIDTH//3,WIDTH-1,WIDTH//3):
        pygame.draw.line(DISPLAYSURF, BLACK, (i,0+MARGIN), (i,HEIGHT-MARGIN), 1)
    for i in range(HEIGHT//3,HEIGHT-1,HEIGHT//3):
        pygame.draw.line(DISPLAYSURF, BLACK, (0+MARGIN,i), (WIDTH-MARGIN,i), 1)
        
def drawLetter(letter,square):
    if not(letter=="X" or letter=="O"):
        return
    Text=fontObj.render(letter, True, RED if letter=="X" else BLACK)
    Rect=Text.get_rect()
    #assign x and y based on square
    x=WIDTH//6+((WIDTH//3)*(square%3))
    y=HEIGHT//6+((HEIGHT//3)*(square//3))
    Rect.center=(x,y)
    DISPLAYSURF.blit(Text, Rect)

def drawText(text,x,y,size,filled=False):
    fontObj = pygame.font.Font('freesansbold.ttf', size)
    if(filled):
        Text=fontObj.render(text, True, BLACK, RED)
    else:
        Text=fontObj.render(text, True, BLACK)
    Rect=Text.get_rect()
    Rect.center=(x,y)
    DISPLAYSURF.blit(Text, Rect)
    return Rect

def findSquare():
    x=pygame.mouse.get_pos()[0]
    y=pygame.mouse.get_pos()[1]
    if abs(x%(WIDTH//3)-(WIDTH//3))<10 or abs(y%(HEIGHT//3)-(HEIGHT//3))<10: #within 10 pixels of line between square or edge
        return -1 #chooser's square can not be determined
    square=(3*(y//(HEIGHT//3)))+(x//(WIDTH//3))
    return square;

def randomStrategy():
    return random.randrange(9);#returns random square between 0 and 8 inclusive

def goodStrategy():
    """returns the best square for the computer to place their piece on"""
    BESTMOVES =(4,0,2,6,8,1,3,5,7);
    #0|1|2
    #3|4|5
    #6|7|8
    
    #check if you are about to win
    for i in range(3):#check rows
        if(((1 if board[i*3]==computerPiece else 0)+(1 if board[i*3+1]==computerPiece else 0)+(1 if board[i*3+2]==computerPiece else 0))==2):
            if(board[i*3]==""):
                return i*3
            elif(board[i*3+1]==""):
                return i*3+1
            elif(board[i*3+2]==""):
                return i*3+2         
    for i in range(3):#check cols
        if(((1 if board[i]==computerPiece else 0) + (1 if board[i+3]==computerPiece else 0) + (1 if board[i+6]==computerPiece else 0)) == 2):
            if(board[i]==""):
                return i
            elif(board[i+3]==""):
                return i+3
            elif(board[i+6]==""):
                return i+6
    for i in range(2):#check diagonals
        if(((1 if board[i*2]==computerPiece else 0) + (1 if board[4]==computerPiece else 0) + (1 if board[8-(i*2)]==computerPiece else 0)) == 2):
            if(board[i*2]==""):
                return i*2
            elif(board[4]==""):
                return 4
            elif(board[8-(i*2)]==""):
                return 8-(i*2)
    #check if player is about to win
    for i in range(3):#check rows
        if(((1 if board[i*3]==playerPiece else 0)+(1 if board[i*3+1]==playerPiece else 0)+(1 if board[i*3+2]==playerPiece else 0))==2):
            if(board[i*3]==""):
                return i*3
            elif(board[i*3+1]==""):
                return i*3+1
            elif(board[i*3+2]==""):
                return i*3+2         
    for i in range(3):#check cols
        if(((1 if board[i]==playerPiece else 0) + (1 if board[i+3]==playerPiece else 0) + (1 if board[i+6]==playerPiece else 0)) == 2):
            if(board[i]==""):
                return i
            elif(board[i+3]==""):
                return i+3
            elif(board[i+6]==""):
                return i+6
    for i in range(2):#check diagonals
        if(((1 if board[i*2]==playerPiece else 0) + (1 if board[4]==playerPiece else 0) + (1 if board[8-(i*2)]==playerPiece else 0)) == 2):
            if(board[i*2]==""):
                return i*2
            elif(board[4]==""):
                return 4
            elif(board[8-(i*2)]==""):
                return 8-(i*2)
    #pick a square adjacent towards your previous choices
            
    #pick the best possible move
    for i in BESTMOVES:
        if(board[i]==""):
            return i

def hasWon(piece):#piece is "X" or "O" 
    #returns whether there are 3 in the row of piece
    #find non-hardcoded solution later
    return (board[0]==piece and board[1]==piece and board[2]==piece) or \
            (board[3]==piece and board[4]==piece and board[5]==piece) or \
            (board[6]==piece and board[7]==piece and board[8]==piece) or \
            (board[0]==piece and board[3]==piece and board[6]==piece) or \
            (board[1]==piece and board[4]==piece and board[7]==piece) or \
            (board[2]==piece and board[5]==piece and board[8]==piece) or \
            (board[0]==piece and board[4]==piece and board[8]==piece) or \
            (board[2]==piece and board[4]==piece and board[6]==piece)

def boardFull():
    """returns true if board has no empty spots"""
    for i in board:
        if i=="":
            return False;
    return True;

def runGame():
    """runs game"""
    global isPlayerTurn
    global board
    while True:
        fpsClock.tick(FPS)
        DISPLAYSURF.fill(WHITE)
        drawboard();
        for i in range(len(board)):
            drawLetter(board[i],i)
        if hasWon(playerPiece):
            pygame.display.update()
            for i in range(30):
                fpsClock.tick(FPS)
            return 0#player won
        elif hasWon(computerPiece):
            pygame.display.update()
            for i in range(30):
                fpsClock.tick(FPS)
            return 1#computer won
        elif boardFull():
            pygame.display.update()
            for i in range(30):
                fpsClock.tick(FPS)
            return 2#tie
        
        if isPlayerTurn:
            drawText("Player turn", WIDTH//2,HEIGHT-MARGIN,16) 
            square=findSquare();
            if(square!=-1 and pygame.mouse.get_pressed()[0] and board[square]==""):
                board[square]=playerPiece
                isPlayerTurn=not isPlayerTurn
        else:#computer turn
            drawText("Computer turn", WIDTH//2,HEIGHT-MARGIN,16)
            square=goodStrategy();
            if(board[square]==""):
                board[square]=computerPiece
                isPlayerTurn=not isPlayerTurn
        #DISPLAYSURF.blit() 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
   
def main():
    winner=runGame()#0=player 1=computer 2=tie
    endmenu(winner);  
    
if __name__ == '__main__':
    mainMenu()
    main()
    
