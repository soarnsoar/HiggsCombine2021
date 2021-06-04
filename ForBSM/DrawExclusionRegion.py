import ROOT
import json
from numpy import array
input_json="exregion_json/mh125_13_withVBF__2016.json"

json_data={}

with open(input_json,"r") as json_file:
    json_data = json.load(json_file)
    #json_data[tanb]=[mA_ex1, mA_ex2] 

#print json_data
ylist=[]
for tanb in sorted(json_data):
    ylist.append(float(tanb))
ylist=sorted(ylist)

ylist=array(ylist)
print ylist

xlist=[]
for i in range(501):
    xlist.append(float(i))
xlist=array(xlist)

h=ROOT.TH2D("test contour","test contour",len(xlist)-1, xlist, len(ylist)-1, ylist)



for y in json_data:
    for x in xlist:
        if len(json_data[y])==2:
            xmin=json_data[y][0]
            xmax=json_data[y][1]
            if x >= xmin and x< xmax: 
                h.Fill(x,float(y),2)

#contours=[1]
#contours=array(contours)
c1=ROOT.TCanvas()
c1.SetLogy()
h.SetFillColor(2)
#h.SetContour(0)
h.Draw("colz")
#h.Smooth()
h.SetStats(0)
ROOT.gPad.Update()
#linelist=ROOT.gROOT.GetListOfSpecials().FindObject("contours")
#g=linelist[0]
#g.Draw()
c1.SaveAs("temp_contour.pdf")
