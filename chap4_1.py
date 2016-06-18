def main():
    decimal = int(input("Enter your decimal between 1 and 10: "))
    translate(decimal)

def translate(dec):
    if dec > 1 and dec < 10:
        if dec == 1:
            print("1 in Roman is I")
        elif dec == 2:
                print("2 in Roman is II")
        elif dec == 3:
                print("3 in Roman is III")
        elif dec == 4:
                print("4 in Roman is IV")
        elif dec == 5:
                print("5 in Roman is V")
        elif dec == 6:
                print("6 in Roman is VI")
        elif dec == 7:
                print("7 in Roman is VII")
        elif dec == 8:
                print("8 in Roman is VIII")
        elif dec == 9:
                print("9 in Roman is IX")
        elif dec == 10:
                print("10 in Roman is X")
    else:
        print("Do you know how to read? ")

main()
