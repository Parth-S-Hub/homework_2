#Define a function which can generate and print a list where the
# values are square of numbers between 1 and 20 (both included).
def Power():
    power = []
    for i in range(1,21):
        A = i**2
        power.append(A)

    print(power)

Power()
