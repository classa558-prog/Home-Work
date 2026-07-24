user = int(input("Enter your age: "))

if user >= 10 and user <= 20:
    print("You are", user, "years old and are eligible congrats bro.")
else:
    if user < 10:
        print("Not eligible", user, "is too low kiddy")
    else:
        print("Not eligible", user, "is too high gramps")