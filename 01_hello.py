print("hello")
# evaluates expression first
print("*" * 10)

print(10 * 10)
print("10" * 10)
print(10 ** 2)

age = 35
print(type(age))
height = 1.9
print(type(height))
name = "john"
print(type(name))
married = True
print(type(married))

# always takes a string
# input and assignment vs input without assignment
# right side gets evaluated and assigned to left side
name = input("Enter your name: ")
# concatenation expression
# print("Hello, " + name + '!')
print("Hello, ", name, '!', sep="")
# default separator is space
print("uno", "dos", "tres")
