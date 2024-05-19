*N-Queens problem*



Create a list of all possible permutation of queen placements
the index of list gives the row of queen and value of list gives column
the above condition make sure no two queen share same column or row
check if any two queen is on same main diagonal (/) or anti diagonal (\)
        condition for main diagonal : r1−c1=r2−c2
        condition for anti diagonal : r1+c1=r2+c2
    since we will take the same two queens in loop , thew will always overlap
    therefore if value of diagonal condition is 1 , no two distinct queens overlap
    

    check this conditioni for all rows and if no two distinct queen overlap in any condition then add that position 
    value to final list

    print the final output :
        print Q if index matches the value of list else print . 

p.s feel free to contact if any error or doubt