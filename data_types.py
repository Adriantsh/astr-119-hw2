import numpy as np #import numpy

#integers
i = 10 #integer
print("The type of i is ", type (i))

a_i = np.zeros(i,dtype=int) #an array of ints
print("The type of a_i is ", type(a_i))	#print out the type
print("The type of a_i[0] is ", type(a_i[0]))  #print out the type

#floats
x = 119.0 #floating point number
print("The type of x is ",type(x)) #print out the type

y = 1.19e2 #sci not float
print("The type of y is ",type(x)) #print out the type


z = np.zeros(i,dtype=float) #declare an array of floats
print(type(z))  #print out type
print(type(z[0])) #print out type


#a 2d array
m = np.zeros((2,2),dtype=float) #declare an array of floats
m[0,0] = 1.0
m[1,1] = 1.0
print(m)