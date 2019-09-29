import datetime

isPizzaOrdered = True if input('Order pizza? y/n ') == 'y' else False
isBigDrinkOrdered = True if input('Order big drink? y/n ') == 'y' else False
isBurgerOrdered = True if input('Order burger? y/n ') == 'y' else False
isNotWeekend = True if datetime.datetime.now().isoweekday() < 6 else False
# isNotWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and isNotWeekend:
    print('a coupon for burger')
elif not (isPizzaOrdered or isBigDrinkOrdered) and not isNotWeekend:
    print('you must order pizza or big drink, Monday to Friday')
elif isNotWeekend:
    print('you must order pizza or big drink to get a coupon for burger')
else:
    print("on weekends we don't give coupons")
