#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_l = random.sample(letters, nr_letters)
password_n = random.sample(numbers, nr_numbers)
password_s = random.sample(symbols, nr_symbols)
password = password_l + password_n + password_s

#Alternatively one kan use for loops to build passwordparts
'''for _ in range(1, nr_letters+1):
  password_l += (random.choice(letters))
for _ in range(1, nr_numbers+1):
  password_n += (random.choice(numbers))
for _ in range(1, nr_symbols+1):
  password_s += (random.choice(symbols))
password = password_l + password_n + password_s
'''



random.shuffle(password)
print(''.join(password))
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P