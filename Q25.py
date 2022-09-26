#Question: Define a class, which have a class parameter and have a same instance parameter.
class Test:
    class_marks = 80

    def __init__(self, class_marks=None):
        self.class_marks = class_marks

print('Marks scored are', Test.class_marks)

Parth = Test()
Parth.class_marks = 100
print('Marks scored are', Parth.class_marks)