from random import randint

# To read a file
filename = "readme.txt"
with open(filename) as fn:
    content = fn.readlines()
print(content)

# To write a file
f = open("output.txt", "w")
f.write("Testing Python Programming language, \n")
f.write("Example Program.")
f.close()

# To append text at the end of a file
filename = "output.txt"
x = randint(0,9)
with open(filename, "a") as myFile:
    myFile.write("\n" + str(x) + "appended text for testing")
