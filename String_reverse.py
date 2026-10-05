class Reverse:
    def __init__(self, s):
        self.s = s  

    def reverse_string(self):
        words = self.s.split(" ")
        new_list = []
        
        for word in words:
            reversed_word = word[::-1]
            new_list.append(reversed_word)
            
        result = ""
        for word in new_list:
            result = result + word + " "
            
        return result.strip()

obj1 = Reverse(input("Enter anything: "))
print(obj1.reverse_string())