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

    # Game loop
    while(True):
        # Show the board
        gameBoard.printBoard()

        # Prompt for input
        inp = input("Player{0}, enter a move: \n".format(currPlayer))
        args = parseInput(inp)
        if (args == None):
            print("Invalid input!\n")
            continue
        if (args[0] == "move"):
            gameBoard.move(gameBoard.currPlayer, args[1], args[2])
            currPlayer = gameBoard.currPlayer
            os.system('cls')
        elif (args[0] == "jump"):
            res = gameBoard.jump(gameBoard.currPlayer, args[1], args[2])
            if (res == -1):
                continue # Jump failed

            # Loop until CURRPLAYER has no more valid jumps
            while (currPlayer == gameBoard.currPlayer):
                os.system('cls')
                gameBoard.printBoard()
                inp = input("Player{0}, jump again: \n".format(currPlayer))
                args = parseInput(inp)
                res = gameBoard.jump(gameBoard.currPlayer, args[1], args[2])
                if (res == -1):
                    break # Jump failed
            currPlayer = gameBoard.currPlayer
            os.system('clear')

# Try to get input, return NONE if error
def parseInput(string):
    spArr = string.split(" ")
    # Input checking
    if (len(spArr) != 3):
        return
    cmd = spArr[0]
    if (cmd != "move" and cmd != "jump"):
        return
    try:
        coords1 = spArr[1][1:-1].split(",") # Turn string of coordinates into array
        coords2 = spArr[2][1:-1].split(",") # Turn string of coordinates into array
        tup1 = tuple([int(i) for i in coords1])
        tup2 = tuple([int(i) for i in coords2])
        return [cmd, tup1, tup2]
    except IndexError:
        return
    except ValueError:
        return

    return [cmd, (int(tup1[0]), int(tup1[1])), (int(tup2[0]), int(tup2[1]))]

if __name__ == "__main__": main()