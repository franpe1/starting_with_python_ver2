def main():

    wswlist = gettable()  # call the get table funtion below
    yearswon =[]

#   print(wswlist)


# Enter the team name
    team = str(input("enter the team: "))

    c = 0

#** This Took me a while to figure it out ** ##
#   The data is on a 2D table with year,team
#   so, for each row 'n' it will search 'team'
#   in 'wswlist[n]' list
#   if there is match it will add the year [n],[0]
#   to the yearwon list and then it will have a counter
#   for each ocurrence (if there a multiples)
#   (title funtion will uppercase the initial letter
#   so it can be lower or UPPER case)
#**  

    for n in range(len(wswlist)):
        if team.title() in wswlist[n]:
            yearswon.append(wswlist[n][0])
            c += 1
            
# print the result
    print("your team won {} times between 1903 and 2009, in the following years".format(c))
    print(yearswon)


### This funtion will call the file and create a 2D list with the wining team
### and the year
    
def gettable():
    table = []

    file = open('data/WorldSeriesWinners.txt','r')
    wswf = file.readline()

    while wswf != '':
        for i in range(1903,2009):
            if i != 1904 and i != 1994:
                table.append([i,str(wswf.rstrip('\n'))])
                wswf = file.readline()

    file.close()
    return table

main()
