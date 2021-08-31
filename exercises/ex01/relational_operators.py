"""printing using concatenation and relational operatorators on your own"""

__author__ = "730240220"

Left_hand_side: str = input("Choose a number ")
Right_hand_side: str = input("Choose a second number ")

print( "Left-hand side: " + Left_hand_side)
print( "Right-hand side: " + Right_hand_side)

less_than = bool(Left_hand_side < Right_hand_side)
greater_or_equal = bool(Left_hand_side >= Right_hand_side)
equal = bool(Left_hand_side == Right_hand_side)
not_equal = bool(Left_hand_side != Right_hand_side)

print( Left_hand_side + " < " + Right_hand_side + " is " + str(less_than))
print( Left_hand_side + " >= " + Right_hand_side + " is " + str(greater_or_equal))
print( Left_hand_side + " == " + Right_hand_side + " is " + str(equal))
print( Left_hand_side + " != " + Right_hand_side + " is " + str(not_equal))


