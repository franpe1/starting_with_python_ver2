def main():

    acct = loadfile()

    number = int(input("enter the 8 digit account #: "))

    if number in acct:
        print("account found!")
    else:
        print("account not found!")
                 

def loadfile():

    acct = []
    
    file = open('data/charge_accounts.txt','r')
    line = int(file.readline())
    print(type(line))
    print(line)
    
    while line != '':      # make sure line is a str here to compare correctly
        line = int(line)   # convert line from str to int
        acct.append(line)
        line = file.readline() # read the next record as int
  
 
    print(acct)
    print(type(acct[0]))

    file.close()

    return acct
    
main()
