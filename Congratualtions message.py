name = "Agrim"
Split_text = "Hi'I am'happy!"
print(name.upper())
print(name.lower())
length = len(name)
print(name[0:length])
print(str(Split_text.split("'")[1]))
print(Split_text[::-1])

print(name + ", " + Split_text.replace("'", " "))