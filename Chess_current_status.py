# %%
'''
This is a problem on printing the given data on screen in a particular format according to given rules. The data represents current status of a game of chess.
The pieces are named : 
K (for King),
Q (for Queen)
B (for Bishop)
N (for Horse/Knight)
R (for Rook/Elephant)
P (for Pawn/Soldier)
The above names are used for Black pieces.
For White pieces the same is used, but instead of capitals, it will be
small letters: k,q,b,n,r,and p.
Each square of the 8 × 8 chess board is given a serial number from 1 to 64, with top row getting numbers 1 to 8, second row is given number 9 to 16 etc.
The game status is your input data:
(i) Input is a comma separated string
(ii) Format of input is like ”K4,Q5,n23”.
(iii) This means Black King is present in square number 4, Black Queen is in square number 5, and White Knight in square number 23.
(iv) Input string can be short or long depending on the number of pieces present in the board.
(v) The data string is presented in the increasing order of serial numbers,
obviously omitting numbers corresponding to empty squares.
Your job is to print the current status of the “chess board” in 8 lines/rows of output in the following format:
• each line should have exactly 16 characters.
• the character should be name of the piece in that position followed by a space character.
• for an empty square, an underscore ‘ ’ should be printed.
An example output:
R N _ K Q B _ R
P P P _ _ _ P _
_ _ B P p P _ n
_ _ q p _ b _ _
(just top 4 of the 8 rows of the board is shown above) Your printing should take care that, e.g., 3rd square of all the rows should be vertically aligned as shown above).
'''

data = "R1,N2,K4,Q5,B6,R8,P9,P10,P11,P15,B19,P20,p21,P22,N24,q27,p28,b30,q60,k61"
chess_pieces = data.split(",")

chess = []
for sq in chess_pieces:
    chess.append([sq[0],int(sq[1:])])

empty_sq = []
for sq in range(len(chess)-1):
    if chess[sq][1]+1 != chess[sq+1][1]:
        for empty_squares in range(1,(chess[sq+1][1] - chess[sq][1])): 
            empty_sq.append(chess[sq][1]+empty_squares)
for empty_squares in range(chess[-1][1]+1,65):
    empty_sq.append(empty_squares)

for empty_sq_number in empty_sq:
    chess.insert(empty_sq_number-1,["_",empty_sq_number])

for square in range(1,len(chess)+1):
    if square%8 == 0:
        print(chess[square-1][0])
    else:
        print(chess[square-1][0], end=" ")