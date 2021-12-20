from IPpop import *
import globals


class IPGA:

    @classmethod
    def evolvePopulation(cls, pop):

        newPopulation = IPpop(pop.populationSize, False)
        elitismOffset = 0
        # If fittest chromosome has to be passed directly to next generation

        # Performs tournament selection followed by crossover to generate child
        rlist=[]
        for i in range(globals.populationSize):
            rlist.append(i)
        num=0
        for i in range(10):
            contemlist = []
            if i==9:
                for j in rlist:
                    contemlist.append(pop.nroutes[j])
            else:
                for j in range(10):
                    s=cls.select(pop,rlist)
                    rlist.remove(s)
                    contemlist.append(pop.nroutes[s])
            maxlen=len(contemlist[0].route)
            ii,j,p=cls.createPos(maxlen)
            cls.flipInsert(contemlist[1],ii,j,p)
            cls.swapInsert(contemlist[2],ii,j,p)
            cls.lslideInsert(contemlist[3],ii,j,p)
            cls.rslideInsert(contemlist[4],ii,j,p)
            cls.flipInsert(contemlist[6], ii, j, p)
            cls.swapInsert(contemlist[7], ii, j, p)
            cls.lslideInsert(contemlist[8], ii, j, p)
            cls.rslideInsert(contemlist[9], ii, j, p)
            for j in range(5,10):
                cls.modifyBreaks(contemlist[j])
            for j in range(10):
                contemlist[j].distance=0
                contemlist[j].fitness=0
                newPopulation.saveRoute(num, contemlist[j])
                num+=1

        return newPopulation

    @classmethod
    def createPos(cls,maxlen):
        i = random.randint(0, maxlen)
        j = random.randint(0, maxlen)
        while i == j or (i-j+1)==maxlen or (j-1+1)==maxlen:
            i = random.randint(0, maxlen)
            j = random.randint(0, maxlen)
        if i > j:
            t = i
            i = j
            j = t
        p=random.randint(0,maxlen-(j-i+1))
        return i,j,p

    @classmethod
    def select(cls,pop,rlist):
        random.shuffle(rlist)
        picked=rlist[0:10]
        fest=picked[0]
        for i in picked:
            if pop.nroutes[i].getFitness()<pop.nroutes[fest].getFitness():
                fest=i
        return fest

    @classmethod
    def flipInsert(cls,route,i,j,p):
        r = route.route
        swap=r[i:j+1]
        swap.reverse()
        r=r[:i]+r[j+1:]
        route.route=r[:p]+swap+r[p:]

    @classmethod
    def swapInsert(cls,route,i,j,p):
        r = route.route
        swap = r[i:j + 1]
        t=swap[0]
        swap[0]=swap[-1]
        swap[-1]=t
        r = r[:i] + r[j + 1:]
        route.route = r[:p] + swap + r[p:]

    @classmethod
    def lslideInsert(cls,route,i,j,p):
        r = route.route
        swap = r[i:j + 1]
        t = swap[0]
        swap=swap[1:]
        swap.append(t)
        r = r[:i] + r[j + 1:]
        route.route = r[:p] + swap + r[p:]

    @classmethod
    def rslideInsert(cls,route,i,j,p):
        r = route.route
        swap = r[i:j + 1]
        t = swap[-1]
        swap=swap[:-1]
        swap=[t]+swap
        r = r[:i] + r[j + 1:]
        route.route = r[:p] + swap + r[p:]

    @classmethod
    def modifyBreaks(cls,route):
        route.routeLengths=globals.route_lengths()
