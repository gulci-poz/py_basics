course = 'Advanced Python'
print(len(course))
print(course.upper())
print(course.lower())
# index of first appearance, case sensitive
print(course.find('P'))
# index of beginning
print(course.find('Python'))
# case sensitive
print(course.replace('Advanced', 'Basic'))
print('Python' in course)
print(course.title())

msg = 'bla bla'
# each appearance is replaced
print(msg.replace('b', 'a'))
print('s' in msg)
# 48:40
