import art
print(art.logo)

print('Welcome to the number guessing game!')
import random
answer = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
# print(f"The correct answer is {answer}")

difficulty = input("choose_a_difficulty. type 'easy' or 'hard':")

num_attempts = 10 if difficulty == "easy" else 5

print(f"You have {num_attempts} attempts remaining to guess the number")


while num_attempts > 0:
    guess = int(input("make_guess:"))
    if guess == answer:
        print (f"You got it! The answer was {answer}")
        break
    print("Too low." if guess < answer else "Too high.")
    num_attempts -= 1
    if num_attempts > 0:
        print(f"You have {num_attempts} attempts remaining to guess the number")

if num_attempts == 0:
    print(f"You lose. The answer was {answer}")
            
    
    