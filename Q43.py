#Write a program to generate and print another tuple whose
# values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
giventuple=(1,2,3,4,5,6,7,8,9,10)
NewList=[]
for i in giventuple:
	if giventuple[i-1]%2==0:
		NewList.append(giventuple[i-1])

NewTuple=tuple(NewList)
print(NewTuple)