If the gcd of of capacity of two jugs is not a mulitple of target, then we cannot measure the target using 
the two jugs.

eg:
gcd(5,3)=1
target = 4 
four is divisible by one
so we can measure 4 litre using jugs of capacity 5 and 3 litres respectively

gcd(6,3)=3
target=4
four is not divisible by three
so we cannot measure 4 litre using 6 and 3 litre jug


if the target is greater than capacity of two jugs , then also we cannot measure.



repeat the below steps until target is reached(not optimal):
    -if jug1 is empty fill it
    -else if jug2 is full empty it
    -pour water from jug1 to jug2 until jug2 is full or jug1 is empyt(whichever happen first)

print the final answer

------------------------------------------------------------------------------------------------------------
ps: efficiency increased by assigning jug1 as the jug with greatest capacity, but time complexity remain same 

jug1, jug2 = (jug2, jug1) if jug2 > jug1 else (jug1, jug2)
