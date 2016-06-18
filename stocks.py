totalShares = int(input("Enter number or shares: "))
pricePerShare = float(input("Enter price per share: "))

totalPrice = totalShares * pricePerShare

brokerFeeB = totalPrice * 0.02

print("You paid ","$",format(totalPrice,",.2f"), "for your stocks \n" \
      "You paid ","$",format(brokerFeeB,",.2f"), "of broker fees to buy the stocks")

sharesSold = int(input("How many shares did you sell: "))
pricePerShareSold = float(input("What was the sold price per share: "))

totalPriceSell = sharesSold * pricePerShareSold

brokeFeeSell = totalPriceSell * 0.02

#  print("You sold ","$",format(
