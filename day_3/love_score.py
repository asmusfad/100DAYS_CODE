print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

# Write your code below this line 
love_name1 = name1.lower().count('l') +  name1.lower().count('o') +  name1.lower().count('v') +name1.lower().count('e')
love_name2 = name2.lower().count('l') +  name2.lower().count('o') +  name2.lower().count('v') +name2.lower().count('e')

true_name1 = name1.lower().count('t') +  name1.lower().count('r') +  name1.lower().count('u') +name1.lower().count('e')
true_name2 = name2.lower().count('t') +  name2.lower().count('r') +  name2.lower().count('u') +name2.lower().count('e')

true = true_name1 + true_name2
love = love_name1 + love_name2
score_str = str(true) + str(love)
score = int(score_str)
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif  score >= 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")