*Magic Square*


Using Siamse method (only work for odd numbers) , time complexity O(n^2)

for general n*n magic square use itertools permutation with time complexity of O((n^2)!)

steps:
put one in the top row and n//2 column,

place the next number,2, above and right of that column
(since no row is above row 0 , wrap around to the n th row)

wrapping is perfromed using the modulo operator, same as Caesars Cipher

if the above right row is occupid, place the next number just below the current number

(you could use 2 new variables (total 4) and keep condition simple : (i+1)%n , j )  
or use just two variable i and j like i did in code . (i,j=(i+2)%n,(j-1)%n) 

