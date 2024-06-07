import random
import hangman_art
import hangman_words

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
chosen_word = random.choice(hangman_words.word_list)
print (hangman_art.logo)
hidden_word = []
for l in chosen_word:
    hidden_word.append("_")
num_lives = 6
print(" ".join(hidden_word))
guesses = []
while("_" in hidden_word and num_lives > 0):
   cls()
   print(" ".join(hidden_word))
   print(hangman_art.stages[num_lives])

   guess = input("guess a letter: ").lower()
   
   if guess in guesses:
      print(f"You've already guessed {guess}")
      print(" ".join(hidden_word))
   else:
      i = 0
      found_letter = False
      for l in chosen_word:
         if guess == l:
            hidden_word[i] = l
            found_letter = True 
         i += 1
      if guess not in chosen_word:
         num_lives -= 1
         print("num_lives", num_lives)

      guesses.append(guess)
   

   
if num_lives > 0:
   print("You win!")
else: 
   print("You lose!")   



