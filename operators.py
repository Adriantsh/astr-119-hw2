
def main():

	x = 9 #initializing variables
	y = 3

	# Arithmetic Operators
	print(x+y) 		# addition operator
	print(x-y) 		# subtraction operator
	print(x*y) 		# multiplication operator
	print(x/y) 		# division operator
	print(x%y) 		# modulus operator (remainder after division)
	print(x**y) 	# exponentiation operator
	x = 9.191823
	print(x//y) #floored division

	# Assignment operators
	x = 9		# set x = 9
	x += 3 		# add 3 to x
	print(x) 
	x = 9
	x -= 3   	# subtract 3 from x
	print(x)
	x *= 3  	# multiply x by 3
	print(x)  
	x /= 3  	# divide x by 3
	print(x)
	x **= 3  	# take x to the third power 
	print(x)

	#Comparison operators
	x = 9 
	y = 3 
	print(x==y)		#true if x == y, false otherwise
	print(x!=y) 	#true if x != y, false otherwise
	print(x>y) 		#true if x is greater than y, false otherwise
	print(x<y) 		#true if x is less than y, false otherwise
	print(x>=y) 	#true if x is greater than or equal to , false otherwise
	print(x<=y) 	#true if x is less than or equal to y, false otherwise

if __name__ == "__main__":
	main()