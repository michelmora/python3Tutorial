# Lists
# A list is defined using square brackets.
c = [5, 2, 10, 48, 32, 16, 49, 10, 11, 32, 64, 55, 34, 45, 41, 23, 26, 27, 72, 18]
print(c[0])
print(c[1])
print(c[-1])
print(len(c))

# DataTypes

fears = ["Spiders", "Ghosts", "Dracula"]
print(fears[-2])

a = {1: 'first', 2: 'second', 3: 'third', 4: 'second'}
val = 'second'
b = [key for key in a if a[key] == val]
c = len(b) > 0 and b[0]
print(c)
print(b)
