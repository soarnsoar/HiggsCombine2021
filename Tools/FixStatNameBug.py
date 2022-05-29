##---CMS_2016___BoostedVBFDNN_SB_NoMEKDCut_Event_ggH_hww1000_RelW002_bin1_statshape -> CMS_2016___BoostedVBFDNN_SB_NoMEKDCut_Event_ggH_hww1000_RelW002_bin1_stat  shape

##---scan all datacards
import glob
DCLIST=glob.glob('Datacards_201*/*/*/*/*/*.txt')
print "nDC=",len(DCLIST)

##--fix
import os
for DC in DCLIST:
    f=open(DC,'r')
    fnew=open(DC+'_new','w')
    lines=f.readlines()
    for line in lines:
        if '_statshape' in line:
            line=line.replace('_statshape','_stat  shape')
        fnew.write(line)
    f.close()
    fnew.close()
    os.system('mv '+DC+' '+DC+'_old')
    os.system('mv '+DC+'_new'+' '+DC)
