has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print('eligible for loan')

a = True
b = 2
# b = 2 / 0

if a or b / 0 == 0:
    print('ok')

# or is evaluated lazily

# if b / 0 == 0 or True:
#     print('ok')

if has_good_credit and not has_criminal_record:
    print('ok')
else:
    print('not ok')
