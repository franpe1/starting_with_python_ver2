import sys
sys.path.insert(1,'/Library/Python/2.7/site-packages/')
import pymysql

# Open database connection

db = pymysql.connect("localhost","root","hola12","bookstore" )

    
# prepare a cursor object using cursor() method

cursor = db.cursor()


title = ""

cont = "Y"

entrada = input("Update book database? ")

if entrada == "Y" or entrada == "y":

    while cont == "Y" or cont == "y":
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        price = float(input("Enter book price: "))

        pushdata = "INSERT into books (title, author, price) VALUES (\"{}\",\"{}\",\"{}\")" \
                   .format(title , author , price)
       # print(pushdata)
        cursor.execute(pushdata)

        cont = input("More Books? ")
    
        db.commit()


#dale = "INSERT into books (title,author,price) VALUES (\"test33\",\"testy\",\"1.99\")"
#cursor.execute(dale)
#db.commit()
                  


#idBook = int(input("Enter the id of the book: "))

#all = "SELECT * from books WHERE id = %s" % (idBook)

all = "SELECT * from books"

    
# execute SQL query using execute() method.
cursor.execute(all)

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
desc = cursor.description

print("{:3}".format(desc[0][0]) , "{:20}".format(desc[1][0]) , \
      "{:25}".format(desc[2][0]) , "{:10}".format(desc[3][0]))

total = 0

for row in data:
    print (row[0] , "{:20}".format(row[1]) , "{:25}".format(row[2]) ,  \
           "{:10}".format((row[3])))
    price = float(row[3])
    total += price

print("Total","{:55}".format(total,"5,.2f"))

# disconnect from server
cursor.close()
db.close()
