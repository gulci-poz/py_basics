import unittest
from coupon_example.coupon_adv import Coupon


class CouponTest(unittest.TestCase):

    def test_coupon_check_no_weekend_no_condition(self):
        coupon = Coupon()
        self.assertEqual(coupon.check_coupon_conditions(), 'you must order pizza or big drink, Monday to Friday')

    def test_coupon_check_no_weekend_one_condition_ok(self):
        coupon = Coupon()
        coupon.set_the_order(True, False, False, False)
        self.assertEqual(coupon.check_coupon_conditions(), "on weekends we don't give coupons")

    def test_coupon_check_no_weekend_two_conditions_ok(self):
        coupon = Coupon()
        coupon.set_the_order(True, True, False, False)
        self.assertEqual(coupon.check_coupon_conditions(), "on weekends we don't give coupons")

    def test_coupon_check_weekend_no_condition(self):
        coupon = Coupon()
        coupon.set_the_order(False, False, False, True)
        self.assertEqual(coupon.check_coupon_conditions(),
                         'you must order pizza or big drink to get a coupon for burger')

    def test_coupon_check_weekend_one_condition_ok(self):
        coupon = Coupon()
        coupon.set_the_order(True, False, False, True)
        self.assertEqual(coupon.check_coupon_conditions(), 'a coupon for burger')

    def test_coupon_check_weekend_two_conditions_ok(self):
        coupon = Coupon()
        coupon.set_the_order(True, True, False, True)
        self.assertEqual(coupon.check_coupon_conditions(), 'a coupon for burger')
