#!/usr/bin/python

def sayHello( msg ):
    print ( "Hello " + str(msg) + " !")

def callme():
    sayHello("Python")
    sayHello(1.11)

x = 10
y = 20

if ( x < y ):
  print ( "x is smaller" )
else:
  print ( "y is smaller" )

if __name__=="__main__":
   callme()
