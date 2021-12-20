import NewChrome
import globals

class NewPop:
    nroutes = []

    # Good old contructor
    def __init__(self, populationSize, initialise):

        self.populationSize = populationSize
        if initialise:
            self.nroutes = []
            for i in range(populationSize):
                chrome = NewChrome.NewRoute()
                chrome.generateIndividual()
                self.nroutes.append(chrome)
        else:
            for i in range(populationSize):
                self.nroutes.append(None)


    def newSaveRoute(self, index, route):
        self.nroutes[index] = route

        # Returns route at index

    def newGetRoute(self, index):
        return self.nroutes[index]

        # Returns route with maximum fitness value

    def newGetFittest(self):
        fittest = self.nroutes[0]

        for i in range(1, self.populationSize):
            if fittest.getFitness() <= self.newGetRoute(i).getFitness():
                fittest = self.newGetRoute(i)

        return fittest

    def populationSize(self):
        return int(self.populationSize)

    # Equate current population values to that of pop
    def equals(self, pop):
        self.routes = pop.routes
