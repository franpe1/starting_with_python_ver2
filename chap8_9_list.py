def main():
    table = []

    file = open('data/WorldSeriesWinners.txt','r')
    wswf = file.readline()

    while wswf != '':
    
        for i in range(1903,2009):
            if i != 1904 and i != 1994:
                table.append([i,str(wswf.rstrip('\n'))])
                wswf = file.readline()

    file.close()

    print(table)

main()
