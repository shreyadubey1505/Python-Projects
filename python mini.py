name = input("Enter text:" )
if name.isalpha():
    print("This is an alphabetic string")
else:
    print("Invalid text! only letters are allowed")
name = input("Enter text:" )
if name.isnumeric():
    print("This is an numeric string")
else:
    print("Invalid text! only numbers are allowed")
name  = input("Enter text:")
if name.isalnum():
    print("This is an alphanumeric string")
else:
    print("Invalid text! only letters and numbers are allowed")
name  = input("Enter text:")
if name.isascii():
   print("This is a mixed string with special characters")
else:
   print("not mixed string")