

def main():
    weight = float(input("Enter the weight of the pack: "))
    compute(weight)

def compute(w):
    if w <= 2:
        RpP = 1.10
        charges = w * RpP
        printRate(charges)
    elif w >= 3 or w <= 6:
        RpP = 2.20
        charges = w * RpP
        printRate(charges)
    elif w >= 7 or w <= 10:
        RpP = 3.70
        charges = w * RpP
        printRate(charges)
    elif w > 10:
        RpP = 3.80
        charges = w * RpP
        printRate(charges)


def printRate(char):
    print("Your charge is ",format(char,",.2f"))

main()
    
    
