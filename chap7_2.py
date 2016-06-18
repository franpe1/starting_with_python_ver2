def main():
    filename = str(input("enter the name of the file: "))
    file = open(filename,"r")

    i = 0
    for i in range(5):
        fileline = file.readline()
        print(fileline)

main()
