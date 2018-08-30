class Board:
    """
    * 2d list with ints representing pieces/spaces
    * 0 is empty, 1 is white piece, 2 is red piece 
    * Players are thus identified as 1 and 2
    """
    def __init__(self):
        self.currPlayer = 2
        self.boardArray =[[0, 1, 0, 1, 0, 1, 0, 1],
                         [1, 0, 1, 0, 1, 0, 1, 0],
                         [0, 1, 0, 1, 0, 1, 0, 1],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [2, 0, 2, 0, 2, 0, 2, 0],
                         [0, 2, 0, 2, 0, 2, 0, 2],
                         [2, 0, 2, 0, 2, 0, 2, 0]]
        # Set of coordinates of current player pieces, indexed to playerNum
        self.playerPieces = [ "PLACEHOLDER",
                            {(0, 1), (0, 3), (0, 5), (0, 7),
                             (1, 0), (1, 2), (1, 4), (1, 6),
                             (2, 1), (2, 3), (2, 5), (2, 7)},
                            {(5, 0), (5, 2), (5, 4), (5, 6),
                             (6, 1), (6, 3), (6, 5), (6, 7),
                             (7, 0), (7, 2), (7, 4), (7, 6)}]
    
    """
    ===================== MOVE METHODS ==============================
    """
    
    """ 
    * Tries to move player from coordStart to coordFin
    * Player is an int, coords are tuples of ints
    """
    def move(self, player, coordStart, coordFin):
        if (self.currPlayer != player):
            print("Not your turn!")
            return
        if(self.canJump(self.currPlayer)):
            print("You must jump!")
            return

        if (self.isValidMove(player, coordStart, coordFin)):
            # Place the player
            self.boardArray[coordFin[0]][coordFin[1]] = player
            self.boardArray[coordStart[0]][coordStart[1]] = 0
            # Update their pieces
            self.playerPieces[player].remove(coordStart)
            self.playerPieces[player].add(coordFin)
            self.switchTurn()
        else:
            print("invalid move")

    """ Returns true if a move is valid, false otherwise """
    def isValidMove(self, player, coordStart, coordFin):
        if (player != 1 and player != 2):
            return False
        if ((coordFin[1] != coordStart[1] + 1) and (coordFin[1] != coordStart[1] - 1)):
            return False
        elif (self.boardArray[coordFin[0]][coordFin[1]] != 0):
            return False
        elif (self.boardArray[coordStart[0]][coordStart[1]] != player):
            return False
        else:
            return True
        
    """
    ==================== JUMP METHODS =================================
    """
    
    """ Tests whether player has ability to jump """
    def canJump(self, player):
        for p in self.playerPieces[player]:
            if (self.pieceCanJump(player, p)):
                return True
        return False
    
    """ Tests whether an individual piece has ability to jump """
    def pieceCanJump(self, player, coords):
        if (player == 1):
            # generate possible destination coordinates
            destLeft = (coords[0] + 2, coords[1] - 2)
            destRight = (coords[0] + 2, coords[1] + 2)
            return self.isValidJump(player, coords, destLeft) or self.isValidJump(player, coords, destRight)

        elif (player == 2):
            destLeft = (coords[0] - 2, coords[1] - 2)
            destRight = (coords[0] - 2, coords[1] + 2)
            return self.isValidJump(player, coords, destLeft) or self.isValidJump(player, coords, destRight)


    """ Tests to see if a jump is valid """
    def isValidJump(self, player, start, finish):
        # If jump is out of range, obviously not valid
        if ((finish[0] not in range(8)) or (finish[1] not in range(8))):
                return False
        if (self.boardArray[finish[0]][finish[1]] != 0):
            # Can't jump to opposite player
            return False
        if (player == 1):
            if (finish[0] != (start[0] + 2)):
                # Invalid distance
                return False
            elif ((finish[1] != (start[1] + 2)) and (finish[1] != (start[1] - 2))):
                # Invalid distance
                return False
            
            midSquare = self.getMidSquare(player, start, finish)

            # Check if it is occupied
            if (self.boardArray[midSquare[0]][midSquare[1]] == 0):
                return False
            elif ((self.boardArray[midSquare[0]][midSquare[1]] == player)):
                return False
            else:
                # We should be good, then
                return True
        elif (player == 2):
            if (finish[0] != (start[0] - 2)):
                # Invalid direction or distance
                return False
            if ((finish[1] != (start[1] + 2)) and (finish[1] != (start[1] - 2))):
                # Invalid direction or distance
                return False
            
            # Calculate square piece is jumping over
            midSquare = self.getMidSquare(player, start, finish)

            # Check if it is occupied
            if (self.boardArray[midSquare[0]][midSquare[1]] == 0):
                return False
            elif ((self.boardArray[midSquare[0]][midSquare[1]] == player)):
                return False
            else:
                # We should be good, then
                return True

    """ Calculates the coordinates of the square between a jump """
    def getMidSquare(self, player, start, finish):
        if (player == 1):
            if (finish[1] > start[1]):
                return (start[0] + 1, start[1] + 1)
            else:
                return (start[0] + 1, start[1] - 1)
        elif (player ==2):
            if (finish[1] > start[1]):
                return (start[0] - 1, start[1] + 1)
            else:
                return (start[0] - 1, start[1] - 1)

    """ 
    * Tries to jump player from coordStart to coordFin
    * Player is an int, coords are tuples of ints
    """
    def jump(self, player, coordStart, coordFin):
        if (player != self.currPlayer):
            print("Not your turn!")
            return -1
        elif (not self.isValidJump(player, coordStart, coordFin)):
            print("invalid jump")
            return -1
        else:
            # If all of that passes, we can place the current player
            self.boardArray[coordFin[0]][coordFin[1]] = player
            self.boardArray[coordStart[0]][coordStart[1]] = 0
            # And update their pieces
            self.playerPieces[player].remove(coordStart)
            self.playerPieces[player].add(coordFin)

            # Then we remove the other player's lost piece
            midSquare = self.getMidSquare(player, coordStart, coordFin)
            self.boardArray[midSquare[0]][midSquare[1]] = 0
            self.playerPieces[self.getOppositePlayer(player)].remove(midSquare)
            
            
            if (not self.pieceCanJump(player, coordFin)):
                self.switchTurn()
    
    
    """
    ===================== UTIL METHODS ============================
    """
    """ Prints the board in its current state """
    def printBoard(self):
        print("   0 1 2 3 4 5 6 7")
        print("   ---------------")
        for y in range(8):
            line = str(y) + " |"
            for x in range(8):
                line += (str(self.boardArray[y][x]) + " ")
            print(line)
        print("   ---------------")
        print()

    def getOppositePlayer(self, player):
        if (player == 1):
            return 2
        else:
            return 1
    
    def switchTurn(self):
        if self.currPlayer == 1:
            self.currPlayer = 2
        else:
            self.currPlayer = 1
    
    """ Returns int corresponding to winning player, or 0 if game still in session """
    def isGameOver(self):
        if len(self.playerPieces[1]) == 0:
            return 2
        if len(self.playerPieces[2]) == 0:
            return 1
        return 0