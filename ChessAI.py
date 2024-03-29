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
import random
import sys
class ChessPieces:
    def __init__(self, name, points, x, y, colour):
        self.name = name
        self.points = points
        self.x = x
        self.y = y
        self.colour = colour
        self.validMoves = []

    def move(self,x,y):
        self.x = x
        self.y = y
        for i in pieces:
            if i.colour != self.colour:
                if i.x == x and i.y == y:
                    print("Piece Taken")
                    taken.append(i)
                    pieces.remove(i)

                    break
        print("moved")

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
taken = []
blackThreat = False
whiteThreat = False

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
    global blackThreat
    global whiteThreat

    piece.validMoves = []
    moves = []
    whiteLocs = []
    blackLocs = []
    wKing = []
    bKing = []
    for x in pieces:
        if x.colour == "black":
            if x.name == "King":
                bKing = [x.x,x.y]
            blackLocs.append([x.x,x.y])
        else:
            if x.name == "King":
                wKing = [x.x,x.y]
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
        if piece.colour == "white":
            Locs = whiteLocs
            notLocs = blackLocs
        else:
            Locs = blackLocs
            notLocs = whiteLocs
        ULBlocked = False
        URBlocked = False
        DLBlocked = False
        DRBlocked = False
        UBlocked = False
        LBlocked = False
        RBlocked = False
        DBlocked = False
        for i in range(1,7):
            if UBlocked == False:
                if [piece.x, piece.y+i] in Locs:
                    UBlocked = True
                elif [piece.x, piece.y+i] in notLocs:
                    moves.append([piece.x, piece.y+i])
                    UBlocked = True
                else:
                    moves.append([piece.x+i, piece.y])
            if LBlocked == False:
                if [piece.x-i, piece.y] in Locs:
                    LBlocked = True
                elif [piece.x-i, piece.y] in notLocs:
                    moves.append([piece.x-i, piece.y])
                    LBlocked = True
                else:
                    moves.append([piece.x-i, piece.y])
            if RBlocked == False:
                if [piece.x+i, piece.y] in Locs:
                    RBlocked = True
                elif [piece.x+i, piece.y] in notLocs:
                    moves.append([piece.x+i, piece.y])
                    RBlocked = True
                else:
                    moves.append([piece.x+i, piece.y])
            if DBlocked == False:
                if [piece.x, piece.y-i] in Locs:
                    DBlocked = True
                elif [piece.x, piece.y-i] in notLocs:
                    moves.append([piece.x, piece.y-i])
                    DBlocked = True
                else:
                    moves.append([piece.x, piece.y-i])
            if URBlocked == False:
                if [piece.x+i, piece.y+i] in Locs:
                    URBlocked = True
                elif [piece.x+i, piece.y+i] in notLocs:
                    moves.append([piece.x+i, piece.y+i])
                    URBlocked = True
                else:
                    moves.append([piece.x+i, piece.y+i])
            if ULBlocked == False:
                if [piece.x+i, piece.y-i] in Locs:
                    ULBlocked = True
                elif [piece.x+i, piece.y-i] in notLocs:
                    moves.append([piece.x+i, piece.y-i])
                    ULBlocked = True
                else:
                    moves.append([piece.x+i, piece.y-i])
            if DRBlocked == False:
                if [piece.x-i, piece.y+i] in Locs:
                    URBlocked = True
                elif [piece.x-i, piece.y+i] in notLocs:
                    moves.append([piece.x-i, piece.y+i])
                    URBlocked = True
                else:
                    moves.append([piece.x-i, piece.y+i])
            if DLBlocked == False:
                if [piece.x-i, piece.y-i] in Locs:
                    DLBlocked = True
                elif [piece.x-i, piece.y-i] in notLocs:
                    moves.append([piece.x-i, piece.y-i])
                    DLBlocked = True
                else:
                    moves.append([piece.x-i, piece.y-i])

    deleteIndex = []
    for i in moves:
        if i == wKing:
            whiteThreat = True
        elif i ==  bKing:
            blackThreat = True
        if i[0] not in range(0, 8) or i[1] not in range(0, 8):
            deleteIndex.append(moves.index(i))


    for i in sorted(deleteIndex, reverse = True):
        del moves[i]

    piece.validMoves = moves

