import sys

def shut_down():
    boolean = input("Wanna leave the program, y for yes n for no.")
    if boolean == "y":
        print("Bye")
        sys.exit()
    elif boolean == "n":
        print("Ok")
    else:
        print("Invalid choice.")
shut_down()
