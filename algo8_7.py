import random

def main():

    col = 3
    row = 5
    twodlist = []

    for x in range (row):
        twodlist += [[0]*col]

    print(twodlist)

    for r in range(row):
        for c in range(col):
            number = random.randint(1,100)
            twodlist[r][c] = number

    print (twodlist)

    getint(twodlist)


def getint(list):

    row = len(list)
    col = len(list[0])
    
    for r in range(row):
        for c in range (col):
            print(list[r][c])
        
main()
