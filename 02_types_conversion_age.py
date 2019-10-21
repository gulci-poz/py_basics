import datetime

birth_year = input("Birth year: ")
# error
# age = 2019 - birth_year
# 2019 - '1984'
# other functions for type conversion: float(), bool() and str()
# age = 2019 - int(birth_year)
age = datetime.datetime.now().year - int(birth_year)
print(age)
print(type(birth_year))
print(type(int(birth_year)))
