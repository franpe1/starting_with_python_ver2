def main():
    test_file = open(r"/Users/fraperez/Documents/Python/test1.txt", "w")

    i = 0
    
    for i in range(10):
        message = "This is a test {}\n".format(i)
        test_file.write(message)
    
    test_file.close()

main()
