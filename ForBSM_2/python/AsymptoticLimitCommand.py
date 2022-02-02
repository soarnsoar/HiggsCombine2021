import os

class AsymptoticLimitCommand:
    def __init__(self,year,mH,suffix,bst):
        year=str(year)
        mH=str(mH)
        WSpath=os.getcwd()+"/Workspaces_"+year+"/"+suffix+"/hwwlnuqq_"+bst+"_"+mH+"_"+year+".root"
        LimitDIR="AsymptoticLimits/"+year+"/"+suffix
        command_list=["cd "+os.getcwd(),"mkdir -p "+LimitDIR,"cd "+LimitDIR]
        LimitOptions=" -m "+mH+" --freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*}"
        Asymptotic="combine -M AsymptoticLimits -d "+WSpath+" "+LimitOptions+" "
        command_list.append(Asymptotic)
        self.command= "&&".join(command_list)
    def GetCommand(self):
        return self.command

