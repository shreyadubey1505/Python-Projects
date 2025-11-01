bill = float(input("Enter your total bill:"))
if bill > 5000:
   print("You get a 20% discount")
   discount = bill * 0.2
   print("Your discount is", discount)
   print("Your final bill is", bill - discount)
elif 2000 <= bill <= 4999:
   print("You get a 10% discount")
   discount = bill * 0.1
   print("Your discount is", discount)
   print("Your final bill is", bill - discount)
else:
   print("no discount")
   print("Your final bill is", bill)
