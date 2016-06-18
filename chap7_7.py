import random

def main():
    number = int(input("how many random #s: "))

    file = open("random.txt","w")
    
    i = 0

    for i in range(number):
        ran = random.randint(1,100)
        f_ran = str(ran) + "\n"
        file.write(f_ran)
        
    file.close()

main()
