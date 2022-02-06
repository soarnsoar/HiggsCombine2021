import sys
sys.path.append('python')
from ExclusionDrawer import ExDrawer


if __name__ == '__main__':
    year=sys.argv[1]
    model=sys.argv[2]
    #mydraw=ExDrawer(2016,'mh125_13')
    mydraw=ExDrawer(year,model)
    mydraw.Draw()
