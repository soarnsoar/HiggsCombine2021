
#python_tool/ExportShellCondorSetup.py
import sys
sys.path.insert(0,'python_tool')
from ExportShellCondorSetup import Export
from FixRateParams_DCpath import FixRateParam
#def Export(WORKDIR,command,jobname,submit,ncpu,nretry=3):
def FixRateParam(DCpath):
    f=open(DC,'r')
    fnew=open(DC+'_new','w')
    lines=f.readlines()
    for line in lines:
        
        if ("rateParam" in line) and not ('1 [0,5]' in line):
            newline_inlist=line.split()[:-1]+['1 [0,5]\n']
            line='  '.join(newline_inlist)
            #print line                                                                                                                                   
        fnew.write(line)
        f.close()
        fnew.close()
        os.system('mv '+DC+' '+DC+'_old_rateparam')
        os.system('mv '+DC+'_new'+' '+DC)



##---scan all datacards
if __name__ == '__main__':
    import os
    curdir=os.getcwd()
    import glob
    DCDIR_M_LIST=glob.glob('Datacards_*/*/')
    


    for DCDIR_M in DCDIR_M_LIST:
        commandlist=[]
        commandlist.append('cd '+curdir)
        DCLIST=glob.glob(DCDIR_M+"/*/*/*.txt")
        for DC in DCLIST:
            #FixRateParam(DC)
            _command='python Tools/FixRateParams_DCpath.py '+DC
            commandlist.append(_command)
        #Export(WORKDIR,command,jobname,submit,ncpu,nretry=3)
        command='&&'.join(commandlist)
        WORKDIR='WORKDIR_FixRateParam/'+DCDIR_M
        jobname="FixRateParam"
        submit=True
        ncpu=1
        Export(WORKDIR,command,jobname,submit,ncpu)

