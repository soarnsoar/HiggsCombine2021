import os
import sys
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export

def AsymptoticLimitCommand(year,mass,bst,interference,POlist,suffix=""):

    if not interference: suffix+="_NoI"
    ##---1)WORKDIR
    workdir="WORKDIR/AsymptoticLimits/"+suffix+"/"+mass+"__"+bst+"__"+year+"/"
    ##---2)input WS
    WSDIRpath=os.getcwd()+"/"+'Workspaces_'+year
    #if not interference: WSDIRpath+="_NoI"


    #suffix="_".join(POlist)

    WSpath=WSDIRpath+"/"+suffix+"/hwwlnuqq_"+("_".join([bst,mass,year]))+".root"
    #WSpath=WSDIRpath+"/hwwlnuqq_"+bst+"_"+mass+"_"+year+".root"
    ##--3)options
    
    opt="--freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*}"
    
    ##---4)limit command
    asymplimit_command="combine -M AsymptoticLimits -d "+WSpath+" -m "+mass+" "+opt


    ##---5)outputdir
    outputdir='AsymptoticLimits/'+year+'/smlike/'+bst+"/"+'/'+suffix
    
    
    commands=["cd "+os.getcwd(),'mkdir -p '+outputdir,'cd '+outputdir,asymplimit_command]
    command=';'.join(commands)    
    jobname=os.getcwd()+'/'+workdir
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
    parser.add_option("-i", "--interference", dest="interference" ,default=False  , action="store_true")
    
    parser.add_option("-p", "--PO", default=False,dest="PO")
    
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    interference=bool(options.interference)
    print 'interference',interference
    
    if not options.PO:
        POlist=[]
    else:
        POlist=options.PO.split(",")
        


    workdir,command,jobname,submit,ncpu=AsymptoticLimitCommand(year,mass,bst,interference,POlist,"smlike")
    Export(workdir,command,jobname,submit,ncpu)
    
