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
    self.validMoves = []



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

def validMoves(piece):
    piece.validMoves = []
    moves = []
    whiteLocs = []
    blackLocs = []
    for x in pieces:
        if x.colour == "black":
            blackLocs.append([x.x,x.y])
        else:
            whiteLocs.append([x.x,x.y])

    if piece.name == "Pawn":
        if piece.colour == "white":
            change = 1
            if [piece.x + 1, piece.y + 1] in blackLocs:
                moves.append([piece.x + 1, piece.y + 1])
            if [piece.x - 1, piece.y + 1] in blackLocs:
                moves.append([piece.x - 1, piece.y + 1])
        elif piece.colour == "black":
            change = -1
            if [piece.x + 1, piece.y - 1] in blackLocs:
                moves.append([piece.x + 1, piece.y - 1])
            if [piece.x - 1, piece.y - 1] in blackLocs:
                moves.append([piece.x - 1, piece.y - 1])
        if [piece.x, piece.y + change] not in blackLocs and [piece.x, piece.y + change] not in whiteLocs:
            moves.append([piece.x, piece.y + change])
        if ((piece.y == 1 and piece.colour == "white") or (piece.y == 6 and piece.colour == "black"))and [piece.x, piece.y + (2*change)] not in blackLocs and [piece.x, piece.y + (2*change)] not in whiteLocs:
            moves.append([piece.x, piece.y + (2*change)])

    elif piece.name == "Knight":
        moves.append([piece.x + 2, piece.y + 1])
        moves.append([piece.x + 2, piece.y - 1])
        moves.append([piece.x - 2, piece.y + 1])
        moves.append([piece.x - 2, piece.y - 1])
        moves.append([piece.x + 1, piece.y + 2])
        moves.append([piece.x + 1, piece.y - 2])
        moves.append([piece.x - 1, piece.y + 2])
        moves.append([piece.x - 1, piece.y - 2])
        for i in moves:
            if piece.colour == "white":
                if i in whiteLocs:
                    moves.remove(i)
            else:
                if i in blackLocs:
                    moves.remove(i)

    elif piece.name == "Bishop":
        UL = True
        UR = True
        DL = True
        DR = True
        for i in range(8):
            if UL == True:
                if [piece.x + i, piece.y - i] in blackLocs:
                    if piece.colour == "black":
                        UL = False
                    else:
                        moves.append([piece.x + i, piece.y - i])
                        UL = False
                elif [piece.x + i, piece.y - i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x + i, piece.y - i])
                        UL = False
                    else:
                        UL = False
                else:
                    moves.append([piece.x + i, piece.y - i])
            if UR == True:
                if [piece.x + i, piece.y + i] in blackLocs:
                    if piece.colour == "black":
                        UR = False
                    else:
                        moves.append([piece.x + i, piece.y + i])
                        UR = False
                elif [piece.x + i, piece.y + i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x + i, piece.y + i])
                        UR = False
                    else:
                        UR = False
                else:
                    moves.append([piece.x + i, piece.y + i])
            if DR == True:
                if [piece.x - i, piece.y + i] in blackLocs:
                    if piece.colour == "black":
                        DR = False
                    else:
                        moves.append([piece.x - i, piece.y + i])
                        DR = False
                elif [piece.x - i, piece.y + i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x - i, piece.y + i])
                        DR = False
                    else:
                        DR = False
                else:
                    moves.append([piece.x - i, piece.y + i])
            if DL == True:
                if [piece.x - i, piece.y - i] in blackLocs:
                    if piece.colour == "black":
                        DL = False
                    else:
                        moves.append([piece.x - i, piece.y - i])
                        DL = False
                elif [piece.x - i, piece.y - i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x - i, piece.y - i])
                        DL = False
                    else:
                        DL = False
                else:
                    moves.append([piece.x - i, piece.y - i])

    elif piece.name == "Rook":
        U = True
        D = True
        L = True
        R = True
        for i in range(8):
            if R == True:
                if [piece.x+i,piece.y] in blackLocs:
                    if piece.colour == "black":
                        R = False
                    else:
                        moves.append([piece.x+i,piece.y])
                        R = False
                elif [piece.x+i,piece.y] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x+i,piece.y])
                        R = False
                    else:
                        R = False
                else:
                    moves.append([piece.x+i,piece.y])

            if U == True:
                if [piece.x,piece.y+i] in blackLocs:
                    if piece.colour == "black":
                        U = False
                    else:
                        moves.append([piece.x,piece.y+i])
                        U = False
                elif [piece.x,piece.y+i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x,piece.y+i])
                        U = False
                    else:
                        U = False
                else:
                    moves.append([piece.x,piece.y+i])

            if L == True:
                if [piece.x-i,piece.y] in blackLocs:
                    if piece.colour == "black":
                        U = False
                    else:
                        moves.append([piece.x-i,piece.y])
                        U = False
                elif [[piece.x-i,piece.y]] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x-i,piece.y])
                        U = False
                    else:
                        U = False
                else:
                    moves.append([piece.x-i,piece.y])

            if D == True:
                if [piece.x,piece.y-i] in blackLocs:
                    if piece.colour == "black":
                        D = False
                    else:
                        moves.append([piece.x,piece.y-i])
                        D = False
                elif [piece.x,piece.y-i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x,piece.y-i])
                        D = False
                    else:
                        D = False
                else:
                    moves.append([piece.x,piece.y-i])

    elif piece.name == "Queen":
        U = True
        D = True
        L = True
        R = True
        UL = True
        UR = True
        DL = True
        DR = True
        for i in range(8):
            if U == True:
                if [piece.x,piece.y+i] in blackLocs:
                    if piece.colour == "black":
                        U = False
                    else:
                        moves.append([piece.x,piece.y+i])
                        U = False
                elif [piece.x,piece.y+i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x,piece.y+i])
                        U = False
                    else:
                        U = False
                else:
                    moves.append([piece.x,piece.y+i])

            if D == True:
                if [piece.x,piece.y-i] in blackLocs:
                    if piece.colour == "black":
                        D = False
                    else:
                        moves.append([piece.x,piece.y-i])
                        D = False
                elif [piece.x,piece.y-i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x,piece.y-i])
                        D = False
                    else:
                        D = False
                else:
                    moves.append([piece.x,piece.y-i])

            if L == True:
                if [piece.x-i,piece.y] in blackLocs:
                    if piece.colour == "black":
                        L = False
                    else:
                        moves.append([piece.x-i,piece.y])
                        L = False
                elif [piece.x-i,piece.y] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x-i,piece.y])
                        L = False
                    else:
                        L = False
                else:
                    moves.append([piece.x-i,piece.y])

            if R == True:
                if [piece.x+i,piece.y] in blackLocs:
                    if piece.colour == "black":
                        R = False
                    else:
                        moves.append([piece.x+i,piece.y])
                        R = False
                elif [piece.x+i,piece.y] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x+i,piece.y])
                        R = False
                    else:
                        R = False
                else:
                    moves.append([piece.x+i,piece.y])

            if UL == True:
                if [piece.x - i,piece.y+i] in blackLocs:
                    if piece.colour == "black":
                        UL = False
                    else:
                        moves.append([piece.x - i,piece.y+i])
                        UL = False
                elif [piece.x - i,piece.y+i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x - i,piece.y+i])
                        UL = False
                    else:
                        UL = False
                else:
                    moves.append([piece.x - i,piece.y+i])
            if UR == True:
                if [piece.x + i,piece.y+i] in blackLocs:
                    if piece.colour == "black":
                        UR = False
                    else:
                        moves.append([piece.x + i,piece.y+i])
                        UR = False
                elif [piece.x + i,piece.y+i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x + i,piece.y+i])
                        UR = False
                    else:
                        UR = False
                else:
                    moves.append([piece.x + i,piece.y+i])

            if DL == True:
                if [piece.x - i, piece.y - i] in blackLocs:
                    if piece.colour == "black":
                        DL = False
                    else:
                        moves.append([piece.x - i, piece.y - i])
                        DL = False
                elif [piece.x - i, piece.y - i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x - i, piece.y - i])
                        DL = False
                    else:
                        DL = False
                else:
                    moves.append([piece.x - i, piece.y - i])

            if DR == True:
                if [piece.x + i, piece.y - i] in blackLocs:
                    if piece.colour == "black":
                        DR = False
                    else:
                        moves.append([piece.x + i, piece.y - i])
                        DR = False
                elif [piece.x + i, piece.y - i] in whiteLocs:
                    if piece.colour == "black":
                        moves.append([piece.x + i, piece.y - i])
                        DR = False
                    else:
                        DR = False
                else:
                    moves.append([piece.x + i, piece.y - i])

    deleteIndex = []
    for i in moves:
        if i[0] not in range(0, 8):
            deleteIndex.append(moves.index(i))

        elif i[1] not in range(0, 8):
            deleteIndex.append(moves.index(i))

    for i in sorted(deleteIndex, reverse = True):
        del moves[i]

    piece.validMoves = moves

