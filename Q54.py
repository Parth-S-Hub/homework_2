#Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class square(shape):
    def __init__(self,length):
        shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Sq = square(10)
print(Sq.area())

