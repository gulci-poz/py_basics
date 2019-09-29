import datetime


class Coupon:
    def __init__(self):
        self.isPizzaOrdered = False
        self.isBigDrinkOrdered = False
        self.isBurgerOrdered = False
        self.isNotWeekend = False

    def collect_the_order(self):
        self.isPizzaOrdered = True if input('Order pizza? y/n ') == 'y' else False
        self.isBigDrinkOrdered = True if input('Order big drink? y/n ') == 'y' else False
        self.isBurgerOrdered = True if input('Order burger? y/n ') == 'y' else False
        self.isNotWeekend = True if datetime.datetime.now().isoweekday() < 6 else False

    def set_the_order(self, is_pizza_ordered, is_big_drink_ordered, is_burger_ordered, is_not_weekend):
        self.isPizzaOrdered = is_pizza_ordered
        self.isBigDrinkOrdered = is_big_drink_ordered
        self.isBurgerOrdered = is_burger_ordered
        self.isNotWeekend = is_not_weekend

    def check_coupon_conditions(self):
        if (self.isPizzaOrdered or self.isBigDrinkOrdered) and self.isNotWeekend:
            return 'a coupon for burger'
        elif not (self.isPizzaOrdered or self.isBigDrinkOrdered) and not self.isNotWeekend:
            return 'you must order pizza or big drink, Monday to Friday'
        elif self.isNotWeekend:
            return 'you must order pizza or big drink to get a coupon for burger'
        else:
            return "on weekends we don't give coupons"
