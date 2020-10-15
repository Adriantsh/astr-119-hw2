
import numpy as np 
import sys

#define a function that returns a value
def expo(x): 			#x is an argument to the function
	return np.exp(x) 	#return the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))  #call the expo func

#define a main function
def main():
	n = 10  # provide a default value for n

	#check if there is command line argument
	if (len(sys.argv)>1):
		n = int(sys.argv(1)) #if addn'l arg provided, set n = arg

	#print the value of n
	print("n is equal to ",n)


	show_expo(n) 		#call the show_expo subroutine

#run the main function
if __name__ == "__main__":
	main()