# Default Argument Values
# The most useful form is to specify a default value for one or more arguments. This creates a function that can be
# called with fewer arguments than it is defined to allow


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


# This function can be called in several ways:

# giving only the mandatory argument:
# ask_ok('Do you really want to quit?')
# giving one of the optional arguments:
# ask_ok('OK to overwrite the file?', 2)
# or even giving all arguments:
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# The default values are evaluated at the point of function definition in the defining scope, so that

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


# will print 5

# Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable
# object such as a list, dictionary, or instances of most classes. For example, the following function accumulates
# the arguments passed to it on subsequent calls:
#
# def f(a, l=[]):
#     l.append(a)
#     return l
#
#
# print(f(1))
# print(f(2))
# print(f(3))


# This will print

# [1]
# [1, 2]
# [1, 2, 3]

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

def g(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l


print(g(1))
print(g(2))
print(g(3))


# Functions can also be called using keyword arguments of the form kwarg=value.

# When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict)
# containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a
# formal parameter of the form *name (described in the next subsection) which receives a tuple containing the
# positional arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a
# function like this:


def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


# Note that the list of keyword argument names is created by sorting the result of the keywords dictionary’s keys()
# method before printing its contents; if this is not done, the order in which the arguments are printed is undefined.

# It could be called like this:

cheese_shop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")


# def function_name(arguments, arguments tuple, argumetns dictionary)
# def function_name('arg_ex', 'arg_tup_ex_1', 'arg_tup_ex_2', key_dict_1='value1', key_dict_2='value2', )
# to get the first parameter just use arg_ex parameter name
# to get the positional parameters use
#     for arg in arguments:
#         print(arg)
# to get the keyword arguments use
#     for kw in keys:
#         print(kw, ":", keywords[kw])

# Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of
# arguments. These arguments will be wrapped up in a tuple. Before the variable number of
# arguments, zero or more normal arguments may occur.
def concat(*args, sep="/"):
    return sep.join(args)


concat("earth", "mars", "venus")
# 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'

# The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function
# call requiring separate positional arguments. For instance, the built-in range() function expects separate start and
# stop arguments. If they are not available separately, write the function call with the *-operator to unpack the
# arguments out of a list or tuple:
list(range(3, 6))  # normal call with separate arguments
# [3, 4, 5]
args = [3, 6]
list(range(*args))  # call with arguments unpacked from a list


# [3, 4, 5]

# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

# Lambda Expressions
# Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments:
# lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically
# restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition.
# Like nested function definitions, lambda functions can reference variables from the containing scope:


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
# 42
print(f(10))
# 43

# The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
