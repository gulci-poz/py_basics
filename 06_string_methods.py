course = 'Advanced Python'
print(len(course))
# len is a general purpose function, we can count elements in a list
print(len(course.split()))
# functions on string objects - methods
# string value is not modified, operation is performed on a copy
# we can assign it to other variable
print(course.upper())
print(course.lower())
# index of the first appearance, case sensitive
print(course.find('P'))
# index of the first appearance of the beginning (its first letter)
print(course.find('Python'))
# -1 if not found
print(course.find('J'))
# case sensitive
print(course.replace('Advanced', 'Basic'))
# returns boolean
print('Python' in course)
# title case - words start with capital letter
print('advanced python'.title())

msg = 'bla bla'
# each appearance is replaced
print(msg.replace('b', 'a'))
print('s' in msg)
