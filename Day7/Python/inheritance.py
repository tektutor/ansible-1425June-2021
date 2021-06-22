#!/usr/bin/python

class Parent:
    def __init__(self):
        self.x = 10
        self.y = 20

    def printValues(self):
        print ( "X = " + str ( self.x ) )
        print ( "Y = " + str ( self.y ) )

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.z = 30

    def printValues(self):
        Parent.printValues(self)
        print ( "Z = " + str ( self.z ) )


if __name__ == "__main__":
    obj = Child()
    obj.printValues()
        
