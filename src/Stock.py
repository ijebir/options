import pandas as pd

class Stock(object):

    def __init__(self, ticker):
        self.ticker = ticker
        # Should the historical data be set as numpy array or as pandas dataFrame
        # We know that pricing is associated with dates, and we are interested in only close or adj. close
        # We need to reference the last date for sure, but we need 251 trading days back

    # Getters
    def get_sigma():
        return self.sigma
    
    def get_variance():
        return self.variance
    
    # Setter
    def add_point(self, date, value):
        pass

    def __str__(self):
        return "Stock: " + str(self.ticker)