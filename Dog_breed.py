class Dog:
    animal = "Canine"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black & Tan")

print("--- Dog 1 Details ---")
print(f"Animal: {dog1.animal}")
print(f"Breed: {dog1.breed}")
print(f"Colour: {dog1.colour}\n")

print("--- Dog 2 Details ---")
print(f"Animal: {dog2.animal}")
print(f"Breed: {dog2.breed}")
print(f"Colour: {dog2.colour}")