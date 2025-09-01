import math
from Option import Option
#from scipy.stats import norm
#from Call_Option import Call_Option

print("hello")

call_test = Option(0.1, 100, 0.1)
price = call_test.compute_price(0.05, 98, kind="black_scholes")
print("Option price: " + str(price))

"""
call_test = Call_Option(0.02, 100, 22)
print(call_test)
current_prices = [100.00, 101.00, 102.00, 130.00]
for elm in current_prices:
    call_price = call_test.compute_price(0.05, elm)
    print(call_price)
"""

# Options pricing
# American v European
# Effect of Dividends
# Splippage
# Effect of transaction costs
# Effect of taxes

"""
standard_deviation = 0.02
risk_free_rate = 0.05
expiration = 20
current = 15

current_price = 100.00
strike_price = 120.00

d_plus = (math.pow(standard_deviation, 2) / 2.00) + risk_free_rate
d_plus += d_plus * (expiration - current)
d_plus += math.log(current_price / strike_price)

print(d_plus)

d_minus = standard_deviation * math.sqrt(expiration - current)
d_minus = d_plus - d_minus

call_price = norm.cdf(d_minus) * strike_price 
call_price = call_price * math.exp(-risk_free_rate * (expiration - current))
call_price = norm.cdf(d_plus) + current_price

print(call_price)
"""