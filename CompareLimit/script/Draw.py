import sys
import os
__HC_VBFOPT__SOARNSOAR__=os.getenv("__HC_VBFOPT__SOARNSOAR__")
sys.path.append(__HC_VBFOPT__SOARNSOAR__+'/CompareLimit/python/')
from LimitReader import LimitReader

if __name__ == '__main__':
    bst="Boosted"
    year="2016"
    masses=[400,500,600,700,800,900,1000]
    cuts=['nocut',0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
    for cut in cuts:
        for mass in masses:
            reader=LimitReader(mass,bst,year,cut)
            _limit=reader.GetLimit()
            print mass,cut,_limit