def kingMoves(colour):
    blackMoves = []
    whiteMoves = []
    Bmoves = []
    Wmoves = []
    for i in pieces:
        if i.colour == "black" and i.name != "King":
            blackMoves.extend(i.validMoves)
        elif i.colour == "white" and i.name != "King":
            whiteMoves.extend(i.validMoves)
    blackKing = pieces[15]
    whiteKing = pieces[-1]
    Bmoves = [[blackKing.x + 1, blackKing.y + 1],[blackKing.x + 1, blackKing.y - 1],[blackKing.x + 1, blackKing.y],[blackKing.x - 1, blackKing.y + 1],[blackKing.x - 1, blackKing.y - 1],[blackKing.x - 1, blackKing.y],[blackKing.x, blackKing.y + 1],[blackKing.x, blackKing.y - 1]]


    Wmoves = [[whiteKing.x + 1, whiteKing.y + 1],[whiteKing.x + 1, whiteKing.y - 1],[whiteKing.x + 1, whiteKing.y],[whiteKing.x - 1, whiteKing.y + 1],[whiteKing.x - 1, whiteKing.y - 1],[whiteKing.x - 1, whiteKing.y],[whiteKing.x, whiteKing.y + 1],[whiteKing.x, whiteKing.y - 1]]
    WmovesTemp = Wmoves
    for i in Wmoves:
        if i in blackMoves or Bmoves:
            Wmoves.remove(i)
    for i in Bmoves:
        if i in whiteMoves or WmovesTemp:
            Bmoves.remove(i)
    whiteKing.validMoves = Wmoves
    blackKing.validMoves = Bmoves

def kingCheck(colour):
    print("checking King Protection for", colour)



def drawBoard(colour):
    global rows
    rows = []
    if colour == "white":
        for x in range(8):
            rows.append(['  ','  ','  ','  ','  ','  ','  ','  '])
        for i in pieces:
            if i.colour == 'white':
                if i.name == "Knight":
                    rows[(7-i.y)][i.x] = 'WN'
                else:
                    rows[(7-i.y)][i.x] = 'W'+i.name[0]
            else:
                if i.name == "Knight":
                    rows[(7-i.y)][i.x] = 'BN'
                else:
                    rows[(7-i.y)][i.x] = 'B'+i.name[0]
    else:
        for x in range(8):
            rows.append(['  ','  ','  ','  ','  ','  ','  ','  '])
        for i in pieces:
            if i.name == "Knight":
                rows[(i.y)][i.x] = 'N'
            else:
                rows[(i.y)][i.x] = i.name[0]
    for x in rows:
        print(*x)
    print("\n\n")

def validCheck(piece,newLoc):
    if piece.name != "King":
        validMoves(piece)
    else:
        kingMoves(piece.colour)
    print(piece.validMoves)
    print(newLoc)
    if newLoc in piece.validMoves:
        return True
    else:
        return False

def playerTurn(colour):
    move = input("Players turn, input move \n")
    moved = False
    while (moved == False):
        piece = False
        for i in pieces:
            if i.colour == colour:
                if i.x == int(move[0]) and i.y == int(move[1]):
                    piece = True
                    if (colour == "white" and whiteThreat == True and i.name != "king"):
                        print("You are in Check please protect your King.")
                        break
                    elif (colour == "black" and blackThreat == True and i.name != "king"):
                        print("You are in Check please protect your King.")
                        break
                    if validCheck(i,[int(move[2]),int(move[3])]):
                        i.move(int(move[2]),int(move[3]))
                        moved = True
                    else:
                        print("Invalid move, please try again.")
                        move = input("Players turn, input move \n")
        if piece == False:
            print("You do not have a piece in that location please try again.")
            move = input("Players turn, input move \n")

def aiTurn(colour):
    AllMoves = []
    kingMoves(colour)
    for i in pieces:
        if i.colour == colour:
            validMoves(i)
            if i.validMoves != []:
                AllMoves.append([i,i.validMoves])
    pieceNo = random.randint(0,len(AllMoves)-1)
    moveNo = random.randint(0,len(AllMoves[pieceNo][1])-1)
    AllMoves[pieceNo][0].move(AllMoves[pieceNo][1][moveNo][0],AllMoves[pieceNo][1][moveNo][1])

def checkWin(colour):
    text = ""
    if blackThreat == True:
        print("Blacks King under threat")
        if bKing.validMoves == []:
            if colour == "black":
                text = "Unfortunately you have lost to the AI"
            else:
                text = "Congratulations, you've won and beaten the AI"
            return True
    if whiteThreat == True:
        print("White King under threat")
        if wKing.validMoves == []:
            if colour == "black":
                text = "Congratulations, you've won and beaten the AI"
            else:
                text = "Unfortunately you have lost to the AI"
            return True
    return False

def main():
    global blackThreat
    global whiteThreat
    Win = False
    createPieces()
    AIColour = "black"
    playerColour = input("What colour would you like to play? (Black or White)")
    while playerColour.lower() != "black" and playerColour.lower() != "white":
        playerColour = input("Invalid colour please try again (Black or White)")
    if playerColour.lower() == "black":
        AIColour = "white"
    print("You are playing as", playerColour+",", "the AI is playing as", AIColour)
    turn = 0
    while Win == False:
        turn += 1
        print("turn", turn)
        blackThreat = False
        whiteThreat = False
        drawBoard(playerColour)
        Win = checkWin(playerColour)
        if AIColour == "white":
            aiTurn(AIColour)
            drawBoard(playerColour)
            Win = checkWin(playerColour)
            playerTurn(playerColour)
        else:
            playerTurn(playerColour)
            drawBoard(playerColour)
            Win = checkWin(playerColour)
            aiTurn(AIColour)
        Win = checkWin(playerColour)
    wait = input()

if __name__ == '__main__':
    main()
