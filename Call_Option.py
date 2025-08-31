from Option import Option
import math
from scipy.stats import norm

class Call_Option(Option):

    def __init__(self, sd, strike, time_to_exp):
        super().__init__(sd, strike, time_to_exp)
        self.pnl = []

    def compute_price(self, risk_free, current_stock_price):
        super().compute_d_1(risk_free, current_stock_price)
        super().compute_d_2(risk_free, current_stock_price)
        price = math.exp(-risk_free * self.time_to_exp)
        price *= norm.cdf(super().get_d_2())
        price *= -1.0 * super().getStrike()
        price += current_stock_price * norm.cdf(super().get_d_1())
        return price
    
    '''
    def compute_PnL(self, risk_free):
        # Create a list of prices (+-Stike)
        chart_price = 0.0
        while chart_price < (2 * super().getStrike()):
            price = self.compute_price(risk_free, chart_price)
            self.pnl.append(price)
            chart_price += 1.00
        return self.pnl
        '''