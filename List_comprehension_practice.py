num = int(input("Enter a number: "))
odd_numbers = [x for x in range(num+1) if x % 2 != 0]
print(odd_numbers)
fruits = ["apple",  "strawberry", "pineapple", "peach"]
updated_fruits = [x.capitalize() for x in fruits]
print(updated_fruits)