import math
import os
import random
import re
import sys
#learnt that unlike java or C you can not change the variables within the for loop it is much similar to foreach lopp tham for loop have to use while loop instead
# Complete the jumpingOnClouds function below.
#start from 0 
#jump 2 inxdexes ahead , if index value is a 1 then jump only one index , go until last index 
def jumpingOnClouds(c):
    count = 0;
    i = 0
    while (i <= len(c)-2):
        if (i != len(c)-2 ):
            if (c[i+2] == 0):
                count+= 1            
                i+=2
                #print("Index: ", i, "Count: ", count)
                #increase by 2
            else:
                count+=1
                i += 1
                #print("Else..... Count: ", count, "Index: ", i)
                #increase by 1
        else:
            if (c[i+1] == 0):
                count+= 1            
                i+=1
    return count



list2 = [0, 0, 0, 1, 0, 0];
print("Final Count", jumpingOnClouds(list2))
