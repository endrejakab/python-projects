#!/usr/bin/python3
import numpy as np                                                      #  import numy for random number generation
abc = np.random.choice(list(range (1,16)), size = 15, replace = False)  #  generate an array of random numbers between 1-15
#abc = arr.array('h', [12,2,3,1,10,14,9,8,4,11,13,15,5,7,6])            #  give an array
print("The generated array is: ", abc)                                  #  list array
b, i, n= 0, 0, 0                                                        #  b is counter, n is the first member of array
m = 1                                                                   #  m is the second member of array
l = len(abc)                                                            #  length of array
for i in abc:                                                           #  iterate over array
    while n < l and m < l:                                              #  to eliminate never ending cycles
        if abc[n] > abc[m]:                                             #  if the first element is higher then the second
            b += 1                                                      #  step counter by one
            m += 1                                                      #  go to the third element and compare
        else:
            m += 1                                                      #  do not setp counter, and go to the third element
    n += 1                                                              #  if m reached l then step n by one
    m = n + 1                                                           #
print("Number of inversions: ", b)                                              #the number of inversions
if (b % 2 == 0):                                                        #if it is par, then can be solved
    print("The problem is solvable.")                                        
else:
    print("Th problem is not solvable.")                                #if it is impar, then can not be solved