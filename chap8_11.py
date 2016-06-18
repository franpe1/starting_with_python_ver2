def main():

    days = ['Su','Mo','Tu','We','Th','Fr','Sa']
    sale = [0,0,0,0,0,0,0]
    x = 0
     
    for i in days:
        sale[x] = float(input("enter sales for {} ".format(i)))
        x += 1
            
    total = cal(sale)
    print("the total sales for the week is {} ".format(total))
    

def cal(list):
    total = 0
    for n in list:
        total = total + n
    return total

main()
                        
        
