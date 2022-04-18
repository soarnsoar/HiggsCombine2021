##---CMS_2016___BoostedVBFDNN_SB_NoMEKDCut_Event_ggH_hww1000_RelW002_bin1_statshape -> CMS_2016___BoostedVBFDNN_SB_NoMEKDCut_Event_ggH_hww1000_RelW002_bin1_stat  shape

##---scan all datacards
import glob
#DCLIST=glob.glob('Datacards_2016/Datacard_M1000/__BoostedGGFDNN_SR_UNTAGGED_M1500_C0.01/Event/datacard.txt')
DCLIST=glob.glob('Datacards_*/*.txt')
print "nDC=",len(DCLIST)

##--fix
import os
for DC in DCLIST:
    f=open(DC,'r')
    fnew=open(DC+'_new','w')
    lines=f.readlines()
    for line in lines:
        
        if ("rateParam" in line) and not ('1 [0,50]' in line):
            #Wjetsnorm_Boosted_GGFDNN0_2016                              rateParam                __BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01       Wjets0j                  1.0000
            newline_inlist=line.split()[:-1]+['1 [0,50]\n']
            line='  '.join(newline_inlist)
            #print line
        fnew.write(line)
    f.close()
    fnew.close()
    os.system('mv '+DC+' '+DC+'_old_rateparam')
    os.system('mv '+DC+'_new'+' '+DC)
