from boardClass import *
""" My suite of little tests """

# Makes sure the board prints
def testPrint():
    print("TESTING PRINTBOARD") 
    b = Board()
    b.printBoard()
    print()

# Tests a valid move
def testValidMove():
    print("TESTING VALID MOVE")
    b = Board()
    b.printBoard()
    print(b.currPlayer)
    b.move(2, (5, 0), (4, 1))
    b.printBoard()
    print()

# Tests an invalid move
def testInvalidMove():
    print("TESTING INVALID MOVE")
    b = Board()
    b.printBoard()
    print(b.currPlayer)
    b.move(2, (5, 0), (4, 0))
    b.printBoard()
    print()

# Tests an invalid move
def testInvalidPlayer():
    print("TESTING INVALID PLAYER")
    b = Board()
    b.printBoard()
    print(b.currPlayer)
    b.move(1, (5, 0), (4, 0))
    b.printBoard()
    print()

# Tests a valid jump
def testValidJump():
    print("TESTING VALID JUMP")
    b = Board()
    b.printBoard()
    print(b.currPlayer)
    b.move(2, (5, 2), (4, 3))
    b.printBoard()
    b.switchTurn()
    b.move(1, (2, 5), (3, 4))
    b.printBoard()
    b.switchTurn()
    b.jump(2, (4, 3), (2, 5))
    b.printBoard()
    print()

def runAll():
    testPrint()
    testValidMove()
    testInvalidMove()
    testInvalidPlayer()

def main():
    #testValidJump()
    runAll()
    #print("01234"[1:-1])



if __name__ == "__main__": main()
