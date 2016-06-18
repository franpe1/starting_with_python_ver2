import random

def main():
    for count in range(100):
        number = random.randint(1,1000)
        result = evenodd(number)
        print("The number {} is {}".format(number,result))

def evenodd(n):
    cal = n % 2
    if cal >= 1:
        result = "Odd"
        return result
    else:
        result = "Even"
        return result

main()
