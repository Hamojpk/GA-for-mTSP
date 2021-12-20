import globals
from dustbin import Dustbin
from globals import *
from routemanager import RouteManager


class NewRoute:
    # Good old constructor
    def __init__ (self, route = None):
        # 2D array which is collection of respective routes taken by trucks
        self.route = []
        # 1D array having routes in a series - used during crossover operation
        self.base = []
        # 1D array having route lengths
        self.routeLengths = route_lengths()
        self.startpos=RouteManager.getDustbin(0)
        # fitness value and total distance of all routes
        self.fitness = 0
        self.distance = 0

        # creating empty route
        if route == None:
            for i in range(RouteManager.numberOfDustbins()-1):
                self.base.append(Dustbin(-1,-1))

        else:
            self.route = route

    def generateIndividual (self):
        self.routeLengths = route_lengths()
        k=0
        # put 1st member of RouteManager as it is (It represents the initial node) and shuffle the rest before adding
        for dindex in range(1, RouteManager.numberOfDustbins()):
            self.base[dindex-1] = RouteManager.getDustbin(dindex)
        random.shuffle(self.base)
        self.startpos=RouteManager.getDustbin(0)
        pos=0
        for i in range(numTrucks):
            # add same first node for each route
            for j in range(self.routeLengths[i]-1):
                pos+=1
                self.route.append(self.base[k]) # add shuffled values for rest
                k+=1

    # Returns j'th dustbin in i'th route
    def getDustbin(self, i, j):
        pos=0
        for p in range(i):
            pos+=self.routeLengths[p]-1
        pos+=(j-1)
        return self.route[pos]

    # Sets value of j'th dustbin in i'th route
    def setDustbin(self, i, j, db):
        pos = 0
        for p in range(i):
            pos += self.routeLengths[p]
        pos += j
        self.route[pos] = db
        #self.route.insert(index, db)
        self.fitness = 0
        self.distance = 0

    # Returns the fitness value of route
    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 9000/self.getDistance()

        return self.fitness

    # Return total ditance covered in all subroutes
    def getDistance(self):

        if self.distance == 0:

            routeDistance = 0
            pos=0
            for i in range(numTrucks):
                routeDistance+=self.startpos.distanceTo(self.route[pos])
                for j in range(self.routeLengths[i]-1):
                    fromDustbin = self.route[pos+j]
                    if j+1 < self.routeLengths[i]-1:
                        destinationDustbin = self.route[pos+j+1]
                    else:
                        destinationDustbin = self.startpos
                    routeDistance += fromDustbin.distanceTo(destinationDustbin)
                pos += j+1
            self.distance=routeDistance
        return self.distance

    # Checks if the route contains a particular dustbin
    def containsDustbin(self, db):
        if db in self.base: #base <-> route
            return True
        else:
            return False

    # Returns route in the form of a string
    def toString (self):
        geneString = '|'
        print (self.routeLengths)
        #for k in range(RouteManager.numberOfDustbins()-1):
        #    print (self.base[k].toString())
        pos=0
        for i in range(numTrucks):
            geneString+=self.startpos.toString()+'|'
            for j in range(self.routeLengths[i]-1):
                geneString += self.route[pos+j].toString() + '|'
            geneString += '\n'
            pos+=(j+1)

        return geneString
