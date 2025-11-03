print("The Treasure Island")
print("Your mission is to find the treasure.")
print(
    "You are in a dark, narrow cave with only two doors.Do you want to go through door 1 or door 2?"
)
stage1 = input("Choose door 1 or door 2:")
if stage1 == "1":
  print("Congratulations you choose the correct door.")
  print("Now there is a river.")
  print("Do you want to swim across the river or use the boat to cross it?")
  stage2 = input("Choose swim(S) or boat(B):")
  if stage2 == "B":
    print("Congratulations you cross the river.")
    print(
        "There are three doors in front of you. Red door, Blue door and Yellow door."
    )
    stage3 = input("Choose a door (R/B/Y):")
    if stage3 == "B":
      print("Congratulations you found the treasure.")
      print("YOU WON")
    else:
      print("Sorry, you choose the wrong colour.")
      print("GAME OVER")
  else:
    print("The river had crocodile.")
    print("GAME OVER")
    print("People luckily put their hands on treasure.")

else:
  print("Sorry, you choose the wrong door.")
  print("GAME OVER")
  print("People luckily put their hands on treasure.")
