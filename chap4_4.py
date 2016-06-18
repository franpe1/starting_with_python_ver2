def main():
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))
    magic(month,day,year)

def magic(m,d,y):
    magiCal = m * d

    if magiCal == y:
        print("You're lucky dude this is a magic date ",m,"/",d,"/",y,sep="")
    else:
        print("Oh well.... not magic date for you")

main()
