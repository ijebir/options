import math
from Option import Option
from Stock import Stock
from Option_PnL import Option_PnL
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import *

OPTIONS = [
    "Apple Inc. (AAPL)",
    "Microsoft Inc (MSFT)"
]

window = tk.Tk()

# set window resolution
window.geometry('1438x900')
window.title('Options Pricing Tool')

#label = tk.Frame(window, bg='wheat')  # Bg to show label size on window
#label.pack(padx=100, pady=30)
tk.Label(window, text="Step 1: Set Parameters", font=("Helvetica", 20, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

tk.Label(window, text="Select Stock:",).grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)
gender = ttk.Combobox(window, values=OPTIONS, state="readonly")
gender.grid(row=1, column=2, padx=5, pady=5)

tk.Label(window, text="Risk Free Rate:",).grid(row=1, column=3, padx=5, pady=5, sticky=tk.E)
default_risk_free = StringVar(window, value='5.00%')
name = ttk.Entry(window, textvariable=default_risk_free)
name.grid(row=1, column=4, padx=5, pady=5, ipadx=5)

tk.Label(window, text="Option Type:",).grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)
optionTypeView = ttk.Combobox(window, values=["Call", "Put"], state="readonly")
optionTypeView.grid(row=2, column=2, padx=5, pady=5)

tk.Label(window, text="Time to expiration:",).grid(row=2, column=3, padx=5, pady=5, sticky=tk.E)
default_exp = StringVar(window, value='1.00')
tte = ttk.Entry(window, textvariable=default_exp)
tte.grid(row=2, column=4, padx=5, pady=5, ipadx=5)

submit = ttk.Button(window, text="Calculate")
submit.grid(row=3, column=4, padx=5, pady=5, sticky=tk.E)

tk.Label(window, text="Step 2: Stock Data Calc", font=("Helvetica", 20, "bold")).grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="Standard Deviation:",).grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=5, column=2, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="Variance:",).grid(row=6, column=1, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=6, column=2, padx=5, pady=5, sticky=tk.E)
#image_1 = tk.PhotoImage(file="./img/file_example_PNG_500kB.png").subsample(3, 3)
#tk.Label(window, image=image_1, relief=tk.RAISED).grid(row=5, column=0, rowspan=5, padx=10, pady=10)


tk.Label(window, text="Step 3: Pricing Option", font=("Helvetica", 20, "bold")).grid(row=7, column=0, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="Option Price:",).grid(row=8, column=1, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=8, column=2, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="d_1:",).grid(row=9, column=1, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=9, column=2, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="d_2:",).grid(row=10, column=1, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=10, column=2, padx=5, pady=5, sticky=tk.E)

tk.Label(window, text="Delta:",).grid(row=8, column=3, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=8, column=4, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="Vega:",).grid(row=9, column=3, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=9, column=4, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="Gamma:",).grid(row=10, column=3, padx=5, pady=5, sticky=tk.E)
tk.Label(window, text="2.4%",).grid(row=10, column=4, padx=5, pady=5, sticky=tk.E)
#tk.Label(window, text="d_1:",).grid(row=11, column=3, padx=5, pady=5, sticky=tk.E)
#tk.Label(window, text="2.4%",).grid(row=11, column=4, padx=5, pady=5, sticky=tk.E)
#tk.Label(window, text="d_2:",).grid(row=12, column=3, padx=5, pady=5, sticky=tk.E)
#tk.Label(window, text="2.4%",).grid(row=12, column=4, padx=5, pady=5, sticky=tk.E)
#tk.Label(window, text="d_2:",).grid(row=13, column=3, padx=5, pady=5, sticky=tk.E)
#tk.Label(window, text="2.4%",).grid(row=13, column=4, padx=5, pady=5, sticky=tk.E)

image_1 = tk.PhotoImage(file="./img/file_example_PNG_500kB.png").subsample(3, 3)
tk.Label(window, image=image_1, relief=tk.RAISED).grid(row=8, column=5, rowspan=5, padx=10, pady=10)

tk.Label(window, text="Step 4: Charting Sensitivies", font=("Helvetica", 20, "bold")).grid(row=11, column=0, padx=5, pady=5, sticky=tk.E)
image_2 = tk.PhotoImage(file="./img/file_example_PNG_500kB.png").subsample(3, 3)
tk.Label(window, image=image_2, relief=tk.RAISED).grid(row=12, column=1, rowspan=5, padx=10, pady=10)

#image_1 = tk.PhotoImage(file="./img/file_example_PNG_500kB.png").subsample(2, 2)
#image_2 = tk.PhotoImage(file="./img/file_example_PNG_500kB.png").subsample(2, 2)
#tk.Label(window, image=image_1, relief=tk.RAISED).grid(row=0, column=3, rowspan=5, padx=10, pady=10)
#tk.Label(window, image=image_1, relief=tk.RAISED).grid(row=8, column=3, rowspan=5, padx=10, pady=10)

#tk.Label(window, text="Risk Free Rate:",).grid(row=0, column=3, padx=5, pady=5, sticky=tk.E)
#name = ttk.Entry(window)
#name.grid(row=1, column=3, padx=5, pady=5, ipadx=5)

# Gender field




window.mainloop()

"""
pw = ttk.PanedWindow(orient=tk.HORIZONTAL)
left_list = tk.Listbox(window)
left_list.pack(side=tk.LEFT)
pw.add(left_list)
right_list = tk.Listbox(window)
right_list.pack(side=tk.LEFT)
pw.add(right_list)

stock_drop_down_label = tk.Label(text="Select stock")
stock_drop_down_label.pack()
left_list.insert(0, stock_drop_down_label)

pw.pack(fill=tk.BOTH, expand=True)

# Add select stock from dropdown
#stock_drop_down_label = tk.Label(text="Select stock")
#stock_drop_down_label.pack()
stock_drop_down = StringVar(window)
stock_drop_down.set(OPTIONS[0])
w = OptionMenu(window, stock_drop_down, *OPTIONS)
w.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

window.mainloop()
"""




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