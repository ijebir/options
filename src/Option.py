import math
from scipy.stats import norm

class Option(object):

    """
    def __init__(self, sd, strike, time_to_exp, type="call"):
        self.type = type
        self.sd = sd
        self.strike = strike
        self.variance = math.pow(self.sd, 2)
        self.time_to_exp = time_to_exp
    """

    def __init__(self, stock, strike, time_to_exp, type="call"):
        self.type = type
        self.time_to_exp = time_to_exp
        self.strike = strike
        self.sd = stock.get_sigma()
        self.variance = stock.get_variance()

    def compute_d_1(self, risk_free, current_stock_price):
        self.d1 = self.variance / 2
        self.d1 += risk_free
        self.d1 *= self.time_to_exp
        self.d1 += math.log(current_stock_price / self.strike)
        self.d1 /= (self.sd * math.sqrt(self.time_to_exp))

    def compute_d_2(self, risk_free, current_stock_price):
        self.d2 = self.variance / 2
        self.d2 = risk_free - self.d2
        self.d2 *= self.time_to_exp
        self.d2 += math.log(current_stock_price / self.strike)
        self.d2 /= (self.sd * math.sqrt(self.time_to_exp))

    # Getters
    def getSD(self): 
        return self.sd
    
    def getVar(self): 
        return self.variance
    
    def getStrike(self): 
        return self.strike
    
    def get_time_to_exp(self):
        return self.time_to_exp
    
    def get_d_1(self):
        return self.d1
    
    def get_d_2(self):
        return self.d2
    
    # Setters
    def setSD(self, sd):
        self.sd = sd
        self.variance = math.pow(self.sd, 2)

    def setVar(self, var):
        self.variance = var
        self.sd = math.sqrt(self.variance)

    def setStrike(self, k):
        self.strike = k

    def __str__(self):
        ret_str = "Option with:\n"
        ret_str += "\tStrike: " + str(self.strike) + "\n"
        ret_str += "\tStandard Deviation: " + str(self.sd) + "\n"
        ret_str += "\tVariance: " + str(self.variance) + "\n"
        return ret_str
        #return "Option with strike: " + str(self.strike) + ", sd: " + str(self.sd)

    def compute_price(self, risk_free, current_stock_price, kind="black_scholes"):
        if kind == "black_scholes":
            self.compute_d_1(risk_free, current_stock_price)
            self.compute_d_2(risk_free, current_stock_price)
            if self.type == "call":
                price = math.exp(-risk_free * self.time_to_exp)
                price *= norm.cdf(self.get_d_2())
                price *= -1.0 * self.getStrike()
                price += current_stock_price * norm.cdf(self.get_d_1())
                return price
            else:
                raise ValueError("Unkown option type: " + str(self.type))
        else:
            raise ValueError("Unknown kind: " + str(kind))
        
    @staticmethod
    def compute_delta(option):
        if option.type == "call":
            return norm.cdf(option.get_d_1())

    @staticmethod
    def compute_vega(option, current_price):
        if option.type == "call":
            vega = math.pow(option.get_d_1(), 2) / 2.0
            vega = math.exp(-1.0 * vega)
            vega *= math.sqrt(option.get_time_to_exp())
            vega *= math.sqrt(current_price)
            vega = vega / math.sqrt(2.0 * math.pi)
            return vega
        
    @staticmethod
    def compute_gamma(option, current_price):
        gamma = math.sqrt(option.get_time_to_exp())
        gamma *= option.getSD() * current_price
        gamma *= math.sqrt(2.0 * math.pi)
        gamma = 1.0 / gamma
        gamma *= math.exp(-1.0 * ( math.pow(option.get_d_1(), 2.0) / 2.0 ) )
        return gamma