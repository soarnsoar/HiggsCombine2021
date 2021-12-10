
#python_tool/ExportShellCondorSetup.py
import sys
sys.path.insert(0,'python_tool')
from ExportShellCondorSetup import Export
from FixStatNameBug_DCpath import FixStatNameBug
#def Export(WORKDIR,command,jobname,submit,ncpu,nretry=3):


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
            _command='python Tools/FixStatNameBug_DCpath.py '+DC
            commandlist.append(_command)
        #Export(WORKDIR,command,jobname,submit,ncpu,nretry=3)
        command='&&'.join(commandlist)
        WORKDIR='WORKDIR_FixStatNameBug/'+DCDIR_M
        jobname="FixStatNameBug"
        submit=True
        ncpu=1
        Export(WORKDIR,command,jobname,submit,ncpu)

