# Documentation Strings
# Here are some conventions about the content and formatting of documentation strings.
# The first line should always be a short, concise summary of the object’s purpose. For brevity, it should not
# explicitly state the object’s name or type, since these are available by other means (except if the name happens to
# be a verb describing a function’s operation). This line should begin with a capital letter and end with a period.
# If there are more lines in the documentation string, the second line should be blank, visually separating the summary
# from the rest of the description. The following lines should be one or more paragraphs describing the object’s
# calling conventions, its side effects, etc.
# The Python parser does not strip indentation from multi-line string literals in Python, so tools that process
# documentation have to strip indentation if desired. This is done using the following convention. The first non-blank
# line after the first line of the string determines the amount of indentation for the entire documentation string.
# (We can’t use the first line since it is generally adjacent to the string’s opening quotes so its indentation is not
# apparent in the string literal.) Whitespace “equivalent” to this indentation is then stripped from the start of all
# lines of the string. Lines that are indented less should not occur, but if they occur all their leading whitespace
# should be stripped. Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).

# Example


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)


# Do nothing, but document it.

# No, really, it doesn't do anything.

# Function annotations are completely optional metadata information about the types used by user-defined functions
# (see PEP 484 for more information).

# Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any
# other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an
# expression evaluating to the value of the annotation. Return annotations are defined by a literal ->, followed by
# an expression, between the parameter list and the colon denoting the end of the def statement. The following example
# has a positional argument, a keyword argument, and the return value annotated:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


print(f('spam'))
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'
