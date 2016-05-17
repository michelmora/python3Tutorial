# Range
range(5)
#  0, 1, 2, 3, 4

range(5, 10)
# 5, 6, 7, 8, 9

range(0, 10, 3)
# 0, 3, 6, 9

range(-10, -100, -30)
# -10, -40, -70

list(range(5))
# [0, 1, 2, 3, 4]

# Break statement, like in C, breaks out of the smallest enclosing for or while loop.

# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list
# (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
#  This is exemplified by the following loop, which searches for prime numbers:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

# When used with a loop, the else clause has more in common with the else clause of a try statement than it does that
# of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs
# when no break occurs.

# Continue statement
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# Found an even number 2
# Found a number 3
# Found an even number 4
# Found a number 5
# Found an even number 6
# Found a number 7
# Found an even number 8
# Found a number 9

# Pass statement
# The pass statement does nothing. It can be used when a statement is required syntactically but the program
# requires no action

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# This is commonly used for creating minimal classes:

class MyEmptyClass:
    pass


# Another place pass can be used is as a place-holder for a function or conditional body when you are working on
# new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:

def initlog(*args):
    pass  # Remember to implement this!
