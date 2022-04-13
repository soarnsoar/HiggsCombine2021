##---CMS_2016___BoostedVBFDNN_SB_NoMEKDCut_Event_ggH_hww1000_RelW002_bin1_statshape -> CMS_2016___BoostedVBFDNN_SB_NoMEKDCut_Event_ggH_hww1000_RelW002_bin1_stat  shape

##---scan all datacards
import glob
#DCLIST=glob.glob('Datacards_2016/Datacard_M1000/__BoostedGGFDNN_SR_UNTAGGED_M1500_C0.01/Event/datacard.txt')
DCLIST=glob.glob('Datacards_*/*.txt')
print "nDC=",len(DCLIST)

##--fix
import os
for DC in DCLIST:
    if os.path.isfile(DC+'_old_rateparamname'):
        
        f=open(DC+'_old_rateparamname','r')
    else:
        f=open(DC,'r')
    fnew=open(DC+'_new','w')
    lines=f.readlines()
    for line in lines:
        
        if ("rateParam" in line):
            rateparamname=line.split()[0]
            #print rateparamname
            rateparamname="_".join([rateparamname.split('_')[0],rateparamname.split('_')[1],rateparamname.split('_')[3]])
            line='  '.join([rateparamname]+line.split()[1:])+'\n'
            #line='  '.join(newline_inlist)
            #print line
        fnew.write(line)
    f.close()
    fnew.close()
    os.system('mv '+DC+' '+DC+'_old_rateparamname')
    os.system('mv '+DC+'_new'+' '+DC)
