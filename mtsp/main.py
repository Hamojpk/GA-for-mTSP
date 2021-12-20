import random
from ipga import IPGA
import IPpop
from NGA import NGA
import NewPop
from NGA2 import NGA2
import NewPop2
from dustbin import Dustbin
import globals
from galogic import GA
import matplotlib.pyplot as plt
import progressbar

from population import Population
from routemanager import RouteManager

numNodes = globals.loadSet('pr226.txt')
# Add Dustbins
for i in range(numNodes):
    RouteManager.addDustbin(Dustbin(globals.xlist[i], globals.ylist[i]))

random.seed(1)
yaxis = []  # Fittest value (distance)
xaxis = []  # Generation count
ny2 = []
ny=[]
print(globals.calutime)
globals.calutime = 0
i=0



#baseline
pop = Population(globals.populationSize, True)
globalRoute = pop.getFittest()
for i in range(globals.numGenerations+20):
    print(i)
    print(globalRoute.getDistance())
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print(globals.calutime)
globals.calutime=0


#nga2
newpop2=NewPop2.NewPop(globals.populationSize, True)
gNew2 = newpop2.newGetFittest()
for i in range(globals.numGenerations+20):
    print(i)
    print(gNew2.getDistance())
    newpop2 = NGA2.evolvePopulation(newpop2)
    lnew2 = newpop2.newGetFittest()
    if gNew2.getDistance() > lnew2.getDistance():
        gNew2 = lnew2
    ny2.append(lnew2.getDistance())
print(globals.calutime)
globals.calutime=0

#nga
npop=NewPop.NewPop(globals.populationSize,True)
gn=npop.newGetFittest()
for i in range(globals.numGenerations+20):
    print(i)
    print(gn.getDistance())
    npop = NGA.evolvePopulation(npop)
    ln = npop.newGetFittest()
    if gn.getDistance() > ln.getDistance():
        gn = ln
    ny.append(ln.getDistance())
print(globals.calutime)
globals.calutime = 0

print(globals.calutime)
print('Global minimum distance: ' + str(globalRoute.getDistance()))
print('Final Route: ' + globalRoute.toString())
print('Global minimum distance: ' + str(gNew2.getDistance()))
print('Final Route: ' + gNew2.toString())
print('Global minimum distance: ' + str(gn.getDistance()))
print('Final Route: ' + gn.toString())
fig = plt.figure()
plt.plot(xaxis, yaxis, 'r-')
plt.plot(xaxis, ny2, 'b-')
plt.plot(xaxis,ny,'g-')
plt.show()
