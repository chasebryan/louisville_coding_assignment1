"""4) Write a short program that asks to a customer the following information.
• Name
• Last Name
• Email Address
• Age
• Address
• Zip Code
• State
• Phone Number
• Name of the Product
• Value of the Product in USD
Your program should consider the following validation rules.
a. Make all the letters lowercase in string values.
b. Phone number should not be longer than 10 characters. If an entry is longer than 10 characters,
the program will return the message ‘Phone number cannot be more than 10 characters.’ and ask
customer to re-enter a valid phone number.
c. Zip code cannot be a negative value. If an entry is negative, return the message ‘Zip code is wrong’
and prompt the user to enter all the information again. If the zip code is valid, prompt the user
with a message ‘Information are entered correctly’. (Hint: Use while loop.)"""

name = input("Enter first name: ")
last_name = input("Enter last name: ")
email_address = input("Enter email address: ")
age = input("Enter age: ")
address = input("Enter address: ")
zip_code = int(input("Enter zip code: "))

while zip_code < 0:
	print("Zip code is wrong.")
	zip_code = int(input("Enter zip code again: "))
	if zip_code > 0:
		print("Information are entered correctly")
		break

state = input("Enter state: ")
phone_number = input("Enter phone number: ")

while len(phone_number) > 10:  #configures phone number to be <= 10
	print("Phone number cannot be more than 10 characters.")
	phone_number = input("Enter phone number again: ")
	if len(phone_number) <= 10:
		break
	
name_product = input("Enter name of the product: ")
value_product = input("Enter value of the product in USD: ")


