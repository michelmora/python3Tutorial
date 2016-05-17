# Strings in Python can be defined using quote symbols.

s = "Hello World"
print(s)

# Strings are an array of characters. You may access character elements of a string using the brackets symbol.
# Computers start counting from zero, thus  s[0] is the first character:

print(s[0])
print(s[-1])

# String Slicing You can slice the string into smaller strings.
# To do so you need to specify either index or both. her a starting, ending index of both
print(s[:3])
print(s[4:])
print(s[1:3])
# If no number is given, such as in s[:3] it will simply take the beginning or end of teh string.
