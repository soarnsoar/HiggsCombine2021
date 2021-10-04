import sys

sys.path.insert(0,'../')
sys.path.insert(0,'.')
sys.path.insert(0,'../python_tool')
sys.path.insert(0,'python_tool')

from ExportShellCondorSetup import Export
from CondorSubmit_MakeWorkSpace import MakeWorkSpaceCommand

from math import sqrt
import os
def GetSMXsec(mH):
    if os.path.isfile('xsec_smlike.py'):
        exec(open("xsec_smlike.py",'r'))
    else:
        exec(open("ForSMLike/xsec_smlike.py",'r'))
    ggh=xsec_smlike['GGF'][mH]['nominal']
    ggh_pdfUp=xsec_smlike['GGF'][mH]['pdfUp']
    ggh_pdfDown=xsec_smlike['GGF'][mH]['pdfUp']
    ggh_scaleUp=xsec_smlike['GGF'][mH]['scaleUp']
    ggh_scaleDown=xsec_smlike['GGF'][mH]['scaleUp']

    gghUp=sqrt((ggh_pdfUp-1)**2+(ggh_scaleUp-1)**2)
    gghDown=sqrt((ggh_pdfDown-1)**2+(ggh_scaleDown-1)**2)

    qqh=xsec_smlike['VBF'][mH]['nominal']
    qqh_pdfUp=xsec_smlike['VBF'][mH]['pdfUp']
    qqh_pdfDown=xsec_smlike['VBF'][mH]['pdfUp']
    qqh_scaleUp=xsec_smlike['VBF'][mH]['scaleUp']
    qqh_scaleDown=xsec_smlike['VBF'][mH]['scaleUp']

    qqhUp=sqrt((qqh_pdfUp-1)**2+(qqh_scaleUp-1)**2)
    qqhDown=sqrt((qqh_pdfDown-1)**2+(qqh_scaleDown-1)**2)
    print ggh,gghUp,gghDown,qqh,qqhUp,qqhDown
    return ggh,gghUp,gghDown,qqh,qqhUp,qqhDown

def WorkSpaceCommand(year,mH,bst,interference):
    xsec_gghwwlnuqq,xsec_gghwwlnuqq_totalup,xsec_gghwwlnuqq_totaldown,xsec_qqhwwlnuqq,xsec_qqhwwlnuqq_totalup,xsec_qqhwwlnuqq_totaldown=GetSMXsec(mH)

    POlist=["input_ggH_xsec:"+str(xsec_gghwwlnuqq),
            "input_qqH_xsec:"+str(xsec_qqhwwlnuqq),
            "delta_ggH_xsec:"+str(xsec_gghwwlnuqq_totalup)+","+str(xsec_gghwwlnuqq_totaldown),
            "delta_qqH_xsec:"+str(xsec_qqhwwlnuqq_totalup)+","+str(xsec_qqhwwlnuqq_totaldown)
        ]
    #MakeWorkSpaceCommand(year,mass,bst,interference,POlist,"model_indep")
    workdir,command,jobname,submit,ncpu = MakeWorkSpaceCommand(year,mH,bst,interference,POlist,"smlike")
    Export(workdir,command,jobname,submit,ncpu)




if __name__ == '__main__':
    ##
    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option("-y", "--year", dest="year" , help="year")
    parser.add_option("-m", "--mass", dest="mass" , help="mass")
    parser.add_option("-b", "--bst", dest="bst" , help="bst")
    parser.add_option("-i", "--interference", dest="interference" ,default=False  , action="store_true")
    
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    interference=options.interference
    
    WorkSpaceCommand(year,int(mass),bst,interference)
