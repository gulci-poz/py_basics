import math

import xx_module_main

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
# augmented assignment operators - for all operators above
x += 3
print(x)

# operator precedence - order of operations
# ()
# **
# * / // %
# + -

print(round(2.5))
print(round(2.6))
print(abs(2))
print(abs(-2))

# module - different python file, a code library
# may have a different behaviour when run as main file comparing to being imported
xx_module_main.hello_from_module()

print(math.ceil(2.9))
print(math.floor(2.9))
