import random

from routemanager import *
from NewChrome import NewRoute
import globals

class IPpop:

    nroutes = []

    # Good old contructor
    def __init__(self, populationSize, initialise):
        self.populationSize = populationSize
        if initialise:
            for i in range(populationSize):
                chrome = NewRoute()
                chrome.generateIndividual()
                self.nroutes.append(chrome)

    # Saves the route passed as argument at index
    def saveRoute(self, index, route):
        self.nroutes[index] = route

    # Returns route at index
    def getRoute(self, index):
        return self.nroutes[index]
    # Returns route with maximum fitness value
    def getFittest(self):
        fittest = self.nroutes[0]

        for i in range(1, self.populationSize):
            if fittest.getFitness() <= self.getRoute(i).getFitness():
                fittest = self.getRoute(i)

        return fittest




        # Returns route at index



        # Returns route with maximum fitness value


    def populationSize(self):
        return int(self.populationSize)