def kingMoves():
    blackMoves = []
    whiteMoves = []
    moves = []
    for i in pieces:
        if piece.colour == "black" and piece.name != "King":
            blackMoves.extend(piece.validMoves)
        elif piece.colour == "white" and piece.name != "King":
            whiteMoves.extend(piece.validMoves)
    blackKing = pieces[15]
    whiteKing = pieces[-1]
    moves = [[blackKing.x + 1, blackKing.y + 1],[blackKing.x + 1, blackKing.y - 1],[blackKing.x + 1, blackKing.y],[blackKing.x - 1, blackKing.y + 1],[blackKing.x - 1, blackKing.y - 1],[blackKing.x - 1, blackKing.y],[blackKing.x, blackKing.y + 1],[blackKing.x, blackKing.y - 1]]
    for i in moves:
        if i in whiteMoves:
            moves.remove(i)
    blackKing.validMoves = moves
    moves = [[whiteKing.x + 1, whiteKing.y + 1],[whiteKing.x + 1, whiteKing.y - 1],[whiteKing.x + 1, whiteKing.y],[whiteKing.x - 1, whiteKing.y + 1],[whiteKing.x - 1, whiteKing.y - 1],[whiteKing.x - 1, whiteKing.y],[whiteKing.x, whiteKing.y + 1],[whiteKing.x, whiteKing.y - 1]]
    for i in moves:
        if i in blackMoves:
            moves.remove(i)
    whiteKing.validMoves = moves


def drawBoard():
    global rows
    rows = []
    for x in range(8):
        rows.append([' ',' ',' ',' ',' ',' ',' ',' '])
    for i in pieces:
        if i.name == "Knight":
            rows[(7-i.y)][i.x] = 'N'
        else:
            rows[(7-i.y)][i.x] = i.name[0]
    for x in rows:
        print(*x)


def playerTurn():
    pass

def aiTurn():
    test = []
    for i in pieces:
        validMoves(i)
        print(i.validMoves)


def main():
    createPieces()
    #while True:
    drawBoard()
    aiTurn()


if __name__ == '__main__':
    main()
