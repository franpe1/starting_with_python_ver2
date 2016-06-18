totalFood = float(input("Enter total for food: "))

tax = totalFood * 0.07
tip = totalFood * 0.15
total = totalFood + tax + tip

print("Your total for food:","\t","$",format(totalFood,"10,.2f"),"\n", \
      "Your tax is: ","\t","\t","$",format(tax,"10,.2f"),"\n", \
      "Your tip is: ","\t","\t","$",format(tip,"10,.2f"),"\n", \
      "Your total is: ","\t","$",format(total,"10,.2f"),"\n")
