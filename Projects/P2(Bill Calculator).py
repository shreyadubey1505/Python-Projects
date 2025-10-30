print("Welcome to the Tip Calculator and Bill Splitter")

total_bill = float(input("What is the total bill: ₹"))
tip_percent = float(input("What percentage tip would you like to give: "))
num_people = int(input("How many people to split the bill: "))

tip_amount = (tip_percent / 100) * total_bill
total_with_tip = total_bill + tip_amount

amount_per_person = total_with_tip / num_people

print("Each person should pay: ₹", round(amount_per_person, 2))
