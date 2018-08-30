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

# Tests that game recognizes when it's over
def testEndState():
    print("TESTING DETECT END STATE")
    b = Board()
    b.boardArray = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
    b.playerPieces = [ "PLACEHOLDER", {(2, 3)}, {(3, 2)}]
    b.printBoard()
    if (b.isGameOver() != 0):
        print("Error, game should not be over!")
    
    b.jump(2, (3, 2), (1, 4))
    b.printBoard()
    if (b.isGameOver() != 2):
        print("Error, game should be over!")
    print()

def runAll():
    testPrint()
    testValidMove()
    testInvalidMove()
    testInvalidPlayer()
    testEndState()

def main():
    #testValidJump()
    runAll()
    #print("01234"[1:-1])



if __name__ == "__main__": main()
