import os
class CollectLimitCommand:
    def __init__(self,year,suffix):
        year=str(year)
        LimitDIR="AsymptoticLimits/"+year+"/"+suffix
        command_list=["cd "+os.getcwd(),"mkdir -p "+LimitDIR,"cd "+LimitDIR]
        Collect="combineTool.py -M CollectLimits -i higgsCombine*.root"
        command_list.append(Collect)
        self.command= "&&".join(command_list)
    def GetCommand(self):
        return self.command


