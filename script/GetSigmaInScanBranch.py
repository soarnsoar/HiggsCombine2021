import ROOT
import glob
import sys

def GetSigmaOnScanBranch(param):

    xlist=[]
    inputpath=glob.glob("higgsCombinescan.MultiDimFit*.root")[0]
    tfile=ROOT.TFile.Open(inputpath)
    ttree=tfile.Get("limit")
    for i in ttree:
        exec("x=i."+param)
        xlist.append(x)
    xlist=sorted(set(xlist))
    tfile.Close()
    #print xlist[0],xlist[1],xlist[2]
    
    return xlist[0],xlist[1],xlist[2]
if __name__ == '__main__':
    param=sys.argv[1] ##
    nominal=int(sys.argv[2])
    xm,x0,xp=GetSigmaOnScanBranch(param)
    x3m=xm-2*(x0-xm)
    x3p=x0+2*(xp-x0)
    if nominal:
        print param+'='+str(x0)
    else:
        print param+'='+str(x3m)+','+str(x3p)
