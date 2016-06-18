from  random import randint
import math

def main():
    number1 = randint(100,200)
    number2 = randint(100,200)

    print("  {} \n +{} \n _____".format(number1,number2)) 
    
    result = int(input("  "))

    answer = check(number1,number2)

    if answer == result:
        print("you konw your stuff 100 pts for you")
    else:
        print("wtf!!")

def check(number1,number2):
    total = number1 + number2
    return total

main()
