# ---------------------------------
# Part 1  :  Writing text to a file

# First open a new file

print("\n *** Part 1 ")

fileout = open("mydata.dat","w")


# Now write some lines of text to it

fileout.write("Long ago in a galaxy far, far away")
fileout.write("It is a period of civil war.")
fileout.write("Rebel spaceships, striking from a hidden base, have won")
fileout.write("their first victory against the evil Galactic Empire.")


# Now close it
fileout.close()


# ---------------------------------
# Part 2  :  Part 1 didnt format things very well
# Lets do better

# First open a new file

print("\n *** Part 2 ")

fileout = open("mydata.dat","w")


# Now write some lines of text to it

fileout.write("\n Long ago in a galaxy far, far away")
fileout.write("\n It is a period of civil war.")
fileout.write("\n Rebel spaceships, striking from a hidden base,")
fileout.write("\n have won their first victory against the evil Galactic Empire.")


# Now close it
fileout.close()


# ----------------------------------
# Part 3
# Probably you dont want to explicitly convert every item to a string

# As example if you have produced a list of numbers

print("\n *** Part 3 ")

myList = [1,2,3,4,5,6]

fileout = open("mydata.dat","w")
fileout.write(str(myList))
fileout.close()



# ----------------------------------
# Part 4
# Read the file back in again and print to the screen
print("\n *** Part 4 ")


filein = open("mydata.dat","r")
lines = filein.readlines()
filein.close()

for line in lines:
    print(line)

