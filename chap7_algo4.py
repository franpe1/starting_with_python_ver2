
def main():
    sum = 0
    
    numberfile = open('number_file.txt','r')

    line = numberfile.readline()

    while line != '':
        a = int(line)
        sum += a
        line = numberfile.readline()
    
    print(sum)
    numberfile.close()

main()
                      
