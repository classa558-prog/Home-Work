low_bound = int(input("Enter the lowest number in your range of squared numbers: "))
high_bound = int(input("Enter the highest number in your range of squared numbers: "))
squares=[]
for i in range(low_bound, high_bound+1):
    if (i**0.5) % 1 == 0:
        squares.append(i)
even_squares = []
odd_squares = []
for i in squares:
    if i % 2 == 0:
        even_squares.append(i)
    else:
        odd_squares.append(i)
print(f"All squares: {squares}")
print("Even Squares:",even_squares)
print("Odd Squares:",odd_squares)
