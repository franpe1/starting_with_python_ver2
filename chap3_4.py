def main():
    loan = float(input("Enter loan amount: "))
    insu = float(input("Enter insurance amount: "))
    gas  = float(input("Enter gas amount: "))
    oil  = float(input("Enter oil amount: "))
    tire = float(input("Enter tire amount: "))
    mant = float(input("Enter maintenance ammount: "))

    monthly(loan, insu, gas, oil, tire, mant)
    yearly(loan, insu, gas, oil, tire, mant)

def monthly(l,i,g,o,t,m):
    totalMonth = l + i + g +o + t + m
    print("Your total expenses per month is: ",totalMonth)

def yearly(l,i,g,o,t,m):
    totalYear = (l + i + g + o + t + m) * 12
    print("your total exp per year is :",totalYear)

main()
