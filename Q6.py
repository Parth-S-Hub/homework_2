#Question: Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math
C = 50
H = 30
Ans =[]
values = [a for a in input().split(',')]
for x in values:
    Ans.append(str(int(math.sqrt(2*C*int(x)/H))))
print((','.join(Ans)))
      


