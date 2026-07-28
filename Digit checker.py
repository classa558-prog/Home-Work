# Taking input
user_input = int(input("Enter a number: "))
x = user_input
# Temporary variable to use in the while loop so the print statement works.

# Counter is used to check how many digits there are.

counter = 0
# Keep flooring by ten to make the number 1 digit smaller
while x > 0:
    x//= 10
    counter += 1
    # Increasing by 1 untill the number has no more digits.
# Printing output
print(user_input, "has", counter, "digits.")


