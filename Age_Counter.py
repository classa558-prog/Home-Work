try:
    age = int(input("Enter your age: "))
    if age < 0 or age < 18:
        raise ArithmeticError
    if age % 2 == 0:
            print("Even number and you are permitted for a license.")
    else:
        print("Odd number and you are permitted for a license.")

    
except ValueError:
    print("You have not entered an integer! ")
except ArithmeticError:
    print("Invalid age, cannot be lower than 0 or 18!")


    



