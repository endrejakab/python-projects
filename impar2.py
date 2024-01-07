#!/usr/bin/python3
import random
abc = random.sample((range(1,16)), 15)
print("A generalt szamsor: ", abc)                                      #list array
b, i, n= 0, 0, 0                                                        #b is counter, n is the first member of array
m = 1                                                                   #m is the second member of array
l = len(abc)                                                            #length of array
for i in abc:                                                           #iterate over array
    while n < l and m < l:                                              #to eliminate never ending cycles
        if abc[n] > abc[m]:                                             #if the first element is higher then the second
            #print(abc[n], abc[m])
            b += 1                                                      #step counter by one
            m += 1                                                      #go to the third element and compare
        else:
            #print(abc[n], abc[m])
            m += 1                                                      #do not setp counter, and go to the third element
    n += 1                                                              #if m reached l then step n by one
    m = n + 1                                                           #
print("Cserek szama: ", b)                                              #the number of inversions
if (b % 2 == 0):                                                        #if it is par, then can be solved
    print("Megoldhato rejtveny")                                        
else:
    print("Nem megoldhato rejtveny")                                    #if it is impar, then can not be solved