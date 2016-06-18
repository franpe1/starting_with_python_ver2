import math


def main():
    radians = radian()
    print(radians)

def radian():
    d = int(input("enter # or degress: "))

    r = math.radians(d)

    return r

main()
    
