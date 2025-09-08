import math
from Option import Option
from Stock import Stock
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# playing around with GUI
r = tk.Tk()
r.title('Options Pricing Tool')
#w = r.Label(r, text='Hello World!')
button = tk.Button(r, text='Calulate', width=25, command=r.destroy)
button.pack()
#w.pack()
r.mainloop()

#from scipy.stats import norm
#from Call_Option import Call_Option

# Consider making the Option a subclass of Stock

"""
print("hello")

aapl = Stock("AAPL")
print(aapl)
dates = aapl.get_dates()
high_prices = aapl.get_high_prices()
low_prices = aapl.get_low_prices()
# reverse data order to obtain times series ASC
dates = dates.iloc[::-1]
high_prices = high_prices.iloc[::-1]
low_prices = low_prices.iloc[::-1]
print(type(dates))
#print(high_prices)
#print(low_prices)

fig, ax = plt.subplots()
ax.plot(dates, high_prices)
#fig.yscale('log')
ax.plot(dates, low_prices)
ax.set(
    xlabel='Date', 
    ylabel='Stock High',
    title='Historical Stock Price'
)
# Only show 12 ticks on the x-axis
ax.xaxis.set_major_locator(plt.MaxNLocator(12))
# Add filler between high and low
ax.fill_between(
    dates,
    high_prices,
    low_prices,
    color="#929292",
)

ax.grid()
plt.show()
"""

"""
axes.plot(
    data.index,
    data["mean"],
    color="black",
    zorder=10,
)
"""

#print(df)
#print("Standard deviation of returns: " + str(std_s))
#print("Variance: " + str(var_s))

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

fx, ax = plt.subplots()
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