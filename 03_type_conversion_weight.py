weight = float(input('Weight: '))
unit_choice = input('(L)bs or (K)gs: ')
weight_result = 0

if unit_choice.lower() == 'k':
    weight_result = weight * 2.20462
    print(f'Your weight in lbs is {weight_result}')
elif unit_choice.lower() == 'l':
    weight_result = weight * 0.45359237
    print(f'Your weight in kgs is {weight_result}')
else:
    print('Choose (l) for lbs or (k) for kgs.')
