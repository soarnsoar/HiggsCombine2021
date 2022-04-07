import os
import sys
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export

def MultiDimFitCommand(year,mass,bst,interference,POI,POlist,cut,suffix=""):

    if not interference: suffix+="_NoI"
    ##---1)WORKDIR
    #workdir="WORKDIR/MultiDimFit/"+suffix+"/"+mass+"__"+bst+"__"+year+"__"+cut+"/"+POI+'/'
    workdir="WORKDIR/MultiDimFit/"+suffix+"/"+mass+"__"+bst+"__"+year+"__"+cut+"/"
    ##---2)input WS
    WSDIRpath=os.getcwd()+"/"+'Workspaces_'+year
    #if not interference: WSDIRpath+="_NoI"


    #suffix="_".join(POlist)

    WSpath=WSDIRpath+"/"+suffix+"/hwwlnuqq_"+("_".join([bst,mass,year,cut]))+".root"
    #WSpath=WSDIRpath+"/hwwlnuqq_"+bst+"_"+mass+"_"+year+".root"
    ##--3)POI options

    ##--3-1) option for fast fitting
    opt_minst="--cminDefaultMinimizerStrategy 0"
    opt_minst=""
    
    ##---4)limit command
    POIARG=','.join(POI)
    POIRANGE='=0,5:'.join(POI)
    POIRANGE.rstrip(':')
    POIRANGE+='=0,5'
    #multidimfit_command="combine -M MultiDimFit -d "+WSpath+" -m "+mass+" --redefineSignalPOIs "+POIARG+" --freezeParameters sigma,fvbf --setParameters sigma=0,fvbf=0 --algo grid --points 1200 --setParameterRanges "+POIRANGE+" "+opt_minst
    multidimfit_command="combine -M MultiDimFit -d "+WSpath+" -m "+mass+" --redefineSignalPOIs "+POIARG+" --freezeParameters sigma,fvbf --setParameters sigma=0,fvbf=0 --algo singles --cl=0.68 --setParameterRanges "+POIRANGE+" "+opt_minst


    ##---5)outputdir
    #outputdir='MultiDimFit/'+year+'/model_indep/'+bst+"/"+"/"+cut+"/"+POI+'/'+suffix
    outputdir='MultiDimFit/'+year+'/model_indep/'+bst+"/"+"/"+cut+"/"+suffix
    
    
    commands=["cd "+os.getcwd(),'mkdir -p '+outputdir,'cd '+outputdir,multidimfit_command]
    command=';'.join(commands)    
    jobname="multidim"
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
    parser.add_option("-r", "--poi", default=False,dest="POI")
    parser.add_option("-p", "--PO", default=False,dest="PO")
    parser.add_option("-c", "--cut", default=False,dest="cut")
    
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    interference=bool(options.interference)
    cut=options.cut
    POI=options.POI.split(',')
    print 'interference',interference
    if not options.PO:
        POlist=[]
    else:
        POlist=options.PO.split(",")
        


    workdir,command,jobname,submit,ncpu=MultiDimFitCommand(year,mass,bst,interference,POI,POlist,cut,"model_indep")
    Export(workdir,command,jobname,submit,ncpu)
    
