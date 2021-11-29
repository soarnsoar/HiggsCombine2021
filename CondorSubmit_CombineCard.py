import os

##---------------------------------Card Config----------------------##
def GetCardPath(mass,year,WP,isDNN=True):
    cats={}
    mass=str(mass)
    year=str(year)
    if isDNN:
        ##--Boosted
        cats["hww_lqq_bst_vbf_sb_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_SB_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_TOP_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_SR_NoMEKDCut/WW_mass/datacard.txt"
        ##--Resolved
        cats["hww_lqq_vbf_sb_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__SB_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_vbf_top_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__TOP_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_vbf_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__SR_NoMEKDCut/WW_mass/datacard.txt"
    else:
        print 1/0
        
    return cats

def GetCombineCardCommands(mass,year,bst,WP,isDNN=True):
    cats={}
    if year=="3yrs":
        cats2016=GetCardPath(mass,2016,WP,isDNN)
        cats2017=GetCardPath(mass,2017,WP,isDNN)
        cats2018=GetCardPath(mass,2018,WP,isDNN)
        

        for cat in cats2016:
            cats2016[cat]="../Datacards_2016/"+cats2016[cat]
        for cat in cats2017:
            cats2017[cat]="../Datacards_2017/"+cats2017[cat]
        for cat in cats2018:
            cats2018[cat]="../Datacards_2018/"+cats2018[cat]

        cats.update(cats2016)
        cats.update(cats2017)
        cats.update(cats2018)
    else:
        cats=GetCardPath(mass,year,WP,isDNN)
    

    command="combineCards.py -S "
    for cat in cats:
        if bst!="all":
            if not bst in cats[cat] : continue
        command+=cat+"="+cats[cat]+" "


    print command
    return command

if __name__ == '__main__':
    #GetCommands(1000,2016)
    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option("-y", "--year", dest="year" , help="year")
    parser.add_option("-m", "--mass", dest="mass" , help="mass")
    parser.add_option("-b", "--bst", dest="bst" , help="bst")
    parser.add_option("-w", "--wp", dest="wp" , help="wp")
    parser.add_option("-d", "--dnn", dest="dnn" , help="dnn",action='store_true',)
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    wp=options.wp
    dnn=bool(options.dnn)

    

    cc_command=GetCombineCardCommands(mass,year,wp,bst,dnn)+'> combine_hwwlnuqq_'+bst+'_'+wp+'_'+mass+'_'+year+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    workdir="WORKDIR/CombineCard/"+mass+"__"+bst+"__"+wp+"__"+year
    os.system('mkdir -p Datacards_'+year)
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]
    command=';'.join(commands)
    
    #jobname=workdir
    jobname="combinecard"
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
