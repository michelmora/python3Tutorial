# Objects are Python’s abstraction for data. All data in a Python program is represented by objects or
# by relations between objects. (In a sense, and in conformance to Von’s(python creator) model of a
# “stored program computer ”, code is also represented by objects.)

# Objects are never explicitly destroyed; however, when they become unreachable they may be garbage-collected.

# Note that the use of the implementation’s tracing or debugging facilities may keep objects alive that would
# normally be collectible. Also note that catching an exception with a ‘try...except‘ statement may keep objects alive.

# None
# This type has a single value. There is a single object with this value. This object is accessed through the built-in
# name None. It is used to signify the absence of a value in many situations, e.g., it is returned from functions that
# don’t explicitly return anything. Its truth value is false.

# NotImplemented
# This type has a single value. There is a single object with this value. This object is accessed through the built-in
# name NotImplemented. Numeric methods and rich comparison methods should return this value if they do not implement the
# operation for the operands provided. (The interpreter will then try the reflected operation, or some other fallback,
# depending on the operator.) Its truth value is true.

# Ellipsis
# This type has a single value. There is a single object with this value. This object is accessed through the
# literal ... or the built-in name Ellipsis. Its truth value is true.
