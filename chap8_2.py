import random

def main():

    for i in range(7):
        winers = lotery()
        print(winers[i])

def lotery():
    numbers = [0]*7
    for i in range(7):
        numbers[i] = random.randint(1,9)
    return numbers

main()

    
