import sys

# Printing Arguments
# print('Arguments:', len(sys.argv) - 1)
# name = input("Enter a name: ")
# x = int(input("What is x?"))
# y = float(input("Write a number"))

print('Arguments:', len(sys.argv))
print('List:', sys.argv)
m = 1
for i in range(1, len(sys.argv)):
    m *= int(sys.argv[i])
print('multiplication:', m)
