import math
from Option import Option
from Stock import Stock
from Option_PnL import Option_PnL
import numpy as np
import matplotlib.pyplot as plt

OPTIONS = [
    "Apple Inc. (AAPL)",
    "Microsoft Inc (MSFT)"
]

DEFAULT_RISK_FREE = 0.05
DEFAULT_TTE = 1.0
DEFAULT_OPTION_TYPE = "call"
DEFAULT_STOCK = "AAPL"
DEFAULT_STRIKE = 100.00

print("\nOption Pricing Tool\n")

#print("|       Default paramters            |")
#print("| ================================== |")
#print("| Option Type    | " + str(DEFAULT_OPTION_TYPE))
#print(" ----------------------------------")
#print("| Risk Free Rate | " + str(DEFAULT_RISK_FREE))
#print(" ----------------------------------")
#print("| Expiration     | " + str(DEFAULT_TTE))
#print(" ----------------------------------")
#print("| Ticker         | " + str(DEFAULT_STOCK))
#print(" ==================================")

# Run the calculations
aapl = Stock("AAPL")
pretty_sd = (aapl.get_sigma() * 100.00)
pretty_var = (aapl.get_variance() * 100.00)
option = Option(aapl, DEFAULT_STRIKE, DEFAULT_TTE, type=DEFAULT_OPTION_TYPE)
d_1 = option.compute_d_1(DEFAULT_RISK_FREE, aapl.get_close_prices()[0])
d_2 = option.compute_d_2(DEFAULT_RISK_FREE, aapl.get_close_prices()[0])
option_price = option.compute_price(DEFAULT_RISK_FREE, aapl.get_close_prices()[0])
delta = Option.compute_delta(option)
vega = Option.compute_vega(option, aapl.get_close_prices()[0])
gamma = Option.compute_gamma(option, aapl.get_close_prices()[0])
option_pnl = Option_PnL(option, DEFAULT_RISK_FREE)
df = option_pnl.get_data_frame()

print("Underlying Ticker: \033[1m" + str(DEFAULT_STOCK) + "\033[0m     |", "Standard Deviation: \033[1m%.2f%%\033[0m  |" % pretty_sd, "Option price: \033[1m%.4f\033[0m" % option_price)
print("Option type: \033[1m" + str(DEFAULT_OPTION_TYPE) + "\033[0m           |", "Variance: \033[1m%.2f%%\033[0m            |" % pretty_var, "Delta: \033[1m%.4f\033[0m" % delta)
print("Expiration: \033[1m" + str(DEFAULT_TTE) + "\033[0m             |", "d_1: \033[1m%.4f\033[0m               |" % d_1, "Vega: \033[1m%.4f\033[0m" % vega)
print("Risk Free Rate: \033[1m" + str(DEFAULT_RISK_FREE) + "\033[0m        |", "d_2: \033[1m%.4f\033[0m               |" % d_2, "Gamma: \033[1m%.4f\033[0m" % gamma)

fig, ax = plt.subplots()
ax.plot(df["final_stock_prices"], df["option_prices"])
ax.set(xlabel='Stock Price', ylabel='Option Price',
       title='Option Price with respect to Price')
ax.grid()
plt.show()

print("\nProgram closing.")

"""
risk_free = 0.05

aapl = Stock("AAPL")
strike = 100.00
time_to_exp = 1.0
print(aapl)

aapl_call = Option(aapl, strike, time_to_exp)
print(aapl_call)

aapl_call_PnL = Option_PnL(aapl_call, risk_free)

#final_prices = aapl_call.gen_ST_prices()
#print(final_prices)

"""

"""
# playing around with GUI
r = tk.Tk()
r.title('Options Pricing Tool')
#w = r.Label(r, text='Hello World!')
button = tk.Button(r, text='Calulate', width=25, command=r.destroy)
button.pack()
#w.pack()
r.mainloop()
"""

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

fig, ax = plt.subplots()
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