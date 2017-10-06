from boardClass import *
import os

def main():
    print("Welcome to checkersLite!")
    print("Be sure to read instructions in Notes.txt")
    input("Press enter to start!")
    gameLoop()
    
def gameLoop():
    os.system('cls')
    gameBoard = Board()
    currPlayer = gameBoard.currPlayer
    while(True):
        gameBoard.printBoard()
        inp = input("Player{0}, enter a move: \n".format(currPlayer))
        args = parseInput(inp)
        if (args[0] == "move"):
            gameBoard.move(gameBoard.currPlayer, args[1], args[2])
            currPlayer = gameBoard.currPlayer
            os.system('cls')
        elif (args[0] == "jump"):
            gameBoard.jump(gameBoard.currPlayer, args[1], args[2])
            while (currPlayer == gameBoard.currPlayer):
                os.system('cls')
                gameBoard.printBoard()
                inp = input("Player{0}, jump again: \n".format(currPlayer))
                args = parseInput(inp)
                gameBoard.jump(gameBoard.currPlayer, args[1], args[2])
            currPlayer = gameBoard.currPlayer
            os.system('cls')

def parseInput(string):
    spArr = string.split(" ")
    tup1 = spArr[1][1:-1].split(",")
    tup2 = spArr[2][1:-1].split(",")
    return [spArr[0], (int(tup1[0]), int(tup1[1])), (int(tup2[0]), int(tup2[1]))]

if __name__ == "__main__": main()