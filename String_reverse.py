class Reverse:
    def __init__(self, s):
        self.s = s  
    def reverse_string(self):
        return self.s[::-1]

obj1 = Reverse(input("Enter anything: "))
print(obj1.reverse_string())