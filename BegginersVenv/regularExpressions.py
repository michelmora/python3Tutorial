# Regular Expressions may be used to test if a string (Text) is according to a certain grammar.
# Sometimes Regular Expressions are called regex or regexp.
import re

s = "Are you afraid of ghosts?"
print("ghosts" in s)
print("coffee" not in s)

s = "12345"
matcher = re.match('\d{5}\Z', s)

if matcher:
    print("True")
else:
    print("False")

# \d 	Matches a decimal digit; equivalent to the set [0-9].
# \D 	The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
# \s 	Matches any whitespace character; equivalent to [ \t\n\r\f\v].
# \S 	The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
# \w 	Matches any alphanumeric character; equivalent to [a-zA-Z0-9_].
# \W 	Matches the complement of \w.
# \b 	Matches the empty string, but only at the start or end of a word.
# \B 	Matches the empty string, but not at the start or end of a word.
# \\ 	Matches a literal backslash.
