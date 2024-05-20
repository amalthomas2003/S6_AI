*Connect 4 Game*

using random 

The list  is used to store row and column of the matrix
the index of the list is the column  and the value represent the current row of matrix

initially the current row is 6 and is decremented as game progresses


after each new move the position is evaluated based on that move only to check if it is a winning move
for the player or computer. 
by passing "P" or "C" as argument in check , we can avoid the need to check the entire board after each move. just consider the last of player and see if it grands the win or not

condition check : 
horizontal :
- see if 4  squares to right(j+k) or left(j-k)  as same as player symbol , ie only j will change

vertical
- see if 4  squares to top(i-k) or bottom(i+k)  as same as player symbol , ie only i will change

diagonal 
- to check diagonal we have 4 conditions : 
    --matrix[i+k][j+k] == s for k in range(4) -> left top to right bottom
    --matrix[i-k][j-k] == s for k in range(4) -> right bottom to left top
    --matrix[i-k][j+k] == s for k in range(4) -> left bottom to right top
    --matrix[i+k][j-k] == s for k in range(4) -> right top to left bottom



The game ends if player plays an illegal move or no more squares are available.

The same logic can be used to implement tic-tac-toe