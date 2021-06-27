from Tools.Plot import * 
import math 
import numpy

#the idea is the pdf shape indicates info or relations -> then can changed saped into level help predict the next elements ?

def main(): # This project should be called find a distribution model! (: 

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
    SeedQuanity=20
    while level<2:
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
        #selectedAry = list(dict.fromkeys([0, round(len(PrbOccurence)/2), len(PrbOccurence)-1]))
        selectedAry = list(dict.fromkeys([0, 1, 2]))
        PlotByIdx(PrbOccurence, selectedAry)
        #Plot(responseAryNotEmpty)
        #PlotMulti(responseAry) #add epty remove 
        responseAry=[]
        level =level+1
    

    

if __name__ == "__main__":
    main()

    #todo do -> the goal is to find relation in each level which can decrease the enthropy tp zero.
    # then it is like knowing by features (algebra)-> which properties can be find in each level 
    # Also it is ajusta tet åproject for python this is why this algorithm is vague and there is no
    # value continuig it.
    # This method is aimed for biological/ scattering real targets not prime num. 
