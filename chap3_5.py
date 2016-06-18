COUNTY_PROPVAL = 0.60
COUNTY_PROPTAX = 0.0064

def main():
    value = float(input("Enter the value of the home/land: "))
    compute(value)

def compute(a):
    propertyValue = a * COUNTY_PROPVAL
    propertyTax = propertyValue * COUNTY_PROPTAX

    print("The value of your property is ",propertyValue, \
          "and your property tax is ",propertyTax)
    
main()
