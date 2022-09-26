#Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length*self.width
        print("The area is", self.area, "sq.cm")


Big = rectangle(10,50)
Big.area()
