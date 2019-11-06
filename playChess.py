import pygame
from board.chessBoard import Board
pygame.init()
gameDisplay=pygame.display.set_mode((800,800))
pygame.display.set_caption("The PY Chess")
clock=pygame.time.Clock()
chessBoard=Board()
chessBoard.createBoard()
chessBoard.printBoard()
allTiles=[]
allPieces=[]
############
def squares(x,y,w,h,color):
    pygame.draw.rect(gameDispaly,color,[x,y,w,h])
    allTiles.apend([color,[x,y,w,h]])
def DrawChessPiece():
    xpos=0
    ypos=0
    color=None
    width=100
    height=100
    black=(66,134,244)
    white=(143,155,175)

    for i in range(8):
        for i in range(8):
            if color%2==0:
                squares(xpos,ypos,width,height,white)
                if not chessBoard.gameTiles[number].pieceOnTile.toString()=='_':
                    img=pygame.image.load("./ChessArt/"
                                          +chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                          +chessBoard.gameTiles[number].pieceOnTile.toString().upper()
                                          +".png")
                    img=pygame.transform.scale(img,(100,100))
                    allPieces.append([img,[xpos,ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos+=1
            else:
                squares(xpos, ypos, width, height, black)
                if not chessBoard.gameTiles[number].pieceOnTile.toString() == '_':
                    img = pygame.image.load("./ChessArt/"
                                            + chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                            + chessBoard.gameTiles[number].pieceOnTile.toString().upper()
                                            + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += 1
            color+=1
            number+=1
        color+=1
        xpos=0
        ypos+=100
############
drawChessPieces()
quitGame=False
while not quitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame=True
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(60)