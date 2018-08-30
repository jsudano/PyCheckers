# PyCheckers
A simple implementation of checkers I did as a coding challenge. Occasionally I change it a bit when I'm bored.

## Dependencies
Should currently run on any system with python3, but I haven't tested on Windows for a while

## Instructions
- run checkers.py to start
- The shell prints a board. 
- Player 1's pieces are the numbers 1, player 2's pieces are the numbers 2
    - Currently missing kings
- Empty spaces are 0
- To move, type `move (Y1,X1) (Y2,X2)` where `(Y1, X1)` are the coordinates of your piece, and `(Y2, X2)` are the coordinates of its destination
- To jump, type `jump (Y1,X1) (Y2,X2)`

## Planned features
- Add kings
    - I actually have to figure out how checkers works before I do that
- Improve the way the actual game loop works
    - Just make it a little less ugly
- Streamline input
- Add an actual UI?