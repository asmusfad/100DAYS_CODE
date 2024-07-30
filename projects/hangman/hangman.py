from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

lives = 6
end_of_game = False

#Create an empty List called display.
display = []
for letter in chosen_word:
  display.append("_")



# start the game

while not end_of_game:
  guessed_letter = input("Guess a letter: ").lower()
  #clear()

  if guessed_letter in display:
    print(f"You've already guessed {guessed_letter}")
    cont = input("Do you want to continue? (y/n) ")
    if cont == "n":
      end_of_game = True
    else:
      continue

  for i in range(word_length):
    if chosen_word[i] == guessed_letter:
      display[i] = guessed_letter


  #print(f"You have {lives} lives left.")

  if guessed_letter not in display:
    print(f"You guessed {guessed_letter} that is not in the word, you lose a life")
    lives -= 1
    if lives == 0:
       end_of_game = True
       print("You lose!")
  print(f"{' '.join(display)}")


  if "_" not in display:
    end_of_game = True
    print("You win!")




  print(stages[lives])