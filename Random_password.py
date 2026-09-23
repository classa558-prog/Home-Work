import random
def create_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*():<>?/]["
    characters_list = list(characters)
    length = 12
    Password = ""
    for i in range(length):
        Password += random.choice(characters_list)
    return Password
Password = create_password() 
print(Password)

