class  prigma:
    def __init__ (self,wights,n1,n2):
        self.wights=wights
        self.nuro1= nuroin(n1)
        self.nuro2 = nuroin(n2)
        self.andgate= nuroin(-150)
        self.fitnees=0


    def calculatefittnes(self,bits,expected):

      nuro1result=self.nuro1.output(bits,[ a for (a,b) in self.wights])
      nuro2result = self.nuro2.output(bits,[ b for (a,b) in self.wights])
      result=self.andgate.output([nuro1result,nuro2result],[100,100])
      if result== expected:
          self.fitnees=self.fitnees+1

    def test (self,bits,expected):
        nuro1result = self.nuro1.output(bits, [a for (a, b) in self.wights])
        nuro2result = self.nuro2.output(bits, [b for (a, b) in self.wights])
        result = self.andgate.output([nuro1result, nuro2result], [100, 100])
        return (result == expected)


class nuroin:

    def __init__(self, bias):
        self.bias = bias

    def sigmoid(self, x):
        """Sigmoid function"""
        return (x > 0)

    # return (1.0 / (1.0 + np.exp(-x)))

    def output(self, inp, whights):
        w = 0
        j = 0
        for i in inp:
            w = w + i * whights[j]
            j = j + 1
        sig = (w + self.bias)
        return self.sigmoid(sig)


def main3():
    
    bestp=prigma([(-100, 100) for _ in range(16)],,)








if  __name__ == '__main__':
    main3()