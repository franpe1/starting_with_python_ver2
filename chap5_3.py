def main():
    expense = 1.0    # set to 1.0 to force the while to kick in
    total   = 0.0
    dif     = 0.0
    
    budget = float(input("enter budget: "))

    while expense > 0:
        expense = float(input("enter expense: ")) # here we need to re-enter expense
        total = total + expense

    print("your total expenses: ",total)

    if total > budget:
        dif = total - budget
        print("you are over by ",dif)
    else:
        dif = budget - total
        print("you saved ",dif)

main()
        
