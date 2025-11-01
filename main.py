age = int(input("Enter your age:"))
ID = input("Do you have a student ID? (yes/no):")

price = 0  # Initialize price

if age < 12:
  price = 50
elif 12 <= age <= 18:
  price = 80
elif 19 <= age <= 60:
  price = 120
else:  # age > 60
  price = 60
  
if ID == "yes":
   print("You got 10% OFF!")
   price = price - (price * 10 / 100)  # Fixed: subtract 10% instead of making price only 10%
   print("Your ticket price is:", price)
elif ID == "no":  
   print("Your ticket price is:", price)


