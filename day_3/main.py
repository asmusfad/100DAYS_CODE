#Welcome to the rollecoaster ride
hieght = int(input("What is your hieght in cm? "))
bill = 0
if hieght >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
  elif age <= 18:
    bill = 7
  else:
    bill = 12
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")