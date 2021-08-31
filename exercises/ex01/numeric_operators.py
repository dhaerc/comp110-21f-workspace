"""printing using concatenation and numeric operators"""

__author__ = "730240220"

Left_hand_side: str = input("Choose a number ")
Right_hand_side: str = input("Choose a second number ")

print( "Left-hand side: " + Left_hand_side)
print( "Right-hand side: " + Right_hand_side)

exponentiation = int(Left_hand_side) **  int(Right_hand_side)
division = int(Left_hand_side) /  int(Right_hand_side)
integer_division = int(Left_hand_side) //  int(Right_hand_side)
remainder = int(Left_hand_side) %  int(Right_hand_side)

print(Left_hand_side + " ** " + Right_hand_side + " is " + str(exponentiation)) 
print(Left_hand_side + " / " + Right_hand_side + " is " + str(division)) 
print(Left_hand_side + " // " + Right_hand_side + " is " + str(integer_division)) 
print(Left_hand_side + " % " + Right_hand_side + " is " + str(remainder)) 