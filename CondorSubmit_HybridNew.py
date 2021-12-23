import os
import sys
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export
#def MakeWorkSpaceCommand(year,mass,bst,mela_m,c,wp,interference,POlist,model_alias=""):
def HybridNewLimitCommand(year,mass,bst,mela_m,c,wp,interference,fvbf,POlist,suffix=""):

    if not interference: suffix+="_NoI"
    ##---1)WORKDIR
    workdir="WORKDIR/HybridNewLimits/"+suffix+"/"+'M'+mela_m+"_C"+c+'/'+mass+"__"+bst+"__"+wp+"__"+year+"/"+fvbf+'/'
    ##---2)input WS
    WSDIRpath=os.getcwd()+"/"+'Workspaces_'+year
    #if not interference: WSDIRpath+="_NoI"


    #suffix="_".join(POlist)
    #Workspaces_2016/model_indep/0.0/hwwlnuqq_Boosted_1000_2016.root
    #WSDIRpath='Workspaces_'+year+"/"+model_alias+'/'+'M'+mela_m+'__'+'C_'+c+'/'+wp
    WSpath=WSDIRpath+"/"+suffix+'/'+'M'+mela_m+'__'+'C_'+c+'/'+wp+"/hwwlnuqq_"+("_".join([bst,mass,year]))+".root"
    #WSpath=WSDIRpath+"/hwwlnuqq_"+bst+"_"+mass+"_"+year+".root"
    ##--3)fvbf options
    opt_fvbf="-------"
    if 'ggfonly' in fvbf:
        #opt_fvbf="--freezeParameters fvbf,rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*} --setParameters fvbf=0  --rAbsAcc 0"
        opt_fvbf="--freezeParameters fvbf --setParameters fvbf=0  --rAbsAcc 0"
    if 'vbfonly' in fvbf:
        opt_fvbf="--freezeParameters fvbf --setParameters fvbf=1  --rAbsAcc 0"
    if 'floating' in fvbf:
        opt_fvbf="--freezeParameters  --rAbsAcc 0"
    
    ##--3-1) option for fast fitting
    #opt_minst="--cminDefaultMinimizerStrategy 0"
    opt_minst=""

    ##---4)limit command combine -d hwwlnuqq_Boosted_1000_2016.root --LHCmode LHC-limits  -M HybridNew
    limit_command="combine -M HybridNew -d "+WSpath+" -m "+mass+" "+opt_fvbf+" "+opt_minst+" --LHCmode LHC-limits -T 500 --expectedFromGrid=0.5"
    #limit_command="combine -M HybridNew -d "+WSpath+" -m "+mass+" --run expected "+opt_fvbf
    #limit_command="combine -M HybridNew -d "+WSpath+" -t -1 -m "+mass+" "+' --freezeParameters allConstrainedNuisances'

    ##---5)outputdir
    outputdir='HybridNewLimits/'+year+'/model_indep/'+"/"+'M'+mela_m+"_C"+c+'/'+bst+'/'+wp+"/"+fvbf+'/'+suffix
    
    
    commands=["cd "+os.getcwd(),'mkdir -p '+outputdir,'cd '+outputdir,limit_command]
    command=';'.join(commands)    
    jobname="HybridNewLimits"
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
    parser.add_option("-w", "--wp", dest="wp" , help="wp")
    parser.add_option("-i", "--interference", dest="interference" ,default=False  , action="store_true")
    parser.add_option("-f", "--fvbf", default=False,dest="fvbf")
    parser.add_option("-p", "--PO", default=False,dest="PO")

    parser.add_option("-c", "--c", dest="c" , help="c")
    parser.add_option("-a", "--mela_m", dest="mela_m" , help="mela_m")
    
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    wp=options.wp
    interference=bool(options.interference)
    c=options.c
    mela_m=options.mela_m

    print 'interference',interference
    if options.fvbf:
        fvbf=options.fvbf
    else:
        fvbf="r_PoI"
    
    if not options.PO:
        POlist=[]
    else:
        POlist=options.PO.split(",")
        

    #def HybridNewLimitCommand(year,mass,bst,mela_m,c,wp,interference,fvbf,POlist,suffix=""):
    workdir,command,jobname,submit,ncpu=HybridNewLimitCommand(year,mass,bst,mela_m,c,wp,interference,fvbf,POlist,"model_indep")
    Export(workdir,command,jobname,submit,ncpu)
    
