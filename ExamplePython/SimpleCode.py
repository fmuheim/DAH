# ==================================================================
# This is some very simple code to illustrate the basic features of Python
# to programmers who already know Java

#-------------------------------------------------
# This is the equivalent of using packages in Java

from math import *


#------------------------------------------------
# This is how you declare and define a class called "Animal"


class Animal:

    #This is the "Constructor"
    def __init__(self, typeOfAnimal):

        self.type = typeOfAnimal

        if( self.type == 'dog' ):
            self.numberOfLegs = 2
            self.noise = 'Woof'
        elif( self.type == 'dolphin'):
            self.numberOfLegs = 0
            self.noise = 'Squeek'
        else:
            self.type = 'Unknown'
            self.noise = 'Unknown'


    #This is a "Method" which just prints
    def makeNoise( self ):
        print self.noise

    #This is a "Method" which just prints a number
    def numberOfLegs( self ):
        print self.numberOfLegs
    

    #This is a Method which returns a character string
    def myType( self ):
        return self.type
    

    #This is a Method which returns a string
    def whatFood( self ):
        if( self.type == 'dog' ):
            return 'I like dog bisciuits'
        elif( self.type == 'dolphin'):
            return ' I like fish'



#-----------------------------------------------
# This is a bit of functional code to be a main programme
# This demonstrates instantiation of objects and calling of methods

def myMainProgramme():

    #Make some "Objects"
    animal1 = Animal( 'dog')
    animal2 = Animal( 'dolphin')

    print '\n'


    #Tell them to make a noise
    animal1.makeNoise()
    animal2.makeNoise()
    
    print '\n'

    #Find out what food they like
    print 'I am a ',animal1.myType(),' and ',animal1.whatFood()
    print 'I am a ',animal2.myType(),' and ',animal2.whatFood()


#----------------
#How to run it all

myMainProgramme()
