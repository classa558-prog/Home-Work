class BMW:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type
    def display_attributes(self):
        print(f"My max speed is {self.max_speed}.\nMy fuel type is {self.fuel_type}.")
class Ferrari:
        def __init__(self, max_speed, fuel_type):
            self.max_speed = max_speed
            self.fuel_type = fuel_type
        def display_attributes(self):
            print(f"My max speed is {self.max_speed}.\nMy fuel type is {self.fuel_type}.")
obj = BMW(220, "Special")
obj1 = Ferrari(450, "Diesel")
for obj_loop in obj, obj1:
     obj_loop.display_attributes()
