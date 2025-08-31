import math

class Option(object):

    def __init__(self, sd, strike, time_to_exp):
        self.sd = sd
        self.strike = strike
        self.variance = math.pow(self.sd, 2)
        self.time_to_exp = time_to_exp

    def compute_d_1(self, risk_free, current_stock_price):
        self.d1 = math.pow(self.variance, 2) / 2
        self.d1 += risk_free
        self.d1 *= self.time_to_exp
        self.d1 += math.log(current_stock_price / self.strike)
        self.d1 /= (self.sd * math.sqrt(self.time_to_exp))

    def compute_d_2(self, risk_free, current_stock_price):
        self.d2 = math.pow(self.variance, 2) / 2
        self.d2 = risk_free - self.d2
        self.d2 *= self.time_to_exp
        self.d2 += math.log(current_stock_price / self.strike)
        self.d1 /= (self.sd * math.sqrt(self.time_to_exp))

    # Getters
    def getSD(self): 
        return self.sd
    
    def getVar(self): 
        return self.variance
    
    def getStrike(self): 
        return self.strike
    
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