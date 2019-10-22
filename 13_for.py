# string - sequence of characters

for letter in 'Python':
    print(letter, end='*')

print()

for name in ['Wiki', 'Mela', 'Ema']:
    print(name, end=' ')

print()

sum_of_prices = 0
prices = [1, 2, 3, 4, 5]
for prices in prices:
    sum_of_prices += prices

print('Sum of prices:', sum_of_prices)

sum_of_numbers = 0

# from zero, range(excluded)
for number in range(11):
    sum_of_numbers += number

print('Sum:', sum_of_numbers)

# range(included, excluded)
for number in range(5, 11):
    print(number, end=' ')

print()

# step
for number in range(5, 11, 2):
    print(number, end=' ')

print()
