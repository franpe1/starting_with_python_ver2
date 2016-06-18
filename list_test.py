def main():
    values = []
    again = 'y'
    while again == 'y':
        num = int(input('Enter a number: '))
        values.append(num)
        print('Do you want to add another number?')
        again = input('y = yes, anything else = no: ')
        print(values)

main()

        
