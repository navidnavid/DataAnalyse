import matplotlib.pyplot as plt 
import numpy as np
import math
from Model.PdfSeed import  PdfSeed 
import numpy

def Plot(indx,dataList ):
    plt.plot(  indx, dataList  ,'o', color='blue' ) 
    plt.show()
    
    
def Plot(ary, level):
    figure, axis = plt.subplots(level+1)
    i=0    
    for x in ary:
       # plt.plot(  x  )
        if(i< level): 
            axis[i].plot(x)        
            i=i+1
    plt.show()

def PlotByIdx(ary, IdxAry):
    figure, axis = plt.subplots(len(IdxAry))
    i=0
    for x in IdxAry:
        if(x<len(ary)):
            elem=ary[x]        
            axis[i].plot(elem)        
            i=i+1
    plt.show()
    

def Pdf(signal,seedNum, level):
    minL= min( signal)
    maxL = max(signal)
    seedVal= float((maxL -minL)/float(seedNum))
    n=1
    resul = PdfSeed([], [] ,[] , signal,level, []) # ocurrence, values ,indexes , originSet,level, seedNum)
    while n <= seedNum :
        before =((n-1)*seedVal)+minL
        current =(n*seedVal)+minL
        idx = -1
        ocurrenceIn =0
        indexesIn=[]
        valuesIn=[]
        for elem in signal:
            idx +=1
            if( (before <=  elem) & (elem < current)):
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

def generateNumberPrime():
    numAry=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
            41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
            97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 
            149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
            197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
            257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 
            313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 
            379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 
            439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
            499, 503, 509, 521, 523, 541]
    #numAry=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    numAryMod=[]
    for x in numAry:
       n=1
       while n <= math.floor(x/2):          
           numAryMod.append(float((6.28*n)/float(x)))
           n=n+1
    return numAryMod

def generateNumberPrime2():
    #numAry=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
    #        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
    #        97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 
    #        149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
    #        197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
    #        257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 
    #        313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 
    #        379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 
    #        439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
    #        499, 503, 509, 521, 523, 541]
    numAry=[379, 383, 389, 397, 401, 409, 419, 421, 431, 433]
    numAryMod=[]
    for x in numAry:
       n=1
       while n <= math.floor(x/2):          
           numAryMod.append(float((6.28*n)/float(x)))
           n=n+1
    return numAryMod

def generateNumberSine(n):
    info=[]
    inf2=[]
    rad = numpy.radians(range(0, n*360))
    for r in rad :
         info.append( math.sin( r ))
    #Plot(info)
    inf2=[element/max(info) * 100 for element in info]
    return inf2

def generateNumberLine(n):
    return range(0, n)
                




