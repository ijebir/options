import math

class Option(object):

    def __init__(self, sd, strike):
        self.sd = sd
        self.strike = strike
        self.variance = math.pow(self.sd, 2)

    # Getters
    def getSD(self): 
        return self.sd
    
    def getVar(self): 
        return self.variance
    
    def getStrike(self): 
        return self.strike
    
    # Setters
    def setSD(self, sd):
        self.sd = sd
        self.variance = math.pow(self.sd, 2)

    def setVar(self, var):
        self.variance = var
        self.sd = math.sqrt(self.variance)

    def setStrike(self, k):
        self.strike = k