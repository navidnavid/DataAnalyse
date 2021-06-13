import matplotlib.pyplot as plt 
import numpy as np
import math
from Model.PdfSeed import  PdfSeed 

def Plot(indx,dataList ):
    plt.plot(  indx, dataList  ,'o', color='blue' ) 
    plt.show()
    
    
def Plot(ary):
    plt.plot(  ary ,'o', color='blue' ) 
    plt.show()
    

def Pdf(signal,seedNum, level):
    minL= min( signal)
    maxL = max(signal)
    seedVal= round((maxL -minL)/seedNum)
    n=1
    resul = PdfSeed([], [] ,[] , signal,level, []) # ocurrence, values ,indexes , originSet,level, seedNum)
    while n <= seedNum :
        before =((n-1)*seedVal)
        current =(n*seedVal)
        idx = -1
        ocurrenceIn =0
        indexesIn=[]
        valuesIn=[]
        for elem in signal:
            idx +=1
            if( before <=  elem & elem < current):
                ocurrenceIn = ocurrenceIn + 1
                indexesIn.append(idx)
                valuesIn.append(elem)
        #---
        resul.Ocurrence.append(ocurrenceIn)
        resul.Indexes.append(indexesIn)
        resul.Values.append(valuesIn)
        resul.SeedNum.append(n)        
        n+=1
    return resul

        
                




