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
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    interference=options.interference
    

    #cc_command=GetCombineCardCommands(mass,year,bst)+'> combine_hwwlnuqq_'+bst+'_'+mass+'_'+year+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    ##---1)WORKDIR
    workdir="WORKDIR/MakeWorkSpace/"+mass+"__"+bst+"__"+year
    ##---2)input card path
    combinecard_path="Datacards_"+year+"/combine_hwwlnuqq_"+bst+"_"+mass+"_"+year+".txt"
    ##---3)model python
    modelpy="HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.XWWInterference_jhchoi:XWW"
    ##---4)Physics Options
    PO="--PO NoSMXsecAdded"
    if not interference: PO+=" --PO noInterference"
    ##---5)WS output paths
    WSDIRpath='Workspaces_'+year
    if not interference: WSDIRpath+="_NoI"
    WSpath=WSDIRpath+"/hwwlnuqq_"+bst+"_"+mass+"_"+year+".root"
    ##---6)WS command
    ws_command="text2workspace.py "+combinecard_path+" -P "+modelpy+" "+PO+" -o "+WSpath
    commands=["cd "+os.getcwd(),'mkdir -p '+WSDIRpath,ws_command]
    command=';'.join(commands)    
    jobname=workdir
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
