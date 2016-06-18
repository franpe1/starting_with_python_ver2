### Global

PENNIES  =  1
NICKELS  =  5
DIMES    = 10
QUARTERS = 25

### START

def main():
    print("WELCOME TO THE DOLLAR GAME")
    p = int(input("Enter the number of pennies: "))
    n = int(input("Enter the number of nickels: "))
    d = int(input("Enter the number of dimes: "))
    q = int(input("Enter the number of quarters: "))
    dollargame(p,n,d,q)

def dollargame(p,n,d,q):
    
    dollar = (p * PENNIES) + (n * NICKELS) + \
             (d * DIMES) + (q * QUARTERS)

    if dollar == 100:
        print("Congratulations you put the exact quantity")
    elif dollar < 100:
        difDollar = 100 - dollar
        print("Nope, you are off by ", difDollar,"cts" , \
              " you need to add more coins",sep="")
    elif dollar > 100:
        difDollar = dollar - 100
        print("Nope, you are over by ", difDollar, "cts" , \
              " you need to take back more coins",sep="")

main()
