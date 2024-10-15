# Andrew Hollands
# October 15 2024
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first 
# and last element of that pair. For example, car(cons(3, 4)) returns 3, and 
# cdr(cons(3, 4)) returns 4.
#

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

# As a nested function, cons returns the function "pair".
# pair has access to both a and b because these variables are in the scope of the
# function.
# we can access these variables through the __closure__ private variable.

def car( function ):
    return function.__closure__[0].cell_contents

def cdr( function ):
    return function.__closure__[1].cell_contents

print( car(cons(3, 4)) )
print( cdr(cons(3, 4)) )
