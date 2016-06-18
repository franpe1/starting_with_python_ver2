def main():
    number = int(input("Enter a positive number: "))

    while number < 0:
        number = int(input("Please enter a positive number: "))

    print("The number was ",number)

main()
        
