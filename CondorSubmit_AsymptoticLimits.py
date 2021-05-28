import os

if __name__ == '__main__':
    #GetCommands(1000,2016)
    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option("-y", "--year", dest="year" , help="year")
    parser.add_option("-m", "--mass", dest="mass" , help="mass")
    parser.add_option("-b", "--bst", dest="bst" , help="bst")
    parser.add_option("-i", "--interference", dest="interference" ,default=True  , action="store_true")
    parser.add_option("-f", "--fvbf", dest="fvbf")
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    interference=options.interference
    fvbf=options.fvbf


    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    ##---1)WORKDIR
    workdir="WORKDIR/AsymptoticLimits/"+mass+"__"+bst+"__"+year+"/"+fvbf+'/'
    ##---2)input WS
    WSDIRpath=os.getcwd()+"/"+'Workspaces_'+year
    if not interference: WSDIRpath+="_NoI"
    WSpath=WSDIRpath+"/hwwlnuqq_"+bst+"_"+mass+"_"+year+".root"
    ##--3)fvbf options
    opt_fvbf="-------"
    if 'ggfonly' in fvbf:
        opt_fvbf="--freezeParameters fvbf --setParameters fvbf=0"
    if 'vbfonly' in fvbf:
        opt_fvbf="--freezeParameters fvbf --setParameters fvbf=1"
    if 'floating' in fvbf:
        opt_fvbf=""
    ##---4)limit command
    asymplimit_command="combine -M AsymptoticLimits -d "+WSpath+" --trackParameters fvbf -t -1 --run expected --rAbsAcc 0 -m "+mass+" "+opt_fvbf

    ##---5)outputdir
    outputdir='AsymptoticLimits/'+year+'/'+bst+"/"+fvbf+'/'
    if not interference: outputdir+="_NoI"
    
    commands=["cd "+os.getcwd(),'mkdir -p '+outputdir,'cd '+outputdir,asymplimit_command]
    command=';'.join(commands)    
    jobname=workdir
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
