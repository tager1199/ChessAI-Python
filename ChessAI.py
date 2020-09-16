#-------------------------------------------------------------------------------
# Name:        ChessAI
# Purpose:
#
# Author:      Thomas Ager
#
# Created:     14/09/2020
# Copyright:   (c) Thomas 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class ChessPieces:
  def __init__(self, name, points, x, y, colour):
    self.name = name
    self.points = points
    self.x = x
    self.y = y
    self.pos = [x,y]
    self.colour = colour

    def validMoves():
        pass

scores = {
"K": 99,
"Q": 9,
"R": 5,
"B": 3,
"N": 3,
"p": 1,
}
pieces = []
rows = []
def createPieces():
    global pieces
    blackP1 = ChessPieces("Pawn",1,0,6,"black")
    blackP2 = ChessPieces("Pawn",1,1,6,"black")
    blackP3 = ChessPieces("Pawn",1,2,6,"black")
    blackP4 = ChessPieces("Pawn",1,3,6,"black")
    blackP5 = ChessPieces("Pawn",1,4,6,"black")
    blackP6 = ChessPieces("Pawn",1,5,6,"black")
    blackP7 = ChessPieces("Pawn",1,6,6,"black")
    blackP8 = ChessPieces("Pawn",1,7,6,"black")
    blackN1 = ChessPieces("Knight",3,1,7,"black")
    blackN2 = ChessPieces("Knight",3,6,7,"black")
    blackB1 = ChessPieces("Bishop",3,2,7,"black")
    blackB2 = ChessPieces("Bishop",3,5,7,"black")
    blackR1 = ChessPieces("Rook",5,0,7,"black")
    blackR2 = ChessPieces("Rook",5,7,7,"black")
    blackQ = ChessPieces("Queen",5,3,7,"black")
    blackK = ChessPieces("King",5,4,7,"black")
    whiteP1 = ChessPieces("Pawn",1,0,1,"white")
    whiteP2 = ChessPieces("Pawn",1,1,1,"white")
    whiteP3 = ChessPieces("Pawn",1,2,1,"white")
    whiteP4 = ChessPieces("Pawn",1,3,1,"white")
    whiteP5 = ChessPieces("Pawn",1,4,1,"white")
    whiteP6 = ChessPieces("Pawn",1,5,1,"white")
    whiteP7 = ChessPieces("Pawn",1,6,1,"white")
    whiteP8 = ChessPieces("Pawn",1,7,1,"white")
    whiteN1 = ChessPieces("Knight",3,1,0,"white")
    whiteN2 = ChessPieces("Knight",3,6,0,"white")
    whiteB1 = ChessPieces("Bishop",3,2,0,"white")
    whiteB2 = ChessPieces("Bishop",3,5,0,"white")
    whiteR1 = ChessPieces("Rook",5,0,0,"white")
    whiteR2 = ChessPieces("Rook",5,7,0,"white")
    whiteQ = ChessPieces("Queen",5,3,0,"white")
    whiteK = ChessPieces("King",5,4,0,"white")
    pieces = [whiteP1,whiteP2,whiteP3,whiteP4,whiteP5,whiteP6,whiteP7,whiteP8,whiteN1,whiteN2,whiteB1,whiteB2,whiteR1,whiteR2,whiteQ,whiteK,blackP1,blackP2,blackP3,blackP4,blackP5,blackP6,blackP7,blackP8,blackN1,blackN2,blackB1,blackB2,blackR1,blackR2,blackQ,blackK]

def drawBoard():
    for x in range(8):
        rows.append([' ',' ',' ',' ',' ',' ',' ',' '])
    for i in pieces:
        if i.name == "Knight":
            if i.colour =="white":
                rows[(7-i.y)][i.x] = 'WN'
            else:
                rows[(7-i.y)][i.x] = 'N'
        else:
            rows[(7-i.y)][i.x] = i.name[0]


def main():
    createPieces()
    drawBoard()
    for x in rows:
        print(*x)

if __name__ == '__main__':
    main()
