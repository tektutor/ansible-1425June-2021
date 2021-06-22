#!/usr/bin/python

class MyClass:
   def __init__(self):
       print ( "Constructor got invoked ...")
       self.x = 0
       self.y = 0

   def setValues(self, x,y):
       self.x = x
       self.y = y

   def printValues(self):
       print ( "Value of x = ", self.x )
       print ( "Value of y = ", self.y )

print ( "Object 1 ")
obj1 = MyClass()
obj1.setValues ( 10, 20 )
obj1.printValues()
print ( "##########################")

print ( "Object 2 ")
obj2 = MyClass()
obj2.setValues ( 100, 200 )
obj2.printValues()
print ( "##########################")
