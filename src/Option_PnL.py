import numpy as np
import pandas as pd

class Option_PnL(object):

    def __init__(self, option):
        # Generate final stock price list
        max_price_up = option.getStrike() * (1.0 + (3.0 * option.getSD()))
        step_up = (max_price_up - option.getStrike()) / 100.00
        up_prices = np.arange(option.getStrike(), max_price_up, step_up)
        low_price_down = option.getStrike() * (1.0 - (3.0 * option.getSD()))
        step_down = (option.getStrike() - low_price_down) / 100.00
        low_prices = np.arange(low_price_down, option.getStrike(), step_down)
        self.df = pd.DataFrame({"final_stock_prices": np.concatenate([low_prices, up_prices])})
        print(self.df)
        # Compute options prices on the basis of prices
        self.compute_option_prices()
        # Compute options greeks on the basis of prices
        self.compute_option_greeks()
        # Generate charts on the basis of prices

    def compute_option_prices(self):
        pass

    def compute_option_greeks(self):
        pass