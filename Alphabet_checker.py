user_input = input("Enter something: ")

if user_input.isalpha():
    print("Yes! The input contains only alphabet letters.")
else:
    print("No! It contains spaces, numbers, or special characters.")
