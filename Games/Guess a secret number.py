secret_number = int(input ("I'm thinking of a number between 1 and 10. Can you guess it?  "))
match secret_number :
    case 5 | 6 |8|9:
        print ("Nope, your guess is a bit low. Give it another shot!")
    case  1 | 2 | 3 | 4 :
        print ("Oops, your guess is a bit high. Try again!")
    case 7:
        print (" Congratulations, you guessed it!")
        value = input (" Play again? (yes/no)  ")
        if value == "no":
            print ("OK GOOD BYE")
            
        


import random

secret_number = random.randint(1, 10)
guess_count = 0

while True:
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))
    guess_count += 1

    if guess == secret_number:
        print(f"Congratulations, you guessed it in {guess_count} tries!")
        break
    elif guess > secret_number:
        print("Oops, your guess is a bit high. Try again!")
    else:
        print("Nope, your guess is a bit low. Give it another shot!")

while True:
    play_again = input("Play again? (yes/no): ").strip().lower()
    
    if play_again == "yes":
        secret_number = random.randint(1, 10)
        guess_count = 0
        while True:
            guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))
            guess_count += 1

            if guess == secret_number:
                print(f"Congratulations, you guessed it in {guess_count} tries!")
                break
            elif guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            else:
                print("Nope, your guess is a bit low. Give it another shot!")
    else:
        print("Thanks for playing! Goodbye!")
        break
