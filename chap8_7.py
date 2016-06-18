def main():

    # There is prob a better way to do this, but what I found out is
    # that I need to initiate the list first, see below

    glist = []
    blist = []


    ## Procesing the Girls File into an object, but also need to remove the \n
    
    girls_file = open('data/GirlNames.txt' , 'r')

    girls = girls_file.readline()

    while girls != '':
        glist.append(girls.rstrip('\n'))
        girls = girls_file.readline()
    girls_file.close

    ## End of the Girls

    ## Start procesing the boys now the same way we did the Girls
    
    boys_file = open('data/BoyNames.txt', 'r')

    boys = boys_file.readline()
    
    while boys != '':
        blist.append(boys.rstrip('\n'))
        boys = boys_file.readline()
    boys_file.close

    ## End of the Boys

    # Now combine both list into one for simpler search
    allnames = glist + blist


    # Here's where the search happends
    
    cont = 'y'
    while cont == 'y':

    # Basically I can enter both names or one only separeted by a space ex. Juan Sarah
        n = list(str(input("enter name of names to search: ")))

    # NEW STUFF ## Wtih the .split I can convert a string into a list :-)
        name = n.split()


    # So I need to come up with this condition for the case where the user type one name only
    # if I don't do this, then the interpreter will log an indexError for the [1] index
    # So the condition checks if there are two values, assign something to the varialbles, else
    # assign 'Empty' to name2
    
        if len(name) == 2:
            name1 = name[0]
            name2 = name[1]
        else:
            name1 = name[0]
            name2 = 'Empty'

        
    # Performed the Search
        if name1 and name2 in name:
            print('both  names are popular!')
        elif name1 in name:
            print('name {} is popular'.format(name1))
        elif name2 in name:
            print('name {} is popular'.format(name2))
        else:
            print('uhmm none of your names are popular')
                  
    # Continue option at the end
        cont = str(input("continue? "))

main()
