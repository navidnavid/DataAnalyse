from Tools.Plot import * 
import math 
import numpy

#def PlotMulti(pL):
#        for p in pL:
#            Plot(p)

def main():

    info=[]
    rad = numpy.radians(range(0, 360))
    for r in rad :
         info.append( math.sin( r ))
    #Plot(info)
    infoNrml= [element/max(info) * 100 for element in info]
    infoNrml= range(0, 20)
    #------------
    infoNrml= generateNumber()

    #------------
    dataAry=[]
    dataAry.append(infoNrml)
    responseAry=[]
    PrbOccurence=[]
    x=0
    pdfSeedList = []
    while x<10 :
        for  infoNrml in dataAry:
            l=len(infoNrml)
            l=len(dataAry)
            pdfResult = Pdf(infoNrml,2,x)
            PrbOccurence.append(pdfResult.Ocurrence)
            for ary in  pdfResult.Values :
                responseAry.append(ary)
            pdfSeedList.append(pdfResult)
        responseAryNotEmpty = [x for x in responseAry if (x != [] and len(x)>1)]
        dataAry=responseAryNotEmpty
        #PlotMulti(responseAry) #add epty remove 
        responseAry=[]
        x =x+1
    

    

if __name__ == "__main__":
    main()


