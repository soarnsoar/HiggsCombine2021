import json
import sys
import os
__HC_VBFOPT__SOARNSOAR__=os.getenv("__HC_VBFOPT__SOARNSOAR__")
#sys.path.append(__HC_VBFOPT__SOARNSOAR__)
#combineTool.py -M CollectLimits -i higgsCombine*.root -o indep.json
#AsymptoticLimits/2016/model_indep/Boosted/0.05/vbfonly/model_indep_NoI/indep.json
'''
  "1000.0": {
    "exp+1": 0.027506103739142418,
    "exp+2": 0.036606743931770325,
    "exp-1": 0.014311913400888443,
    "exp-2": 0.010770559310913086,
    "exp0": 0.01983642578125,
    "obs": 0.023824886639499807

'''
class LimitReader:
    def __init__(self,mass,bst,year,cut):
        self.mass=str(mass)
        self.bst=bst
        self.year=str(year)
        self.cut=str(cut)

    def ReadJson(self):

        path='/'.join([__HC_VBFOPT__SOARNSOAR__,'AsymptoticLimits',self.year,'model_indep',self.bst,self.cut,'vbfonly','model_indep_NoI','indep.json'])
        #print path
        self.data={}
        with open(path,'r') as st_json:
            self.data=json.load(st_json)
    def GetLimit(self,l='exp0'):
        self.ReadJson()
        if str(float(self.mass)) in self.data:
            if l in self.data[str(float(self.mass))]:
                limit=self.data[str(float(self.mass))][l]
            else:
                limit=9999999999
        else:
            limit=99999999999999
        return limit
