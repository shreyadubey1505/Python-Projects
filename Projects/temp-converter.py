print("Type 1 for celcius to fahrenheit")
print("Type 2 for fahrenheit to celcius")
choice = input("Enter your choice:")
if choice == "1":
   celcius = float(input("Enter the temperature in celcius:"))
   fahrenheit = (celcius * 9 / 5) + 32
   print("The temperature in fahrenheit is:", fahrenheit)
elif choice == "2":
   fahrenheit = float(input("Enter the temperature in fahrenheit:"))
   celcius = (fahrenheit - 32) * 5 / 9
   print("The temperature in celcius is:", celcius)
else:
   print("Invalid input")
