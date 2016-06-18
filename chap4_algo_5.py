def main():
    amount1 = float(input("value 1: "))
    amount2 = float(input("value 2: "))
    compare(amount1,amount2)

def compare(amount1,amount2):
    if amount1 > 10 and amount2 < 100:
        if amount1 > amount2:
            print(amount1," is bigger than ",amount2)
        else:
            print(amount2," is bigger than ",amount1)
    else:
        print("go to fry eggs ")
main()
