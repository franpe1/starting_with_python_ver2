import random

def main():

    cont = "Y"
    playerWin = 0
    compWin = 0
    even = 0
#while cont == "Y" or cont == "y"
    while True:
        try:
            print("Let's Play Rock, Paper or Scissors!")
            option = str(input("Enter your weapon of choice: "))
            whoin = play(option)

            if whoin == "player":
                playerWin += 1
            elif whoin == "comp":
                compWin += 1
            elif whoin == "even":
                even += 1

        except KeyboardInterrupt:
            print("\n {} Even, {} Player Wins, {} Computer Wins" \
                  .format(even,playerWin,compWin))

def play(option):
 
    computer = random.randint(1,3)

    if option == "rock":
        if computer == 1:
            print("rocks, we are even")
            return "even"
        elif computer == 2:
            print("paper, computer wins")
            return "comp"
        elif computer == 3:
            print("scissors, you win")
            return "player"
    if option == "paper":
        if computer == 1:
            print("rocks, you win")
            return "player"
        elif computer == 2:
            print("paper, we are even")
            return "even"
        elif computer == 3:
            print("scissors, computer wins")
            return "comp"
    if option == "scissors":
        if computer == 1:
            print("rocks, computer wins")
            return "comp"
        elif computer == 2:
            print("paper, you win")
            return "player"
        elif computer == 3:
            print("scissors, we are even")
            return "even"
main()
        
    
    
