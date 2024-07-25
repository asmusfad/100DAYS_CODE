# Running total 
target = int(input()) # Enter a number between 0 and 1000

# Write your code here 
total = 0
for number in range(1, target+1): # alternativly range(2, target+1, 2)    
  if number % 2 == 0:
    total += number

print(total)

# Write fizzbuzz game
'''
Your program should print each number from 1 to 100 in turn and include number 100.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
  elif number % 3 == 0:
    print('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(number)
