import glob
import os
import sys
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export

#Datacards_2016/Datacard_M1000/__BoostedALL_SR_NoMEKDCut/Event/
CardDirs_Event=glob.glob("Datacards_201*/Datacard_M*/*/Event/")
print CardDirs_Event

for d in CardDirs_Event:
    commands=["cd "+os.getcwd(),"cd "+d,'ValidateDatacards.py datacard.txt']
    command='&&'.join(commands)
    jobname="ValidateDatacards"
    submit=True
    ncpu=1
    workdir="WORKDIR_ValidateDatacards/"+d
    Export(workdir,command,jobname,submit,ncpu)

