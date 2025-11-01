print(" Welcome to the Rollercoaster Ride Ticket System ")

height = int(input("Enter your height (in cm): "))

if height >= 120:
    age = int(input("Enter your age: "))
    bill = 0

    if 18 <= age <= 50:
        bill = 100
        print("You can ride the rollercoaster.")
        print("Your fair price will be Rs:100.")

    elif age >= 60:
        print("You can ride but only with a young partner.")
        bill = 50
        print("Your fair price will be ₹50.")

    else:
        print("Sorry, you cannot ride alone.")
        bill = 0

    if bill > 0:
        want_photo = input("If you want a photo press 'Y' for Yes: ")
        if want_photo == "Y":
            bill += 5

        print(f"Your total bill is ₹{bill}")

else:
    print("Sorry, you are too short to ride.")
