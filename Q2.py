#Question: Write a program which can compute the factorial of a given number.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:

A = input()
A = int(A)
count = A-1 
if A == 1:
    factorial = 1
while count > 1:
    A *= count
    count = count -1
factorial = A
print(factorial)
