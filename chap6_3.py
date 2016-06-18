def main():
    a = int(input("enter value for a: "))
    b = int(input("enter value for b: "))

    correct = False

    while correct == False:
        if a == b:
            print("values can't be the same")
            a = int(input("enter value for a: "))
            b = int(input("enter value for b: "))
        else:
            correct = True
        
    max = maximum(a,b)

    print("out of {} and {}, {} is a bigger number".format(a,b,max))
            

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

main()
    
