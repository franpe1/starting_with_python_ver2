def main():
    numberfile = open('number_file.txt', 'w')
    for i in range (101):
        n = str(i) + "\n"
        numberfile.write(n)
    numberfile.close()

main()
