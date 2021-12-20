import random
import globals
import NewChrome
import NewPop2
from dustbin import Dustbin


class NGA:

    @classmethod
    def evolvePopulation(cls, pop):

        newPopulation = NewPop2.NewPop(pop.populationSize, False)

        elitismOffset = 0
        # If fittest chromosome has to be passed directly to next generation
        if globals.elitism:
            newPopulation.newSaveRoute(0, pop.newGetFittest())
            elitismOffset = 1

        # Performs tournament selection followed by crossover to generate child
        for i in range(elitismOffset, newPopulation.populationSize):
            parent1 = cls.newtournamentSelection(pop)
            parent2 = cls.newtournamentSelection(pop)
            child = cls.newcrossover(parent1, parent2)
            # Adds child to next generation
            newPopulation.newSaveRoute(i, child)

        # Performs Mutation
        for i in range(elitismOffset, newPopulation.populationSize):

            cls.newmutate(newPopulation.newGetRoute(i))

        return newPopulation

    @classmethod
    def newcrossover(cls, parent1, parent2):
        child = NewChrome.NewRoute()

        rpos=random.randint(0,len(parent1.route)-1)

        for i in range(rpos):
            child.route.append(Dustbin(-1,-1))
        for i in range(rpos,len(parent1.route)):
            child.route.append(parent1.route[i])
        pos=0
        for t in parent2.route:
            if pos==rpos:
                break
            if t not in child.route:
                child.route[pos]=t
                pos+=1


        return child

    # Mutation opeeration
    @classmethod
    def newmutate(cls, route:NewChrome.NewRoute):

        # print ('Indexes selected: ' + str(index1) + ',' + str(index2))

        # generate replacement range for 1
        r1 = random.randint(1,len(route.route) - 1)
        r2 = random.randint(1, len(route.route)- 1)
        while r1==r2:
            r1 = random.randint(1, len(route.route) - 1)
            r2 = random.randint(1, len(route.route) - 1)
        if r1<r2:
            route1startPos = r1
            route1lastPos = r2
        else:
            route1startPos = r2
            route1lastPos = r1

        # generate replacement range for 2

        if random.randrange(1) < globals.mutationRate:
            route.distance = 0
            route.fitness = 0
            route1 = route
            temp = route1.route[r1]
            route1.route[r1] = route.route[r2]
            route1.route[r2] = temp

            swap = route.route[route1startPos:route1lastPos]
            swap.reverse()
            route.route[route1startPos:route1lastPos] = swap
            if route.getDistance() > route1.getDistance():
                route.route = route1.route

            route2=route.routeLengths
            route2=globals.route_lengths()

            if route.getDistance() > route2.getDistance():
                route.routeLengths = route1.routeLengths


    # Tournament Selection: choose a random set of chromosomes and find the fittest among them
    @classmethod
    def newtournamentSelection(cls, pop):
        tournament = NewPop2.NewPop(globals.tournamentSize, False)

        for i in range(globals.tournamentSize):
            randomInt = random.randint(0, pop.populationSize - 1)
            tournament.newSaveRoute(i, pop.newGetRoute(randomInt))

        fittest = tournament.newGetFittest()
        return fittest