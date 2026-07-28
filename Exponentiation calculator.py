base = int(input("Base: "))
exponent = int(input("Exponent: "))

result = 1

for i in range(exponent):
    result *= base

print("Result:", result)
