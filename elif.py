print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))

if height>= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay 5 dollars")
    elif age <= 18:
        print("Please pay 7 dollars")
    else:
        print("Please pay 12 dollars")
else:
    print("Sorry,you have to grow taller before you can ride.")