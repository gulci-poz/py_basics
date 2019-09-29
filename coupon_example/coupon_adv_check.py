from coupon_example.coupon_adv import Coupon

coupon = Coupon()
print(coupon.check_coupon_conditions())
coupon.collect_the_order()
print(coupon.check_coupon_conditions())
