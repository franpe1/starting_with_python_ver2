price=float(input('Enter the price of your item: '))

sales_tax = price * 0.04
county_tax = price * 0.02

price_final = price + sales_tax + county_tax

print('The ammount of your item is: ',"\t",'$',format(price,'10,.2f'),'\n',\
      'Sales tax is: ','\t','\t','$',format(sales_tax,'10,.2f'),'\n',\
      'County tax is: ','\t','\t','$',format(county_tax,'10,.2f'),'\n',\
      'Total price is: ','\t','\t','$',format(price_final,'10,.2f'))
