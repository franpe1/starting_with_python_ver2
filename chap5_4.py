def main():
    speed = float(input("What is the speed of the vehicle in mph? "))
    hours = int(input("How many hours has it traveled? "))

    print("Hour \t\t Distance")
    for x in range (40):
        print("_",end="")
        
    print()
    compute(speed,hours)

def compute(s,h):
    for i in range(h+1):
        
        if i > 0:
            distance = s * i
            print(i,"\t\t",distance)

main()
    
