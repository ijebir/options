import pandas as pd

class Stock(object):

    def __init__(self, ticker):
        self.ticker = ticker
        self.historical_data = pd.read_csv("./data/" + str(ticker) + ".csv")
        # no need to reverse order, data is already ordered by dt DESC
        # Compute daily returns as (new / old) - 1
        self.historical_data["Return"] = (self.historical_data["Close"] / self.historical_data["Close"].shift(-1)) - 1.0
        # extract standard deviation and variance
        self.std_s = self.historical_data["Return"].std()
        self.var_s = self.std_s ** 2

    # Getters
    def get_sigma(self):
        return self.std_s
    
    def get_variance(self):
        return self.var_s
    
    # Setter
    def add_point(self, date, value):
        pass

    def __str__(self):
        return "Stock: " + str(self.ticker) + " ("