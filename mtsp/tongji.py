import gc
import random

import NewPop
import NewPop2
import globals
from NGA import NGA
from NGA2 import NGA2
from dustbin import Dustbin
from galogic import GA
from population import Population
from routemanager import RouteManager

filename=['mtsp51.txt','mtsp100.txt','mtsp150.txt','pr76.txt','pr152.txt','pr226.txt']
for f in filename:
    globals.loadSet(f)
    nodenumber=globals.numNodes
    popnumber=globals.populationSize
    ngal=[]
    nga2l=[]
    baseline=[]
    RouteManager.destinationDustbins=[]
    for i in range(nodenumber):
        RouteManager.addDustbin(Dustbin(globals.xlist[i], globals.ylist[i]))
    for i in range(30):
        random.seed(random.randint(0,400))
        pop = Population(globals.populationSize, True)
        globalRoute = pop.getFittest()
        j=0
        globals.calutime=0
        while globals.calutime<=20000*nodenumber:
            j+=1
            pop = GA.evolvePopulation(pop)
            localRoute = pop.getFittest()
            if globalRoute.getDistance() > localRoute.getDistance():
                globalRoute = localRoute
        print(j)
        globals.calutime=0
        baseline.append(globalRoute.getDistance())
        j=0
        newpop2 = NewPop2.NewPop(globals.populationSize, True)
        gNew2 = newpop2.newGetFittest()
        while globals.calutime<=20000*nodenumber:
            newpop2 = NGA2.evolvePopulation(newpop2)
            lnew2 = newpop2.newGetFittest()
            if gNew2.getDistance() > lnew2.getDistance():
                gNew2 = lnew2
            j+=1
        print(j)
        globals.calutime = 0
        nga2l.append(gNew2.getDistance())

        j=0
        npop = NewPop.NewPop(globals.populationSize, True)
        gn = npop.newGetFittest()
        while globals.calutime<=20000*nodenumber:
            npop = NGA.evolvePopulation(npop)
            ln = npop.newGetFittest()
            if gn.getDistance() > ln.getDistance():
                gn = ln
            j+=1
        print(j)
        globals.calutime = 0
        ngal.append(gn.getDistance())
        del pop,npop,newpop2,globalRoute,gn,gNew2


    avg=[sum(ngal)/len(ngal),sum(nga2l)/len(nga2l),sum(baseline)/len(baseline)]
    maxtr=[max(ngal),max(nga2l),max(baseline)]
    mintr=[min(ngal),min(nga2l),min(baseline)]
    ff=open('resultrecord.txt','a+')
    ff.write('-------------'+f+'-------------\n')
    ff.write('nga'+str(ngal)+'\n')
    ff.write('nga2'+str(nga2l) + '\n')
    ff.write('baseline'+str(baseline) + '\n')
    ff.write(str(avg) + '\n')
    ff.write(str(maxtr) + '\n')
    ff.write(str(mintr) + '\n')
    ff.close()


