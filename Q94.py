#With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.

givenlist = [12,24,35,24,88,120,155,88,120,155]
L = []
[L.append(x) for x in givenlist if x not in L]
L.sort(reverse= True)
print(L)
