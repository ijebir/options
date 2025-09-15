# Options Pricing Tool in Python
This tool allows you to price call and put option using the black-scholes merton model for options pricing. The calculator proceeds then to calculate sensitivity metrics (greek) including deta, gamma, and vega using the stock last closing price as proxy for ST. Finally, charts are produced showing option price and greeks with respect to changing last prices within 3-sigma of last closing.

![alt tag](https://github.com/ijebir/options/blob/main/img/demo.png)

## Class Architecture

**Dependencies** pandas, matplotLib, numpy, and scipy

Classes were used to make this project useful for those implementing more complex Portfolio analysis tools in Python. The Stock class represents an abstraction for historical data, including therefore all abstraction based on data such as variance. On the other hand, the Option class focuses on the contractual nature of the deriviative, while Option_PnL focuses on evaluating the sentsitivity of the derivative (greeks) and the price of the option given a series of final stock prices with +/- 3 sigma.

## Optimizations
*(optional)*

You don't have to include this section but interviewers *love* that you can not only deliver a final product that looks great but also functions efficiently. Did you write something then refactor it later and the result was 5x faster than the original implementation? Did you cache your assets? Things that you write in this section are **GREAT** to bring up in interviews and you can use this section as reference when studying for technical interviews!

## Lessons Learned:

The Black-Scholes Merton (BSM) model represents a basic method for estimating an option's price, and more interesting volatility models could be interesting to incorporate into this tool.

## Possible Future Updates:
Below are some of the changes that could make this project highly useful for Risk programmers:

**Automated Historical data:** Using a direct data source instead of csv.

**Managing Option Type:** Differentiation between European and American options.

**Dividends:** Adding a system for incorporaing expected dividend payments

**More Greeks:** Adding calculations of both Rho and Theta