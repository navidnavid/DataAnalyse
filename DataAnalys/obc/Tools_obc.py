import matplotlib.pyplot as plt 
import numpy as np
import math


class ToolPlot:
    dataList = []
    indx = []
    char = ''

    def __init__(self,indx , dataList ):
        self.dataList = dataList
        self.indx = indx
        
    def Plot(self):
        plt.plot(  self.indx, self.dataList  ,'o', color='blue' ) 
        plt.show()
    
    @staticmethod
    def PlotEasy(ary):
        plt.plot(  ary ,'o', color='blue' ) 
        plt.show()
    
  


class ToolPdf:
    results= []
    info=[]
    numberOfLevel = 0
    factor = 1
    def __init__(self, numberOfLevel, info, factor):
        self.numberOfLevel =numberOfLevel
        self.info = info
        self.factor = factor

    def Pdf(self):
        ocurrence = []
        resRemoveSames = []
        Values =[]
        Indexes=[]
        indxs= 0
        MaxInfo = max(self.info)*self.factor
        MinInfo = min(self.info)*self.factor
        diff = (MaxInfo -MinInfo )/self.numberOfLevel
        diffFactors= [round(x*self.factor/diff )for x in self.info]                
        [resRemoveSames.append(x) for x in diffFactors if x not in resRemoveSames]
        seedNum = []
        seend=0
        for val in resRemoveSames:
            indxs = [i for i, x in enumerate(diffFactors) if x == val]
            ocurrence.append(len(indxs))
            Values.append(diff*val/self.factor)
            Indexes.append(indxs)
            seed=seed +1
            seedNum.append(seed)
        return (ocurrence, Values ,Indexes,seedNum)
       


    # [resRemoveSames.append(x) for x in results if x not in resRemoveSames]
    #[i for i, x in enumerate(results) if x == val]

class makeNormal:
    @staticmethod
    def normalizePi( ary):
        normalToPi = 0
        Min = min(ary)
        Max= max(ary)
        return [(x/abs(Max ))*math.pi for x in ary]
    @staticmethod
    def normalizeToOne( ary):
        normalToPi = 0
        Min = min(ary)
        Max= max(ary)
        return [(x/abs(Max) ) for x in ary]

class Energy:
    @staticmethod
    def RelEnergyByDistance(ary):
        res=0
        Min = min(ary)
        Max = max(ary)
        antiScaling =(Max-Min)*(Max-Min)
        for y in ary:
            res = res+sum([(y-x)*(y-x) for x in ary]) 
        return ((res/antiScaling))
    # TODO calcule the enthopy too

    

def FindMaxEnergy(dataList ):
        maxEnergy = 0 
        SelectednumberOfLevel = 0 
        factor = 100
        ocurrenceOut =[]
        ValuesOut =[]
        idxesOut =[]
        for  numberOfLevel in range(len(dataList)):
            pdf = ToolPdf(numberOfLevel ,dataList , factor)
            ( ocurrence, Values, idxes) = pdf.Pdf()
            energy= Energy.RelEnergyByDistance(ocurrence)
            if energy > maxEnergy:
                maxEnergy = energy
                SelectednumberOfLevel = numberOfLevel;
                ocurrenceOut = ocurrence
                ValuesOut = Values
                idxesOut = idxes
        return (SelectednumberOfLevelm , maxEnergy,ocurrenceOut, ValuesOut, idxesOut)