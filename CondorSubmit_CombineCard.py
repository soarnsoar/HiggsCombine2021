import os

##---------------------------------Card Config----------------------##
def GetCardPath(mass,year,cut):
    cats={}
    mass=str(mass)
    year=str(year)
    #__BoostedALL_SB_VBFCUT_0.3
    if cut=="nocut":
        cats["hww_lqq_bst_vbf_sb_"+year]="Datacard_M"+mass+"/__BoostedALL_SB__nocut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacard_M"+mass+"/__BoostedALL_TOP__nocut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]="Datacard_M"+mass+"/__BoostedALL_SR__nocut/WW_mass/datacard.txt"
        
        #notcut
        cats["hww_lqq_res_vbf_sb_"+year]="Datacard_M"+mass+"/___ResolvedALL__SB_notcut/Event/datacard.txt"
        cats["hww_lqq_res_vbf_top_"+year]="Datacard_M"+mass+"/___ResolvedALL__TOP_notcut/Event/datacard.txt"
        cats["hww_lqq_res_vbf_"+year]="Datacard_M"+mass+"/___ResolvedALL__SR_notcut/WW_mass/datacard.txt"
    else:
        cats["hww_lqq_bst_vbf_sb_"+year]="Datacard_M"+mass+"/__BoostedALL_SB_VBFCUT_"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacard_M"+mass+"/__BoostedALL_TOP_VBFCUT_"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]="Datacard_M"+mass+"/__BoostedALL_SR_VBFCUT_"+cut+"/WW_mass/datacard.txt"
        
        
        cats["hww_lqq_res_vbf_sb_"+year]="Datacard_M"+mass+"/___ResolvedALL__SB_VBFCUT_"+cut+"/Event/datacard.txt"
        cats["hww_lqq_res_vbf_top_"+year]="Datacard_M"+mass+"/___ResolvedALL__TOP_VBFCUT_"+cut+"/Event/datacard.txt"
        cats["hww_lqq_res_vbf_"+year]="Datacard_M"+mass+"/___ResolvedALL__SR_VBFCUT_"+cut+"/WW_mass/datacard.txt"
        



        
    return cats

def GetCombineCardCommands(mass,year,bst,isDNN=True):
    cats={}
    if year=="3yrs":
        cats2016=GetCardPath(mass,2016,isDNN)
        cats2017=GetCardPath(mass,2017,isDNN)
        cats2018=GetCardPath(mass,2018,isDNN)
        

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
        cats=GetCardPath(mass,year,isDNN)
    

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
    parser.add_option("-c", "--cut", dest="cut" , help="cut")
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    cut=(options.cut)

    

    cc_command=GetCombineCardCommands(mass,year,bst,cut)+'> combine_hwwlnuqq_'+bst+'_'+mass+'_'+year+'__CUT_'+cut+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    workdir="WORKDIR/CombineCard/"+mass+"__"+bst+"__cut_"+cut+"__"+year
    os.system('mkdir -p Datacards_'+year)
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]
    command=';'.join(commands)
    
    jobname=workdir
    jobname='CombineDatacards'
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
