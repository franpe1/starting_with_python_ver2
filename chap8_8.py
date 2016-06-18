def main():

# Initiate the uspopulation list
    uspl = []

# Open the File , Remove the \n and store in uspl list
    file = open('data/USPopulation.txt','r')
    uspf = file.readline()
    while uspf != '':
        uspl.append(int(uspf.rstrip('\n')))
        uspf = file.readline()
    file.close

# Create a list with the years

    years = list(range(1950,1990+1))

# Call the compute funtion
    compute(years,uspl)


def compute(years,data):

    e = len(data)

# Calculate the average of the population
    s = 0
    yearindex = 0
    for i in data:
        s += i
    avg = s / e

    print('From 1950 to 1990 the avg population was',format(avg,".0f"))
    
# Get the Year with the greated increase in population
# For this first, get the maximum population from the maxp list, then get the index,
# with this index then get the year from the "years" list

    maxp = max(data)
    maxyindex = data.index(maxp)
    maxyear = years[maxyindex]

    print('On {} it was the year with maximum population with {} hab'.format(maxyear,maxp))
    
# Get the year with the smallest increase in population
# Apply the same logic as for the maximum case

    minp = min(data)
    minyearindex = data.index(minp)
    minyear = years[minyearindex]

    print('On {} it was the year with minimum population with {} hab'.format(minyear,minp))

main()
