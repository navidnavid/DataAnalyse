from Tools.Plot import * 
import math 
import numpy

def PlotMulti(pL):
        for p in pL:
            Plot(p)

def main():

    info=[]
    rad = numpy.radians(range(0, 360))
    for r in rad :
         info.append( math.sin( r ))
    #Plot(info)
    infoNrml= [element/max(info) * 100 for element in info]
    
    dataAry=[]
    dataAry.append(infoNrml)
    responseAry=[]
    x=0
    pdfSeedList = []
    while x<2 :
        for  infoNrml in dataAry:
            l=len(infoNrml)
            l=len(dataAry)
            pdfResult = Pdf(infoNrml,2,x)
            for ary in  pdfResult.Values  :
                responseAry.append(ary)                           
            pdfSeedList.append(pdfResult)
        dataAry=responseAry
        PlotMulti(responseAry)
        responseAry=[]
        x =x+1
    

    

if __name__ == "__main__":
    main()


