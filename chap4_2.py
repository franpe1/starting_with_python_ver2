def main():
    lenR1 = float(input("Enter lenght R1: "))
    widR1 = float(input("Enter lenght R1: "))
    lenR2 = float(input("Enter lenght R2: "))
    widR2 = float(input("Enter lenght R2: "))
    compute(lenR1,widR1,lenR2,widR2)

def compute(lr1,wr1,lr2,wr2):
    areaR1 = lr1 * wr1
    areaR2 = lr2 * wr2

    if areaR1 > areaR2:
        print("The area of R1 is bigger than R2 ", areaR1, "vs",areaR2)
    else:
        print("The area of R2 is bigger than R1 ", areaR2, "vs", areaR1)

main()
