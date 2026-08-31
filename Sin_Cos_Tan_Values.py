import math
import sys
try:
    num = float(input("Enter your number: "))
except:
    print("You have not entered a number.")
    sys.exit()


Operation_choice = input("Enter your operation (S for sin T for tan and C for cosine)").lower()
if Operation_choice == "t":
    print("Your number plugged into the tan() function results in: ", math.tan(num))
elif Operation_choice == "s":
    print("Your number plugged into the sin() function results in: ", math.sin(num))
elif Operation_choice == "c":
    print("Your number plugged into the cos() function results in: ", math.cos(num))
else:
    print("Invalid operation choice.")
 