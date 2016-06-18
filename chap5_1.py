def main():
    total = 0
    for day in ["Sun" , "Mon" , "Tue" , \
                "Wed" , "Thur" , "Fri", \
                "Sat"]:
        print("Today is ", day)
        bugs = int(input("How many bugs did you collect today: "))

        total = total + bugs

    print("You collected ", total , "bugs")

main()
        
          
                         
            
