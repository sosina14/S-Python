#Guessing Game
secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
  guess_count += 1
  guess = int(input("Guess a number between 1 and 10: "))

print(f"You guessed it in {guess_count} tries!")
