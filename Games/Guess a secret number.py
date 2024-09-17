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
            
        
