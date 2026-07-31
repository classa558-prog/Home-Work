
num = int(input("Enter your number: "))
original_num = num
# Taking input.
binary_num = ""
# Making new string to represent binary number.
while num > 0:
    remainder = num % 2 # Getting remainder of the number via modulo.
    binary_num = str(remainder) + binary_num
    # Adding it on to the binary number
    num //= 2 # flooring the number 
print(f"Your number, {original_num} converted into binary is: {binary_num}")
