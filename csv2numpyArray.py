#This code will convert a csv to a numpy array of floats

import numpy as np

line_school = open("baltimore_fastfood_lifeexp.csv", "rb")
A = ([])
for line in line_school:
    x = [i.strip() for i in line.split(',')]
    #print x
    A.append(x)
B = np.array(A)
#print B
C = B.astype(np.float)   
print C
