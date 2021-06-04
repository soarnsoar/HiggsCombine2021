import os
import sys
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export

def AsymptoticLimitCommand(year,mass,bst,interference,fvbf,POlist,suffix=""):

    ##---1)WORKDIR
    workdir="WORKDIR/AsymptoticLimits/"+suffix+"/"+mass+"__"+bst+"__"+year+"/"+fvbf+'/'
    ##---2)input WS
    WSDIRpath=os.getcwd()+"/"+'Workspaces_'+year
    if not interference: WSDIRpath+="_NoI"


    #suffix="_".join(POlist)
    if not interference: suffix+="_NoI"
    WSpath=WSDIRpath+"/"+suffix+"/hwwlnuqq_"+("_".join([bst,mass,year,suffix]))+".root"
    #WSpath=WSDIRpath+"/hwwlnuqq_"+bst+"_"+mass+"_"+year+".root"
    ##--3)fvbf options
    opt_fvbf="-------"
    if 'ggfonly' in fvbf:
        opt_fvbf="--freezeParameters fvbf --setParameters fvbf=0  --rAbsAcc 0"
    if 'vbfonly' in fvbf:
        opt_fvbf="--freezeParameters fvbf --setParameters fvbf=1  --rAbsAcc 0"
    if 'floating' in fvbf:
        opt_fvbf=" --rAbsAcc 0"
    
    ##---4)limit command
    asymplimit_command="combine -M AsymptoticLimits -d "+WSpath+" -t -1 --run expected -m "+mass+" "+opt_fvbf

    ##---5)outputdir
    outputdir='AsymptoticLimits/'+year+'/model_indep/'+bst+"/"+fvbf+'/'+suffix
    
    
    commands=["cd "+os.getcwd(),'mkdir -p '+outputdir,'cd '+outputdir,asymplimit_command]
    command=';'.join(commands)    
    jobname=workdir
    submit=True
    ncpu=1

    return workdir,command,jobname,submit,ncpu


if __name__ == '__main__':
    #GetCommands(1000,2016)
    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option("-y", "--year", dest="year" , help="year")
    parser.add_option("-m", "--mass", dest="mass" , help="mass")
    parser.add_option("-b", "--bst", dest="bst" , help="bst")
    parser.add_option("-i", "--interference", dest="interference" ,default=True  , action="store_true")
    parser.add_option("-f", "--fvbf", default=False,dest="fvbf")
    parser.add_option("-p", "--PO", default=False,dest="PO")
    
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    interference=options.interference
    if options.fvbf:
        fvbf=options.fvbf
    else:
        fvbf="r_PoI"
    
    if not options.PO:
        POlist=[]
    else:
        POlist=options.PO.split(",")
        


    workdir,command,jobname,submit,ncpu=AsymptoticLimitCommand(year,mass,bst,interference,fvbf,POlist,"model_indep")
    Export(workdir,command,jobname,submit,ncpu)
    
