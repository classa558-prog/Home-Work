class Roman:
    def __init__(self, integer=0):
        self.integer = integer
    def obtain(self):
        self.integer = int(input("Enter an integer: "))
    def int_to_roman(self):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        i = 0
        while self.integer > 0:
            while self.integer >= values[i]:
                roman += symbols[i]
                self.integer -= values[i]
            i += 1
        return roman
obj = Roman()
obj.obtain()
print(obj.int_to_roman())


