def main():
    feet = float(input("enter # of feet: "))

    inches = feet_to_inches(feet)
    
    print("{} feet are equal to {} inches".format(feet,inches))

def feet_to_inches(f):
    inches = f * 12
    return inches

main()
