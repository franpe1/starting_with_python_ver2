def main():
    file = open("random.txt","r")

    total = 0
    count = 0

    line = file.readline()

    while line != '':
        
        print(line.rstrip('\n'))
        total += int(line)
        count += 1
        line = file.readline()
    
    print("total is {}".format(total))
    print("total items is {}".format(count))
    file.close()

main()
