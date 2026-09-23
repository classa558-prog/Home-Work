class Circle:
    def __init__(self, radius=0.0):
        self.radius = radius
        self.area = 0.0
        self.perimeter = 0.0
    def obtain_values(self):
        self.radius = float(input("Enter the radius of your circle as a float number: "))

    def find_area(self):
        self.area = (self.radius ** 2)*3.1415926
    def find_perimeter(self):
        self.perimeter = (self.radius * 2)*3.1415926
Circle1 = Circle()
Circle1.obtain_values()
Circle1.find_area()
Circle1.find_perimeter()

print(f"Area: {Circle1.area}")
print(f"Perimeter: {Circle1.perimeter}")

