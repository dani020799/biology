import sys
import numpy as np
import random


lines1=[]
lines2=[]

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




class nuroin :

     def __init__(self, bias ):
        self.bias=bias


     def  sigmoid(self,x):
        """Sigmoid function"""
        return (x>0)
       # return (1.0 / (1.0 + np.exp(-x)))

     def output (self,inp,whights):
         w=0
         j=0
         for i in inp:

             w=w+ i*whights[j]
             j=j+1
         sig=( w + self.bias)
         return self.sigmoid(sig)





def read_files(file1, file2):
    global  lines1, lines2

    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = [line.rstrip() for line in f1]
            lines2 = [line.rstrip() for line in f2]
            #print(f"Contents of {file1}:")
           # print(lines1)
           # print(f"\nContents of {file2}:")
           # print(lines2)

    except FileNotFoundError:
        print("One or both files could not be found.")
    except IOError:
        print("An error occurred while reading the files.")





def main1():
    global lines1, lines2
    if len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        read_files(file1, file2)
    else:
        print("Please provide two file names as command-line arguments.")

    trainlines=[ ]
    testlines=[]
    for l in lines1:
        splitt= l.split("   ")
        bits=[int(bit) for bit in splitt[0]]
        expected=int(splitt[1])
        trainlines.append((bits,expected))
    for l in lines2:
        splitt = l.split("   ")
        bits = [int(bit) for bit in splitt[0]]
        expected = int(splitt[1])
        testlines.append((bits, expected))
    population=[]
    random.seed(a=None, version=2)
    for i in range(10):
        r=  random.randint(0,16)*100 +50
        r1 = random.randint(-16, 0)*100 -50
      #  p= prigma([(float (1/r), float (1/r1)) for _ in range(16)],random.randint(0, 16),random.randint(0, 16))
        p = prigma([(-100, 100) for _ in range(16)], r, r1)
        population.append(p)

    bestfittnes=population[0].fitnees
    bestp = population[0]
    generation=1
    bestlist=[]
    avglist=[]
    lineslen= len(trainlines)
    while (bestfittnes<lineslen*0.98):
        avg=0
        for l in trainlines:
            (a,b) =l
            for index in range(len(population)):
             myp=population[index]
             myp.calculatefittnes(a,b)
             avg=avg+myp.fitnees
             if bestfittnes < myp.fitnees:
                bestfittnes=myp.fitnees
                bestp=myp
        avg=float(avg/10)
        population=sorted(population, key=lambda p: p.fitnees)
        bestlist.append((generation,bestfittnes))
        avglist.append((generation,avg))

        newpopulation=[]
        newpopulation.append(population[0])

        while len(newpopulation) <10:
            if  len(newpopulation)<5:
                r=random.randint(0,9)
                r1 = random.randint(0, 9)
                p1=population[r]
                p2 = population[r1]

               # newwights=[]
              #  for (a1,b1) in p1.wights:
                   # (a2,b2) =p2.wights
                   # neww= (((a1+a2)/2),((b1+b2)/2))
                   # newwights.append(neww)
                newn1= int((p1.nuro1.bias + p2.nuro1.bias)/2)
                newn2 = int((p1.nuro2.bias + p2.nuro2.bias) / 2)
                newp= prigma([(-100, 100) for _ in range(16)],newn1,newn2)
                newpopulation.append(newp)
            else:
                r = random.randint(0, 16) * 100 + 50
                r1 = random.randint(-16, 0) * 100 - 50
                newp = prigma([(-100, 100) for _ in range(16)], r, r1)
                newpopulation.append(newp)



        population= newpopulation
        generation =generation +1
        print ("best fit: " +str(bestfittnes)+ "\n")
        print(bestp.nuro1.bias)
        print(bestp.nuro2.bias)
    counter=0
    for l in testlines:
            (a, b) = l

            if bestp.test(a,b):
                counter=counter+1

    print (float(counter/len(testlines)))
    with open('wnet1.txt', 'w') as file:
        file.writelines(str(-100) + '\n' + str(100) + "\n")
        file.writelines(str(bestp.nuro1.bias) + "\n" + str(bestp.nuro2.bias))



if  __name__ == '__main__':
    main1()
