def main():
    rain_list = [i * 0 for i in range(12)]
    month = ['Jan','Feb','Mar','Apr','May','Jun',
             'Jul','Aug','Sep','Oct','Nov','Dec']
             
    for i in range(len(month)):
        rain_list[i] = float(input("Enter rain level for month #{} ".format(i)))

    result = compute(rain_list)

    print("Total rain fo rthe year is {}\n \
           The min level of rain was {}\n \
           The max level of rain was {}".format(result[0],result[1],result[2]))

def compute(rain_list):
    TotalRain = 0
    menor = 0
    mayor = 0
    for i in range(len(rain_list)):
        TotalRain += rain_list[i]
    avrg = TotalRain / 12
    menor = min(rain_list)
    mayor = max(rain_list)

    return TotalRain , avrg, menor , mayor

main()
    
