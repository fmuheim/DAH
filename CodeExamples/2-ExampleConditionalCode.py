# ==================================================================
# This is some very simple code to illustrate control loops in python


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
# It also introduces lists which are very useful in python

def myMainProgramme():

    #Make some "Objects" in a for loop
    
    # THis makes an empty list
    animals = []
    
    
    # This adds instances of animal objects
    for i in range(0,5):
        animals.append(Animal( 'dog' ) )
    for i in range(0,4):
        animals.append(Animal( 'dolphin' ) )
   
   
    # This accesses the list
    for i in range(0,len(animals)):
        print animals[i].myType()
    
    print '\n'


    # This shows a conditional statement
    for i in range(0,len(animals)):
        if( animals[i].myType() == 'dog' ):
          print animals[i].whatFood()



#----------------
#How to run it all

myMainProgramme()
