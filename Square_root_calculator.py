Number = int(input("Input a Integer:"))
Root_power = int(input("which power root would you like; (e.g. 2 for square root or 3 for cube root):"))
Result = Number**(1/Root_power)
print("The ", Root_power, "of ", Number, "is ", round(Result))