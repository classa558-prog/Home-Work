n = int(input("Enter the height")) # Height of the triangle

for i in range(1, n + 1):
    # Print decreasing spaces followed by increasing stars
    print(" " * (n - i) + "*" * i)