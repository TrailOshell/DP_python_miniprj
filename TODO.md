# MANDATORY
- [x] Write a function
    - [x] that takes rows of a chessboard as arguments
    - [x] and checks if your King is "in check".
- [x] play with...
    - [x] Pawns
    - [x] Bishops
    - [x] Rooks
    - [x] Queens
    - [x] King.
- [x] A piece can only capture the first possible piece that stands on its path.
- [x] The board can be of different sizes but will remain a square.
- [x] There’s only one King
- [x] All the characters that are not used to refer to pieces are considered as empty squares.
- [x] The King is considered to be "in check" when an other enemy piece can capture it.  
    - [x] When it’s the case, you will print "Success" on the standard output followed by a newline
    - [x] otherwise you will print "Fail" followed by a newline.
- [x] Your function should never crash or loop indefinitely.
- [x] Whenever an undefiend behavior occurs you should return an error message or prints nothing and gives back control.

# BONUS
- [x] read .chess file
- [ ] "Create a program that takes the best move for a checkmate."
    - [ ] recursive is probably the way. let it loop and find shortest possible steps(or turns?) for checkmate
- [ ] a chess game
    - [ ] king checker: player use other pieces to checkmate the king
    - [ ] king mode: player survive as the lone king
    - [ ] actual chess game: make a traditional chess game

# EXTRA
- [x] use '-' '|' '\' '/' to draw checkmate line
- [x] add color
- [x] grid name
    ... .. .......10
    ... .. .......9
    .            
    .            
    ... .. .......2
    ... .. .......1
    abc .. zaaaaa?
            abcde

- [ ] trim the output of checkmate result if it's too big