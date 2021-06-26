from Tools.Plot import * 
import math 
import numpy

#the idea is the pdf shape indicates info or relations -> then can changed saped into level help predict the next elements ?

def main():

    info=[]

    #------------
    #infoNrml= generateNumberSine(4)
    infoNrml= generateNumberPrime()
    print(len(infoNrml))
    #------------
    dataAry=[]
    dataAry.append(infoNrml)   
    responseAry=[]
    PrbOccurence=[]
    level=0
    pdfSeedList = []
    SeedQuanity=3
    while level<4:
        for  infoNrml in dataAry:
            l=len(infoNrml)
            l=len(dataAry)
            pdfResult = Pdf(infoNrml,SeedQuanity,level)
            PrbOccurence.append(pdfResult.Ocurrence)
            for ary in  pdfResult.Values :
                responseAry.append(ary)
            pdfSeedList.append(pdfResult)
        responseAryNotEmpty = [x for x in responseAry if (x != [] and len(x)>1)]
        dataAry=responseAryNotEmpty

        #Plot(PrbOccurence, 2)
        selectedAry = list(dict.fromkeys([0, round(len(PrbOccurence)/2), len(PrbOccurence)]))
        PlotByIdx(PrbOccurence, selectedAry)
        #Plot(responseAryNotEmpty)
        #PlotMulti(responseAry) #add epty remove 
        responseAry=[]
        level =level+1
    

    

if __name__ == "__main__":
    main()


