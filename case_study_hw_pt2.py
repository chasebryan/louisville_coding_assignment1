"""5) Write a short program to perform the following tasks.

a. Ask customer to enter which WH they would like to return the product and enter an estimated
distance (in miles). Once completed and confirmed, the program will return a price quote as per
Table 1. Due to the limited scope of the current knowledge area, confirmation is granted without
retrieving and checking from an internal database.

b. Ask customer if they want to change their choice of warehouse as Y/N question. If the answer is
Y, then ask again which WH they would like to use and quote the new price accordingly. If answer
is N, print the message ‘Return warehouse is {WH name}.’ Check if the chosen WH is accepting
returns, if not then print ‘You cannot choose {WH name} for returning your product.’.

c. Calculate the cost of handling and shipping from {WH name} to WH3."""

import os
import sys

product_return = int(input("Which warehouse are you returning from? (Enter a number 1-4) "))
product_return2 = int(input("Which warehouse are you returning to? (Enter a number 1-4) "))
estimated_miles = int(input("How many miles are you shipping from? (Enter a number) "))
print()

if product_return == 1 and product_return2 == 1: #wh1 to wh1
	if estimated_miles < 5:
		print("Your total cost is: $4")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $8")
	if estimated_miles >= 10:
		print("Your total cost is: $12")

if product_return == 1 and product_return2 == 2: #wh1 to wh2
	if estimated_miles < 5:
		print("Your total cost is: $12")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $16")
	if estimated_miles >= 10:
		print("Your total cost is: $20")

if product_return == 1 and product_return2 == 3: #wh1 to wh3
	if estimated_miles < 5:
		print("Your total cost is: $16")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $20")
	if estimated_miles >= 10:
		print("Your total cost is: $24")

if product_return == 1 and product_return2 == 4: #wh1 to wh4
	if estimated_miles < 5:
		print("Your total cost is: $22")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $26")
	if estimated_miles >= 10:
		print("Your total cost is: $30")
		
#-----------------------------------------------------------------------

if product_return == 2 and product_return2 == 1: #wh2 to wh1
	if estimated_miles < 5:
		print("Your total cost is: $14")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $15")
	if estimated_miles >= 10:
		print("Your total cost is: $22")

if product_return == 2 and product_return2 == 2: #wh2 to wh2
	if estimated_miles < 5:
		print("Your total cost is: $6")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $7")
	if estimated_miles >= 10:
		print("Your total cost is: $14")

if product_return == 2 and product_return2 == 3: #wh2 to wh3
	if estimated_miles < 5:
		print("Your total cost is: $16")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $17")
	if estimated_miles >= 10:
		print("Your total cost is: $24")

if product_return == 2 and product_return2 == 4: #wh2 to wh4
	if estimated_miles < 5:
		print("Your total cost is: $21")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $22")
	if estimated_miles >= 10:
		print("Your total cost is: $29")

#-----------------------------------------------------------------------

if product_return == 3 and product_return2 == 1: #wh3 to wh1
	if estimated_miles < 5:
		print("Your total cost is: $17")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $22")
	if estimated_miles >= 10:
		print("Your total cost is: $22")

if product_return == 3 and product_return2 == 2: #wh3 to wh2
	if estimated_miles < 5:
		print("Your total cost is: $15")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $20")
	if estimated_miles >= 10:
		print("Your total cost is: $20")

if product_return == 3 and product_return2 == 3: #wh3 to wh3
	if estimated_miles < 5:
		print("Your total cost is: $5")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $10")
	if estimated_miles >= 10:
		print("Your total cost is: $10")

if product_return == 3 and product_return2 == 4: #wh3 to wh4
	if estimated_miles < 5:
		print("Your total cost is: $12")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $17")
	if estimated_miles >= 10:
		print("Your total cost is: $17")

#-----------------------------------------------------------------------

if product_return == 4 and product_return2 == 1: #wh4 to wh1
	if estimated_miles < 5:
		print("Your total cost is: $26")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $29")
	if estimated_miles >= 10:
		print("Your total cost is: $33")

if product_return == 4 and product_return2 == 2: #wh4 to wh2
	if estimated_miles < 5:
		print("Your total cost is: $23")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $26")
	if estimated_miles >= 10:
		print("Your total cost is: $30")

if product_return == 4 and product_return2 == 3: #wh4 to wh3
	if estimated_miles < 5:
		print("Your total cost is: $15")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $18")
	if estimated_miles >= 10:
		print("Your total cost is: $22")

if product_return == 4 and product_return2 == 4: #wh4 to wh4
	if estimated_miles < 5:
		print("Your total cost is: $8")
	if estimated_miles >= 5 and estimated_miles < 10:
		print("Your total cost is: $11")
	if estimated_miles >= 10:
		print("Your total cost is: $15")
			

question = str(input("Would you like to change your choice of warehouse? (Y or N) "))
if question == ('n' or 'N'):
	print("Return warehouse is ", product_return2)
	if product_return2 == 3:
		print("You cannot choose warehouse 3 for returning your product")
elif question == ('y' or 'Y'):
	os.execl(sys.executable, sys.executable, *sys.argv)
	

#-----------------------------------------------------------------------
