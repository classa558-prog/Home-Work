class Vehicle:
    def __init__(self, speed, miles_driven):
        self.speed = speed
        self.miles_driven = miles_driven
    def find_total_cost(self):
        cost = self.speed*self.miles_driven
        print(cost)
class Bus(Vehicle):
    def __init__(self):
        super().__init__(self)
    super().find_total_cost()
bus1 = Bus(50, 45)
