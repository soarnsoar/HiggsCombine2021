import json
import os
class Read_R:
    def __init__(self,year,model,mA,tanb,key):
        self.year=year
        self.model=model
        self.mA=mA
        self.tanb=tanb
        self.key=key
        self.GetR()

    def GetR(self):
        path=self.GetPath()
        if not os.path.isfile(path):return 2000. 
        with open(path,"r") as handle:
            result=json.load(handle)
        self.mH=sorted(result)[0]
        if self.key in result[self.mH]:
            return result[self.mH][self.key]
        else:
            return 2000

    def Get_mH(self):
        return self.mH

        '''
        {"133.363998413": {"exp-2": 176.77754828751384, "exp-1": 258.0100004800538, "exp+2": 1655.8395688343098, "exp+1": 1098.7472741322565, "exp0": 545.9736358662002, "obs": 83810.84094883689
        '''

    def GetPath(self):
        path='../AsymptoticLimits/'+str(self.year)+'/'+str(self.model)+'/mA_'+str(self.mA)+'_tanb_'+str(self.tanb)+'/limits_interpolate.json'
        return path
