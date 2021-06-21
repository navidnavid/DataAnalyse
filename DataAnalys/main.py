from Tools.Plot import * 
import math 
import numpy

#the idea is the pdf shape indicates info or relations -> then can changed saped into level help predict the next elements ?

def main():

    info=[]

    #------------
    #infoNrml= generateNumberSine(4)
    infoNrml= generateNumberPrime()

    #------------
    dataAry=[]
    dataAry.append(infoNrml)
    responseAry=[]
    PrbOccurence=[]
    x=0
    pdfSeedList = []
    SeedQuanity=30
    while x<8:
        for  infoNrml in dataAry:
            l=len(infoNrml)
            l=len(dataAry)
            pdfResult = Pdf(infoNrml,SeedQuanity,x)
            PrbOccurence.append(pdfResult.Ocurrence)
            for ary in  pdfResult.Values :
                responseAry.append(ary)
            pdfSeedList.append(pdfResult)
        responseAryNotEmpty = [x for x in responseAry if (x != [] and len(x)>1)]
        dataAry=responseAryNotEmpty
        Plot(PrbOccurence)
        Plot(responseAryNotEmpty)
        #PlotMulti(responseAry) #add epty remove 
        responseAry=[]
        x =x+1
    

    

if __name__ == "__main__":
    main()


