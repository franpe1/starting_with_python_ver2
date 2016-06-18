RETAIL = 99
TOTAL = 0
DISC = 0

def main():
    packages = int(input("Enter the number of packages: "))
    discount(packages)
    print("Your discount was ",DISC,"Your total is ",format(TOTAL,",.2f"))
    
def discount(pack):
    global TOTAL
    global DISC
    print(pack)
    
    if 10 >= pack or pack <= 19:
        discPrice = RETAIL * 0.20
        TOTAL = pack * discPrice
        DISC = 20
        
    elif 20 >= pack or pack <= 49:
        discPrice = RETAIL * 0.30
        TOTAL = pack * discPrice
        DISC = 30

    elif 50 >= pack or pack <= 99:
        discPrice = RETAIL * 0.40
        TOTAL = pack * discPrice
        DISC = 40

    elif 100 >= pack:
        discPrice = RETAIL *.50
        TOTAL = pack * discPrice
        DISC = 50

main()
                
            
