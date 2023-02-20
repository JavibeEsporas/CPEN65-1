#Creating an Array Data Structure

import array as arr
 
a = arr.array('i', [1, 2, 3, 4, 5])
 
#Print only the numbers between 0 and 3
for i in range (0, 3):
    print (a[i], end =" ")
