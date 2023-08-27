"""6) The source paper [1] suggests that 40% of the mobile phones would be used in fraud. Develop a short
program for mobile phones to perform the following.

a. Ask customer to enter length, width, depth and weight of the package in centimeter and gram,
respectively.

b. Define a function that uses below formula to calculate the volume of the package.
Centimeter cube formula = L x W x D

c. Check if the entered values for length, width and depth comply with the following inspection rule.

If volume is between 1200 cm3 to 1700 cm3 then print ‘information is correct’, otherwise print
‘information is not correct’
If weight is between 50 g and 150 g, then print ‘information is correct’, otherwise print
‘information is not correct’."""

print("Enter all values in centimeter and gram respectively.")
print()
phone_length = int(input("Enter length of phone: "))
phone_width = int(input("Enter width of phone: "))
phone_depth = int(input("Enter depth of phone: "))
phone_weight = int(input("Enter weight of phone: "))

cent_cube_formula = phone_length * phone_width * phone_depth

if cent_cube_formula >= 1200 and cent_cube_formula <= 1700:
	print("information is correct")
else:
	print("information is not correct")

if phone_weight >= 50 and phone_weight <= 150:
	print("information is correct")
else:
	print("information is not correct")
