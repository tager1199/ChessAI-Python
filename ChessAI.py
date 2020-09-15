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
  def __init__(self, name, points, x, y):
    self.name = name
    self.points = points
    self.pos = [x,y]


scores = {
"K": 99,
"Q": 9,
"R": 5,
"B": 3,
"N": 3,
"p": 1,
}
pieces = ['K','Q','R','B','N','p']
rows = []
def createBoard():
    for x in range(8):
        if (x == 0 or x == 7):
            rows.append(['R','N','B','Q','K','B','N','R'])
        elif (x == 1 or x == 6):
            rows.append(['p','p','p','p','p','p','p','p'])
        else:
            rows.append([' ',' ',' ',' ',' ',' ',' ',' '])

def drawBoard():
    for i in rows:
        line = "|"
        for j in i:
            line += j + '|'
        print(line)

def main():
    createBoard()
    drawBoard()

if __name__ == '__main__':
    main()
