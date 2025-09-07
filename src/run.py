import math
from Option import Option
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from scipy.stats import norm
#from Call_Option import Call_Option

print("hello")

df = pd.read_csv("./data/AAPL.csv")
# no need to reverse order, data is already ordered by dt DESC
# Compute daily returns as (new / old) - 1
df["Return"] = (df["Close"] / df["Close"].shift(-1)) - 1.0
# extract standard deviation and variance
std_s = df["Return"].std()
var_s = std_s * std_s
print(df)
print("Standard deviation of returns: " + str(std_s))
print("Variance: " + str(var_s))

"""
# Generate a list of pices from 0.0 to 150.00
final_price = np.arange(0.1, 20.00, 0.1)
print(final_price[0])
print(final_price[1])
print(final_price[2])

current_price = 100.00
strike_price = 100.00
# Time to maturity (time to expiration) is expressed in *years*
T = 1
# Proxy for buying 
risk_free = 0.05
# Standard Deviation of Historical Daily Returns
sigma = 0.2

option_prices = []

call_test = Option(sigma, strike_price, T)
#price = call_test.compute_price(risk_free, current_price, kind="black_scholes")
#print("Option price: " + str(price))
for item in final_price:
    option_price = call_test.compute_price(risk_free, item, kind="black_scholes")
    option_prices.append(option_price)
    print("For stock price " + str(item) + ", Call is: " + str(option_price))

ax = plt.subplots()
ax.plot(final_price, option_prices)
ax.set(xlabel='Stock Price', ylabel='Option Price',
       title='Option Price with respect to Price')
ax.grid()
plt.show()

"""

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