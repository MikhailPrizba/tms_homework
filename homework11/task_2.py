class Temperature:
    
   
    F = 32
    K = 273.15
    C = 0

    def inCelsius(self, C):
        self.C = C
        self.K = C + Temperature.K
        self.F = C * (9 / 5) + Temperature.F

    def inKelvin(self, K):
        self.K = K
        self.C = K - Temperature.K
        self.F = (K - Temperature.K) * (9 / 5) + Temperature.F

    def inFahrenhei(self, F):
        self.F = F
        self.C = (F - Temperature.F) * (5 / 9)
        self.K = (F - Temperature.F) * (5 / 9) + Temperature.K


t1 = Temperature()
t1.inCelsius(20)
print(t1.K)
print(t1.F)