#Write a function to compute 5/0 and use try/except to catch the exceptions.
#Hints: Use try/except to catch exceptions.
def division(x,y):
    try:
        Z = x/y
    except ZeroDivisionError:
        print("Cannot compute division by zero, Enter values again")
    else:
        print("The value is", Z)

division(10,0)