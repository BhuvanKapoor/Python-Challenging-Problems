# Python-Challenging-Problems

### IDENTIFYING FRIEND CIRCLE
A primary school has students with roll numbers 1 to 60 and also has seats with numbers 1 to 60 printed on them. Normally each student sits in the seat as per roll number. One day the students sit differently as the teacher told them so. It is possible some students did not change position. Or some set of students form friend circles and change the seats only among themselves. <br>
Your input is the list of numbers from 1 to 60 rearranged as per the new seating. The 4th number of the list should be interpreted as the roll number of students in seat number 4. (To make it convenient for Python, create seat number 0 and and assume teacher takes that seat always). <br>
Your job is identiying the friends circle in the new rearrangment. An example friend circle could be [1, 7, 2, 24, 8]. This means these students changed seats among themselves as below: <br>
1 → 7 → 2 → 24 → 8 → 1 <br>
A student refusing to move would make (theoretically) a friend circle of length 1. Two students making mutual exchange will be a friend circle of length 2. etc <br>
Your problem is, given an input list which is a rearrangment of 1 to 60 to print all the friend circles for that rearrangement.

### FINDING LARGEST SUBSEQUENCE
Given a sequence of 100 numbers find the largest subsequence which is increasing. For example, if the given sequence is 5,2,4,11,8,9,3,8,12,14,7,6,9 the increasing subsequences are
[5], [2, 4, 11], [8, 9], [3, 8, 12, 14], [7], [6, 9] <br>
The largest being the subsequence [3,8,12,14], of length 4.

### DISPLAYING CURRENT STATUS OF A CHESS GAME
This is a problem on printing the given data on screen in a particular format according to given rules. The data represents current status of a game of chess. <br>
The pieces are named : <br>
K (for King), <br>
Q (for Queen), <br>
B (for Bishop), <br>
N (for Horse/Knight), <br>
R (for Rook/Elephant), <br>
P (for Pawn/Soldier)<br>
The above names are used for Black pieces. For White pieces the same is used, but instead of capitals, it will be small letters: k,q,b,n,r,and p. <br>
Each square of the 8 × 8 chess board is given a serial number from 1 to 64, with top row getting numbers 1 to 8, second row is given number 9 to 16 etc. <br>
The game status is your input data: <br>
(i) Input is a comma separated string <br>
(ii) Format of input is like ”K4,Q5,n23”. <br>
(iii) This means Black King is present in square number 4, Black Queen is in square number 5, and White Knight in square number 23. <br>
(iv) Input string can be short or long depending on the number of pieces present in the board. <br>
(v) The data string is presented in the increasing order of serial numbers, obviously omitting numbers corresponding to empty squares. <br>
Your job is to print the current status of the “chess board” in 8 lines/rows of output in the following format:<br>
• each line should have exactly 16 characters. <br>
• the character should be name of the piece in that position followed by a space character. <br>
• for an empty square, an underscore ‘_’ should be printed. <br>
An example output:<br>
R N _ K Q B _ R <br>
P P P _ _ _ P _ <br>
_ _ B P p P _ n <br>
_ _ q p _ b _ _ <br>
(just top 4 of the 8 rows of the board is shown above) Your printing should take care that, e.g., 3rd square of all the rows should be vertically aligned as shown above).
