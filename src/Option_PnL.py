import numpy as np
import pandas as pd
from Option import Option

class Option_PnL(object):

    def __init__(self, option, risk_free):
        self.option = option
        # Generate final stock price list
        max_price_up = option.getStrike() * (1.0 + (3.0 * option.getSD()))
        step_up = (max_price_up - option.getStrike()) / 100.00
        up_prices = np.arange(option.getStrike(), max_price_up, step_up)
        low_price_down = option.getStrike() * (1.0 - (3.0 * option.getSD()))
        step_down = (option.getStrike() - low_price_down) / 100.00
        low_prices = np.arange(low_price_down, option.getStrike(), step_down)
        all_prices = np.concatenate([low_prices, up_prices])
        self.df = pd.DataFrame({ "final_stock_prices": all_prices })
        #print(self.df)
        # Compute options prices on the basis of prices
        self.compute_option_prices(risk_free)

    def get_data_frame(self):
        return self.df

    def compute_option_prices(self, risk_free):
        option_prices = np.zeros(shape=(len(self.df["final_stock_prices"])))
        delta_values = np.zeros(shape=(len(self.df["final_stock_prices"])))
        vega_values = np.zeros(shape=(len(self.df["final_stock_prices"])))
        gamma_values = np.zeros(shape=(len(self.df["final_stock_prices"])))
        for idx, *row in self.df.itertuples():
            final_stock_p = row[0]
            op_price = self.option.compute_price(risk_free, final_stock_p)
            delta_val = Option.compute_delta(self.option)
            vega_val = Option.compute_vega(self.option, final_stock_p)
            gamma_val = Option.compute_gamma(self.option, final_stock_p)
            option_prices[idx] = op_price
            delta_values[idx] = delta_val
            vega_values[idx] = vega_val
            gamma_values[idx] = gamma_val
        self.df["option_prices"] = option_prices
        self.df["delta_values"] = delta_values
        self.df["vega_values"] = vega_values
        self.df["gamma_values"] = gamma_values
        print(self.df)
