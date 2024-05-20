
def check_win(matrix,i,j,s):
    try:
        if all(matrix[i-k][j] == s for k in range(4)) or all(matrix[i+k][j] == s for k in range(4)):
            return True
        elif all(matrix[i][j-k] == s for k in range(4)) or all(matrix[i][j+k] == s for k in range(4)):
            return True
        elif all(matrix[i-k][j+k] == s for k in range(4)) or all(matrix[i+k][j-k] == s for k in range(4)):
            return True
        elif all(matrix[i+k][j+k] == s for k in range(4)) or all(matrix[i-k][j-k] == s for k in range(4)):
            return True
    except:
        return False
    else:
        return False
def display_board(matrix):
    for i in matrix:
        print(" ".join(i))
from random import randint
list1=[6]*7
matrix=[[" . "]*7 for _ in range(6)]
while True:
    try:
        pos=int(input("Enter the column : "))  
        list1[pos]-=1
        matrix[list1[pos]][pos]=" P "
        print(" ",'   '.join(f"{i}" for i in range(7)),sep="") #This is to display the top 0 1 2 3... numbering
        display_board(matrix)
        if check_win(matrix,list1[pos],pos," P "):
            print("You win ")
            break
        print("Computer move : ")
        while True:
            num=randint(0,6)
            if list1[num]-1>=0:
                break
        list1[num]-=1
        matrix[list1[num]][num]=" C "
        print(" ",'   '.join(f"{i}" for i in range(7)),sep="") #This is to display the top 0 1 2 3... numbering
        display_board(matrix)
        if check_win(matrix,list1[num],num," C "):
            print("You Lose ")
            break
    except:
        print("Index out of bound/illegal move ")
        break
