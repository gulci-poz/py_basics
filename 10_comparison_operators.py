temperature = 30

# == != >= <= < >
# expression must produce boolean value
if temperature > 30:
    print('hot day')
else:
    print('not a hot day')

name = "bobo"
name_len = len(name)

if name_len < 3:
    print('too short')
elif name_len > 50:
    print('too long')
else:
    print('name ok')
