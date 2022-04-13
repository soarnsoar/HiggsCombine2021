import ROOT
import glob
import sys

def GetSigmaOnScanBranch(param):

    xlist=[]
    inputpath=glob.glob("higgsCombinescan.MultiDimFit**.root")[0]
    tfile=ROOT.TFile.Open(inputpath)
    ttree=tfile.Get("limit")
    for i in ttree:
        exec("x=i."+param)
        xlist.append(x)
    xlist=sorted(set(xlist))
    tfile.Close()
    #print xlist[0],xlist[1],xlist[2]
    print 'param='+str(xlist[0])+','+str(xlist[2])
    return xlist[0],xlist[1],xlist[2]
if __name__ == '__main__':
    param=sys.argv[1] ##
