def main():

    s1 = int(input("enter score #1: "))
    s2 = int(input("enter score #2: "))
    s3 = int(input("enter score #3: "))
    s4 = int(input("enter score #4: "))
    s5 = int(input("enter score #5: "))
    
    avg =  calc_average(s1,s2,s3,s4,s5)
    grade = determine_grade(avg)

    print("The average score is {} and the final grade {}".format(avg,grade))

def calc_average(s1,s2,s3,s4,s5):
    avg = (s1 + s2 + s3 + s4 + s5) / 5
    
    return avg

def determine_grade(g):
    
    if g >= 90:
        return "A"
    elif g >= 80:
        return "B"
    elif g >= 70:
        return "C"
    elif g >= 60:
        return "D"
    elif g < 60:
        return "F"

main()
 
            
