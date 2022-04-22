import ROOT
def GetYields(shape_output,proclist):
    #print shape_output
    tfile=ROOT.TFile.Open(shape_output)
    _y=0
    for _proc in proclist:
        _histoname='histo_'+_proc
        _h=tfile.Get(_histoname)
        _y+=_h.Integral()
    tfile.Close()
    return _y
