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

# More on Lists
# The list data type has some more methods. Here are all of the methods of list objects:

x = 25
i = 1
y = 22
my_list = [x]
L = [y]

# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

my_list.extend(L)
# Extend the list by appending all the items in the given list. Equivalent to a[len(a):] = L.

my_list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

my_list.remove(x)
# Remove the first item from the list whose value is x. It is an error if there is no such item.

my_list.pop(i)
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and
# returns the last item in the list. (The square brackets around the i in the method signature denote that the
# parameter is optional, not that you should type square brackets at that position. You will see this notation
# frequently in the Python Library Reference.)

my_list.index(x)
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.

my_list.count(x)
# Return the number of times x appears in the list.

my_list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for
# their explanation).

my_list.reverse()
# Reverse the elements of the list in place.

my_list.copy()
# Return a shallow copy of the list. Equivalent to a[:].

my_list.clear()
# Remove all items from the list. Equivalent to del a[:].

# How to use it. Samples

a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x'))
# 2 1 0
a.insert(2, -1)
a.append(333)
# a
# [66.25, 333, -1, 333, 1, 1234.5, 333]
a.index(333)
# 1
a.remove(333)
# a
# [66.25, -1, 333, 1, 1234.5, 333]
a.reverse()
# a
# [333, 1234.5, 1, 333, -1, 66.25]
a.sort()
# a
# [-1, 1, 66.25, 333, 333, 1234.5]
a.pop()
# 1234.5
# a
# [-1, 1, 66.25, 333, 333]
