"""7) Write a short program that will:
a. Prompt users to enter a phone number, state name and number of the products to return.
Number of products cannot be more than 5.
b. For each product, prompt users to enter name of the products as many as defined in a.
c. Define a custom function to use phone number and state name as inputs. Take the last 4-digits of
the phone number, the first 2 letter of the state and the product name in capital letters to create
a return code and print the message ‘Return code {Return Code} has been created for {Product
Name}.’."""

phone_number = str(input("Enter your phone number: "))
state_name = str(input("Enter your state name: (ex. Alabama)").upper())
num_products_return = int(input("Enter the number of products to return: (must be <= 5)"))

if num_products_return == 1:
	name_product1 = str(input("Enter the name of the product 1: "))
	def function0():
		x = (phone_number[-4:] + state_name[:2])
		print("Return code ", x, " has been created for", name_product1, ".")
		return
	function0()
	
elif num_products_return == 2:
	name_product1 = str(input("Enter the name of product 1: "))
	name_product2 = str(input("Enter the name of product 2: "))
	def function0():
		x = (phone_number[-4:] + state_name[:2])
		print("Return code ", x, " has been created for", name_product1, "and", name_product2, ".")
		return
	function0()

elif num_products_return == 3:
	name_product1 = str(input("Enter the name of product 1: "))
	name_product2 = str(input("Enter the name of product 2: "))
	name_product3 = str(input("Enter the name of product 3: "))
	def function0():
		x = (phone_number[-4:] + state_name[:2])
		print("Return code ", x, " has been created for", name_product1, ",", name_product2, "and", name_product3, ".")
		return
	function0()

elif num_products_return == 4:
	name_product1 = str(input("Enter the name of product 1: "))
	name_product2 = str(input("Enter the name of product 2: "))
	name_product3 = str(input("Enter the name of product 3: "))
	name_product4 = str(input("Enter the name of product 4: "))
	def function0():
		x = (phone_number[-4:] + state_name[:2])
		print("Return code ", x, " has been created for", name_product1, ",", name_product2, ",", name_product3, "and", name_product4, ".")
		return
	function0()
	
elif num_products_return == 5:
	name_product1 = str(input("Enter the name of product 1: "))
	name_product2 = str(input("Enter the name of product 2: "))
	name_product3 = str(input("Enter the name of product 3: "))
	name_product4 = str(input("Enter the name of product 4: "))
	name_product5 = str(input("Enter the name of product 5: "))
	def function0():
		x = (phone_number[-4:] + state_name[:2])
		print("Return code ", x, " has been created for", name_product1, ",", name_product2, ",", name_product3, ",", name_product4, "and", name_product5, ".")
		return
	function0()
