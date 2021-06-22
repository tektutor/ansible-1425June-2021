#!/usr/bin/python

def readFile ( filename ):
    f = open ( filename, "r" )
    print ( f.read() )
    f.close() 

def writeFile ( filename ):
    f = open ( filename, "w+" )
    f.write ( "First line\n" )
    f.write ( "Second line\n" )
    f.close()


readFile( "files.py" )
writeFile("test.txt")
