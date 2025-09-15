import math
from Option import Option
from Stock import Stock
from Option_PnL import Option_PnL
import matplotlib.pyplot as plt

OPTIONS = [ "AAPL", ]

DEFAULT_RISK_FREE = 0.05
DEFAULT_TTE = 1.0
DEFAULT_OPTION_TYPE = "call"
DEFAULT_STOCK = "AAPL"
DEFAULT_STRIKE = 100.00

print("\nOption Pricing Tool\n")

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

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(df["final_stock_prices"], df["option_prices"])
axs[0, 0].set_title('Option Price with respect to Stock Price')
axs[0, 1].plot(df["final_stock_prices"], df["delta_values"], 'tab:orange')
axs[0, 1].set_title('Delta variation with respect to Stock Price')
axs[1, 0].plot(df["final_stock_prices"], df["vega_values"], 'tab:green')
axs[1, 0].set_title('Vega variation with respect to Stock Price')
axs[1, 1].plot(df["final_stock_prices"], df["gamma_values"], 'tab:red')
axs[1, 1].set_title('Gamma variation with respect to Stock Price')

plt.show()

#for ax in axs.flat:
#    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in axs.flat:
#    ax.label_outer()

print("\nProgram closing.")

# Options pricing
# American v European
# Effect of Dividends
# Splippage
# Effect of transaction costs
# Effect of taxes