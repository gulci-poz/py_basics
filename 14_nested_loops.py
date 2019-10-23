for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')

f_shape = [5, 2, 5, 2, 2]
l_shape = [2, 2, 2, 2, 5]

# for value in f_shape:
#     print('x' * value)

# for value in f_shape:
#     output = ''
#     for x in range(value):
#         output += 'x'
#     print(output)

for value in l_shape:
    for x in range(value):
        print('x', end='')
    print()
