import random

def main():

    play = "Y"

    while play == "Y" or play == "y":
        print("This is the guess number game, Let's Play!")
        number = int(input("Guess a number from 1 - 100: "))
        logic(number)
        play = input("Do you want to continue playing? ")
        


def logic(number):
    gamenumber = random.randint(1,100)

    attempts = 0
    guessed = False

    while guessed == False:

        attempts = attempts + 1
        
        if number == gamenumber:
            print("You guessed right! in {} attempts" \
                         .format(attempts))
            guessed = True
        elif number > gamenumber:
            print("Number too high try again")
            number = int(input("Guess a number from 1 - 100: "))
        elif number < gamenumber:
            print("Number is too low try again")
            number = int(input("Guess a number from 1 - 100: "))

main()
           
        
    
