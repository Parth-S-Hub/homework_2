#Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98

Mylist = []
A = input()
A = A.split(',')
for i in A:
    Mylist.append(i)
print(Mylist)    
B =tuple(Mylist)
print(B)