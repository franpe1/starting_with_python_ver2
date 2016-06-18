def main():
    test_file = open(r"/Users/fraperez/Documents/Python/test1.txt", "r")

    read_file1 = test_file.readline()
    read_file2 = test_file.readline()
    read_file3 = test_file.readline()

    print(read_file1.rstrip('\n'))
    print(read_file2.rstrip('\n'))
    print(read_file3.rstrip('\n'))
    
    test_file.close()

main()
