import os
import sys
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export


def MakeWorkSpaceCommand(year,mass,bst,mela_m,c,wp,interference,POlist,model_alias=""):
    year=str(year)
    mass=str(mass)
    #model_alias="_".join(POlist)
    if not interference: model_alias+="_NoI"
    ##---1)WORKDIR
    #if model_alias!="":
    #    workdir="WORKDIR/MakeWorkSpace/"+mass+"__"+bst+"__"+year
    #else:
    #    workdir="WORKDIR/MakeWorkSpace/"+mass+"__"+bst+"__"+year+"__"+model_alias
    workdir="WORKDIR/MakeWorkSpace/"+model_alias+'/'+'M'+mela_m+'__'+'C_'+c+'/'+wp+"/"+("__".join([mass,bst,year]))
    ##---2)input card path #combine_hwwlnuqq_Boosted_0.6_1000_2016
    #combinecard_path="Datacards_"+year+"/combine_hwwlnuqq_"+bst+'_'+wp+"_"+mass+"_"+year+".txt"
    combinecard_path="Datacards_"+year+"/combine_hwwlnuqq_"+bst+'_M'+mela_m+"_"+"c"+c+"_"+wp+'_'+mass+'_'+year+'.txt'
    ##---3)model python
    modelpy="HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.XWWInterference_jhchoi:XWW"
    ##---4)Physics Options
    PO="--PO NoSMXsecAdded"
    if not interference: PO+=" --PO noInterference"
    for _PO in POlist:
        PO+=" --PO "+_PO
    ##---5)WS output paths
    WSDIRpath='Workspaces_'+year+"/"+model_alias+'/'+'M'+mela_m+'__'+'C_'+c+'/'+wp

    
    WSpath=WSDIRpath+"/hwwlnuqq_"+("_".join([bst,mass,year]))+".root"
    ##---6)WS command
    ws_command="text2workspace.py "+combinecard_path+" -P "+modelpy+" "+PO+" -o "+WSpath
    commands=["cd "+os.getcwd(),'mkdir -p '+WSDIRpath,ws_command]
    command=';'.join(commands)    
    #jobname=workdir
    jobname='MakeWS'
    submit=True
    ncpu=1


    #Export(workdir,command,jobname,submit,ncpu)
    return workdir,command,jobname,submit,ncpu
if __name__ == '__main__':
    #GetCommands(1000,2016)
    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option("-y", "--year", dest="year" , help="year")
    parser.add_option("-m", "--mass", dest="mass" , help="mass")
    parser.add_option("-b", "--bst", dest="bst" , help="bst")
    parser.add_option("-w", "--wp", dest="wp" , help="bst")
    parser.add_option("-i", "--interference", dest="interference" ,default=False  , action="store_true")
    parser.add_option("-p", "--PO", dest="PO" ,default=False)

    parser.add_option("-c", "--c", dest="c" , help="c")
    parser.add_option("-a", "--mela_m", dest="mela_m" , help="mela_m")

    
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    wp=options.wp
    interference=options.interference
    if options.PO:
        POlist=options.PO.split(',')
    else:
        POlist=[]
    c=options.c
    mela_m=options.mela_m

    
    #def MakeWorkSpaceCommand(year,mass,bst,mela_m,c,wp,interference,POlist,model_alias=""):
    workdir,command,jobname,submit,ncpu=MakeWorkSpaceCommand(year,mass,bst,mela_m,c,wp,interference,POlist,"model_indep")
    Export(workdir,command,jobname,submit,ncpu)
