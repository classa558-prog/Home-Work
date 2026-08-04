n = int(input("Enter the height: ")) # Height of the triangle

for i in range(n+1):
    counter = n-i
    for k in range(counter, 0, -1):
        print(" ", end = "")
        counter -= 1
    for j in range(i):
        print("*", end = " ")
    print()


    

