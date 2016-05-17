# For loops
# The last number (11) is not included. This will output the numbers 1 to 10.
# for i in range(1, 11):
#     print(i)
# Python itself starts counting from 0, so this code will also work but will output 0 to 9
# for i in range(0, 10):
#     print(i)
# equivalent to
for i in range(10):
    print(i)
# using list
x = [i for i in range(10)]
print(x)
# using dict
list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', ]
y = {i: list_[i] for i in range(len(list_))}
print(y)
# equivalent to
z = dict(enumerate(list_))
print(z)
a = 42
b = list(a + i for i in range(10))
print(b)
c = 42
d = [a + i for i in range(10)]
print(b)

print(list(range(5)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:  # loop fell through without finding a factor
        print(n, 'is a prime number')

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
# cat 3
# window 6
# defenestrate 12

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
# ['defenestrate', 'cat', 'window', 'defenestrate']
