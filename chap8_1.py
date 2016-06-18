def main():
    days = [0,0,0,0,0]
    total = 0
    
    for i in range(5):
        days[i] = int(input("enter total sales for day {} ".format(i)))
        total += days[i]

    print(days)
    print("total: ",total)

main()
