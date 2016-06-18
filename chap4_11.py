def main():
    seconds = int(input("Enter the number of seconds: "))
    compute(seconds)

def compute(sec):
    if sec >= 60 and sec < 3600:
        minutes = sec / 60
        remain = sec % 60
        print("There are ",format(minutes,".0f")," minutes and",remain," seconds")
    elif sec >= 3600 and sec < 86400:
        hours = sec / 3600
        remain = sec % 3600
        print("There are ",format(hours,".0f")," hours and",remain," seconds")
    elif sec >= 86400:
        days = sec / 86400
        remain = sec % 86400
        print("There are ",format(days,".0f")," days and",remain," seconds")

main()
              
              
