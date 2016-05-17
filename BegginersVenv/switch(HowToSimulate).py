# An if ... elif ... elif ... sequence is a substitute for the switch or case statements found in other languages.


# OPTION No.1
def dog_sound():
    return 'hau hau'


def cat_sound():
    return 'Me au'


def horse_sound():
    return 'R R R R'


def cow_sound():
    return 'M U U U'


def no_sound():
    return "Total silence"


switch = {
    'dog': dog_sound,
    'cat': cat_sound,
    'horse': horse_sound,
    'cow': cow_sound,
}


# value = input("Enter the animal: ")
# if value in switch:
#     sound = switch[value]()
# else:
#     sound = no_sound()
#     # default
#
# print(sound)

# OPTION No.2
# define the function blocks
def zero():
    print("You typed zero.\n")


def sqr():
    print("n is a perfect square\n")


def even():
    print("n is an even number\n")


def prime():
    print("n is a prime number\n")


# map the inputs to the function blocks
options = {0: zero,
           1: sqr,
           4: sqr,
           9: sqr,
           2: even,
           3: prime,
           5: prime,
           7: prime,
           }


# options[10]()


# OPTION NO. 3
# A very elegant way
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")


print(numbers_to_strings(2))


# OPTION NO. 4
# Dictionary Mapping for Functions
def zero():
    return "zero"


def one():
    return "one"


def numbers_to_functions_to_strings(argument):
    switcher = {
        0: zero,
        1: one,
        2: lambda: "two",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()


print(numbers_to_functions_to_strings(3))


# OPTION NO. 5
# Dispatch Methods for Classes
# If we don't know what method to call on a class, we can use a dispatch method to determine it at runtime.
class Switcher(object):
    def numbers_to_methods_to_strings(self, argument):
        """Dispatch method"""
        # prefix the method_name with 'number_' because method names
        # cannot begin with an integer.
        method_name = 'number_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "nothing")
        # Call the method as we return it
        return method()


def number_2(self):
    return "two"


def number_0(self):
    return "zero"


def number_1(self):
    return "one"


tes = Switcher()
print(tes.numbers_to_methods_to_strings(4))
