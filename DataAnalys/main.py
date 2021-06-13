from Tools.Plot import * 
import math 
import numpy

def main():

    info=[]
    rad = numpy.radians(range(0, 360))
    for r in rad :
         info.append( math.sin( r ))
    #Plot(info)
    infoNrml= [element/max(info) * 100 for element in info]
        
    pdfResult = Pdf(infoNrml,5,1)
    pdfResult = Pdf(infoNrml,10,1)
    pdfResult = Pdf(infoNrml,20,1)


    1+1


if __name__ == "__main__":
    main()


