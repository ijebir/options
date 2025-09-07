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
        # extract 52-week range

    # Getters
    def get_sigma(self):
        return self.std_s
    
    def get_variance(self):
        return self.var_s
    
    def get_high_prices(self):
        return self.historical_data["High"]

    def get_low_prices(self):
        return self.historical_data["Low"]
    
    def get_dates(self):
        return self.historical_data["Date"]
    
    # Setter
    def add_point(self, date, value):
        pass

    def __str__(self):
        data_length = len(self.historical_data)
        str_ret = "============== STOCK OBJECT ================="
        str_ret += "\nTicker: " + str(self.ticker)
        str_ret += "\nDate range: " + str(self.historical_data.loc[0]["Date"]) + " to " + str(self.historical_data.loc[data_length-1]["Date"])
        str_ret += " (" + str(data_length) + " trading days)"
        str_ret += "\nStandard Deviation: " + str(self.get_sigma())
        str_ret += "\nVariance: " + str(self.get_variance())
        str_ret += "\n============ END OF STOCK OBJECT ============"
        return str_ret