#!/usr/bin/python

def printNumbers( x ):
    for index in x:
      print ( index )

def loop2( ):
   print ( "While loop" )
   x = 0
   while ( x < 5 ):
    print ( x ) 
    x = x + 1 
   print ( "End of While loop function" )

def loop3():
   x = 0

num = [ 10, 20, 30 ]
printNumbers( num )

print ( 10 in num )

print ( len(num) ) 

loop2()
loop3()
