'''Graph is set up as a list of dictionaries of form: 

graph = [ {'gender':0, #0 is female, 1 is male
    'inContact':[[n1,weightn1],[n2,weightn2],[n3,weightn3]], #list of the people they're connected with --> outer list is the connected verticies, nested list's 0th element is the connected vertex. 1st element is the weight of that edge
    'demise':'zombie' #state of life-fullness, string, choices: 'buried', 'alive', 'zombie'
    'natImmunity':.30 #Naturally occuring, percent immunity of the person
    'age':20 #integer representing person's age
    'inocFac':[0,0,1,0,0,1,1,0] #list representing the inoculation of the person, 0==not vaccinated on that day, 1==vaccinated that day, index of array is the day
    'ebola':0 #do they have ebola? 0==no, 1==yes
    'pDeath': .4 #probability of person dying that day
    'n':3 #n value of that person, vame as the index of the person in the array
    },
    {...},
    {...}
]'''

import pprint
import random
import matplotlib.pyplot as plt
import numpy as np
#import scipy.stats as stats #commenting for use on ubuntu server
import pickle

####################################
#####Variable Variables:############
####################################
peopleInModel = 700
sizeClique = 7
femalesPerClique = 4
probBurialThatDay = .35 #probability of a zombie being buried that day, less than 1
supplyVaccine = 230 #doses per day (or time step) **varry
numConnStrtEbola = 50 #number of people in the vilage who start with ebola
lowFamilyEdgeWeight = 40.0 #1-100%
highFamilyEdgeWeight = 55.0 #1-100%
lowWeightRandomEdges = 2.0 #1-100%
highWeightRandomEdges = 30.0 #1-100
natImmunityInit = .1
numRandomEdges = 30
daysToRunModel = 400
effectofFemaleonPDeath = .15

####################################
#####Not-Variable Variables:#####
####################################
graph = []
demiseWTime = []
buried=[]; alive=[]; zombies=[]

####################################
#####INITALIZE AND SETUP GRAPH:#####
####################################
def initializeGraph():
    graph[:]=[]
    cycle=1 #for gender toggle, don't change
    for vertex in range(peopleInModel):
        personRepDict = {'n':vertex,
            'ebola':0,
            'demise':'alive',
            'natImmunity':natImmunityInit,
            'inocFac':[0],
            'pDeath':0.0}
        

            
        #Set ages of the population!!!
        percentAge=random.randint(0,100)
        if (percentAge<=4):
            personRepDict['age']=random.randint(65,80)
        elif (percentAge<=8) and (percentAge>4):
            personRepDict['age']=random.randint(55,64)
        elif (percentAge<=39) and (percentAge>8):
            personRepDict['age']=random.randint(25,54)
        elif (percentAge<=58) and (percentAge>39):
            personRepDict['age']=random.randint(15,24)
        elif (percentAge<=100) and (percentAge>58):
            personRepDict['age']=random.randint(0,14)
        
        graph.append(personRepDict)

    #add a vertex's clique pals (family) as edges:
    n=0
    for nVtxActl, vertex in enumerate(graph):
        if (nVtxActl%sizeClique)==0:
            for n in range(0,sizeClique):
                #construct the list of the verticies a vertex in a click is connected with:
                s1 = []; s2=[]
                s1 = range(0,n)
                s2 = range(n+1,sizeClique)             
                setS = s1+s2 #the vertices it would be connected to
                actualConnectedVertices = [x+nVtxActl for x in setS]
                writeList = []
                for v in actualConnectedVertices:
                    #make a list of lists where v is the connected vertex and the next argument is the weight of that vertex
                    writeList.append([v,random.randint(lowFamilyEdgeWeight,highFamilyEdgeWeight)/100.0])      
#                print 'nVtxActl: ', nVtxActl
                graph[nVtxActl+n]['inContact']=writeList #TODO: This used to be +n. I might have broken it.


        #set gender distrabution:
        if cycle<femalesPerClique+1:
            personRepDict['gender']=0
            personRepDict['pDeath']=personRepDict['pDeath']+effectofFemaleonPDeath
            cycle=cycle+1
        elif (cycle<sizeClique):
            personRepDict['gender']=1
            cycle=cycle+1
        else:
            personRepDict['gender']=1
            cycle = 1

    #Add in some random graph edges to connect the cliques:
    for _i in range(numRandomEdges):
        parentVertex = random.randint(1,peopleInModel-1)
        childVertex = random.randint(1,peopleInModel-1)
        edgeWeight = random.randint(lowWeightRandomEdges,highWeightRandomEdges)/100.0
        if not(childVertex==parentVertex):
            graph[parentVertex]['inContact'].append([childVertex,edgeWeight])
    #        print graph[parentVertex]['inContact']


####################################
#####BEGIN GRAPH THEORY MODEL:######
####################################

def computeVaccineImmunity(personNumber):
    '''Computes the acquired imunity from receiving a vaccine. 
    #immunity from vaccine increases by .2 per dose
    #immunity decreases by 1/3 of the increase from vaccine with each day w/out vaccine
    
    Never needs to be called itself. Called by computeSusceptabilityDisease()'''
    inocHistory = graph[personNumber]['inocFac']
    inocProb = 0
    for day in inocHistory:
        if (day==0) and (inocProb > 0): 
            #they didn't get the vaccine and they still have some immunity from previous doses
            inocProb = inocProb - (.17/3.0)
        elif day==1:
            #They got the vaccine and will have more immunity! Yeah!
            inocProb = inocProb + .17
    return inocProb

def vaccinatePpl():
    '''Performs triage on the population and administers vaciene to 
    those at greatest risk before others. 
    
    Called in updateGraph()'''
    sup = supplyVaccine
    ill = []
    two0_inoc = []
    one0_inoc = []
    yest_inoc = []
    for person,perDict in enumerate(graph):
#        print 'inocFac: ', graph[person], '\n'
#        print 'person is: ', person
        if graph[person]['pDeath']<0.4:
            if graph[person]['ebola']==1:
                ill.append(graph[person])
            elif graph[person]['inocFac'][-1]==0:
                if len(graph[person]['inocFac']) > 2 and inocFacgraph[person]['inocFac'][-2]==0:
                    two0_inoc.append(graph[person])
                else:
                    one0_inoc.append(graph[person])
            else: 
                yest_inoc.append(graph[person])
    for personNum, person in enumerate(ill):
        if sup>0:
            graph[personNum]['inocFac'].append(1)
            sup=sup-1
        else:
            break
    for person in two0_inoc:
        if sup>0:
            graph[personNum]['inocFac'].append(1)
            sup=sup-1
        else:
            break
    for person in one0_inoc:
        if sup>0:
            graph[personNum]['inocFac'].append(1)
            sup=sup-1
        else:
            break
    for person in yest_inoc:
        if sup>0:
            graph[personNum]['inocFac'].append(1)
            sup=sup-1
        else:
            break
        
def computeSusceptabilityDisease(personNumber):
    '''Computes the succeptability of an indivigual to Ebola.
    Never needs to be called itself (though can be). Called by:
        computeProbabilityDeath()'''
    natImmunity = graph[personNumber]['natImmunity']
    inocFac = computeVaccineImmunity(personNumber)
    
    susceptability = (1-natImmunity)*(1-inocFac)
    return susceptability

def computeProbabilityDeath(personNumber):
    '''Compute a given person's probability of death
    
    called by vertexDemise() to determine if the vertex turns zombie'''
    
    person = graph[personNumber]
    if len(person['inContact']) == 0:
        return person['pDeath']
    neighbor_death = 0
    suceptibility = computeSusceptabilityDisease(personNumber)
    for contact in person['inContact']:
        neighbor_death = neighbor_death + (graph[(contact[0])]['pDeath']*contact[1])
    
    return suceptibility*neighbor_death/len(person['inContact'])

def vertexDemise(personNumber):
    '''manage killing people and turning them into zombies:'''
    #'demise':'zombie' #state of life-fullness, string, choices: 'buried', 'alive', 'zombie'
    
    #move people from alive to dead:
    theirDeathRand = random.randint(0.0,100.0)/100.0
    pDeath = computeProbabilityDeath(personNumber)
    demiseState=graph[personNumber]['demise']
#    print 'death rand: ', theirDeathRand, 'pDeath: ', pDeath
    if (pDeath > theirDeathRand) and (demiseState=='alive'):
        #they're alive and it was their bad day to die
        graph[personNumber]['demise']='zombie'
    if (demiseState=='zombie') and (theirDeathRand<probBurialThatDay):
        #they have a 35% chance of being buried on a given day
        graph[personNumber]['demise']='buried'
        for personNum,personRepDict in enumerate(graph):
            for edges in graph[personNum]['inContact']:
                if graph[personNum]['inContact'][0] == personNumber:
                    graph[personNum]['inContact'][1] = 0
    elif (demiseState=='zombie'):
        #increase risk of death for a zombie's connections the longer they aren't buried
        for personNum,personRepDict in enumerate(graph):
            for edges in graph[personNum]['inContact']:
                if graph[personNum]['inContact'][0] == personNum:
                    graph[personNum]['inContact'][1] = graph[personNum]['inContact'][1]+.05
    

def contactEbola(personNumber):
    '''Compute the risk of a person contacting Ebola and if they do, 
    change their Ebola state to true'''
    ebolaRisk = 0
    numConnectionsWEbola = 0 # # of their connections w/ ebola
    randEbolaNum = random.randint(1.0,100.0)/100.0
    for connection in graph[personNumber]['inContact']:
        #Sum the probability of them getting ebola
        if graph[connection[0]]['ebola']==1: #If their connection has ebola:
            ebolaRisk = ebolaRisk + connection[1] #
            numConnectionsWEbola = numConnectionsWEbola+1
    if (numConnectionsWEbola>0) and (randEbolaNum<=(ebolaRisk/numConnectionsWEbola)):
        #set node's ebola boolean high if generated probability was high enough.
        graph[personNumber]['ebola']=1
        ebolaRisk = ebolaRisk/numConnectionsWEbola
#        print 'ebla rsk: ', ebolaRisk
    
def grabModelDataRT():
    '''grabs the model data during run time and stores it in a useful 
    way for plotting.
    Buried. Alive. Zombie.
    returns demiseWTime, a list of lists that should be unpacked with 
    processBZAdata()'''

    buriedCurrent = 0; zombieCurrent = 0; aliveCurrent = 0
    for person in graph:
        if person['demise']=='buried':
            buriedCurrent=buriedCurrent+1
        elif person['demise']=='alive':
            aliveCurrent=aliveCurrent+1
        elif person['demise']=='zombie':
            zombieCurrent=zombieCurrent+1
    demiseWTime.append([buriedCurrent,zombieCurrent,aliveCurrent])
    return demiseWTime
        

def updateGraph():
    '''Calls the sub functions that will update vertecies in 
    the graph. Does these for all verticies in graph with each time 
    step. Stores data from these iterations in data structures for 
    plotting'''
    #start a few people with ebola for testing purposes
    for person in range(numConnStrtEbola):
        unluckyPerson = random.randint(0,peopleInModel-1)
        graph[unluckyPerson]['ebola']=1
        graph[unluckyPerson]['pDeath']=.1*random.randint(3,9)
    
    vaccinatePpl() #vacinate the graph against ebola with available vaciene
    for day in range(daysToRunModel):
        grabModelDataRT()
        for personNum, personRepDict in enumerate(graph):
            contactEbola(personNum)
            vertexDemise(personNum)
            
def processBZAdata(demiseWTime):   
    '''Extract the three data streems (burried, zombie or alive) into their 
    seprate type lists. Finally plots these by calling makeBZAplot()'''     
    buried=[]; zombies=[]; alive=[]   
    for day, _data in enumerate(demiseWTime):
        buried.append(demiseWTime[day][0])
        zombies.append(demiseWTime[day][1])
        alive.append(demiseWTime[day][2])
    return (buried,zombies,alive)
    
def makeBZAplot(buried, zombies, alive):
    plt.plot(buried, color='k', linewidth=3.0, label = 'Bodies Buried')
#    print 'vals plotted initially: ', buried[0], ' ', buried[3], ' ',  buried[8]
#    print buried
    plt.plot(zombies, color='r', linewidth=3.0, label = 'Unburied Bodies')
    plt.plot(alive, color='g', linewidth=3.0, label='People Alive')
    plt.legend()
    plt.xlabel('Days',fontsize=20)
    plt.ylabel('Number of People', fontsize=20)
    plt.title ('Population Changes over '+ str(daysToRunModel) + ' Days',fontsize=30)
    plt.show()
    plt.clf()
    
def makePoincarePlotAlive(alive) :
    #poincare plot:
    x=[]; y=[]
    for key, value in enumerate(alive):
        if key < len(alive)-1:
            x.append(alive[key])
            y.append(alive[key+1])
    print x[-1]
    plt.plot(x,y, 'ro', markersize=7)
    ln=range(100,peopleInModel+3)
    plt.plot(ln,ln, linewidth=3.0)
    plt.ylabel('People at (t+1)', fontsize=20)
    plt.xlabel('People at (t)', fontsize=20)
    plt.title('Population Poincare Plot', fontsize=30)
    plt.show()
    return x,y

def iterateThroughValuesnumConnStrtEbola():
    global numConnStrtEbola
    global buried
    global alive
    global zombies
    global demiseWTime
    
    topIterableVariableBound=400
    bottomIterableVariableBound=1
    numberTimesTry = 2000
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)
        numConnStrtEbola=assesValue
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "5xConnStrtEbola.p", "wb" ) )
    pickle.dump( dataStore, open( "5yConnStrtEbola.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'bo')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
#    print 'len x: ', len(x), ' len y: ', len(y)
#    print 'fds: ', x[0], 'hhhhh ', y[0]
#    print 'x: ', x
#    print 'y: ', y
    plt.plot(x, m*x+b, 'm',linewidth=3.0) 
    
    plt.ylabel('Average Living at Model End (People)', fontsize=20)
    plt.xlabel('Initial Infection (People)', fontsize=20)
    plt.title('Effect of Initial Infection on Outcome ', fontsize=30)
    plt.savefig('ConnStrtEblaEffectOnPop5.png')
    plt.clf()    
#    makeStats()
    
    plt.plot(y, stats.norm.pdf(y), 'm-', lw=5, alpha=0.6, label='pdf')
    plt.title('PDF ', fontsize=30)
    plt.savefig('ConnStrtEblaPDF5.png')
    plt.clf()
    
def iterateThroughValuesRandEdges():
    global numRandomEdges
    global buried
    global alive
    global zombies
    global demiseWTime
    
    topIterableVariableBound=700
    bottomIterableVariableBound=1
    numberTimesTry = 3500
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)
        numRandomEdges=assesValue
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "6xRandEdges.p", "wb" ) )
    pickle.dump( dataStore, open( "6yRandEdges.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'mo')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'g',linewidth=3.0) 
    
    plt.ylabel('Average Living at Model End (People)', fontsize=17)
    plt.xlabel('Number Extra Familial (Edges)', fontsize=17)
    plt.title('Effect of Extra Familial Edges', fontsize=30)
    plt.savefig('6extraFamilialEdgesSktrPlt.png')
    plt.clf()
#    makeStats()
    
#    plt.plot(y, stats.norm.pdf(y), 'm-', lw=5, alpha=0.6, label='pdf')
#    plt.title('PDF ', fontsize=30)
#    plt.savefig('ConnStrtEblaPDF5.png')
#    plt.clf()
    
#def makeStats(y):
#    '''Compute Pretty statistics for a given input, usually what is plotted on the y axis.
#    Prints statistics to the terminal. '''
#    y2STD = np.array(y)
#    n, min_max, mean, var, skew, kurt = stats.describe(y)
#    print 'Mean is: ', np.mean(y2STD)
#    print 'Standard deviation is: ', np.std(y2STD)
#    print("Number of elements: {0:d}".format(n))
#    print("Minimum: {0:8.6f} Maximum: {1:8.6f}".format(min_max[0], min_max[1]))
#    print("Mean: {0:8.6f}".format(mean))
#    print("Variance: {0:8.6f}".format(var))
#    print("Skew : {0:8.6f}".format(skew))
#    print("Kurtosis: {0:8.6f}".format(kurt))
 
def iterateThroughNatImmunity():
    global natImmunity
    global buried
    global alive
    global zombies
    global demiseWTime
    
    topIterableVariableBound=100.0
    bottomIterableVariableBound=1.0
    numberTimesTry = 1000
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)/100.0
        natImmunity=assesValue
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "7xNatImmunity.p", "wb" ) )
    pickle.dump( dataStore, open( "7yNatImmunity.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'mo')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'y',linewidth=3.0) 
    
    plt.ylabel('Average Living at Model End (People)', fontsize=17)
    plt.xlabel('Number Extra Familial (Edges)', fontsize=17)
    plt.title('Effect of Extra Familial Edges', fontsize=30)
    plt.savefig('7NatImmunityScatPlt.png')
    plt.clf()     
#    makeStats(y)  

def iterateThroughProbBurialThatDay():
    '''Computes the effect of probability of a persone being burried on a given day 
    on the net outcome of ebola on a population '''
    global probBurialThatDay
    global buried
    global alive
    global zombies
    global demiseWTime
    
    topIterableVariableBound=100.0
    bottomIterableVariableBound=1.0
    numberTimesTry = 1000
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)/100.0
        probBurialThatDay=assesValue
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "8xProbBurial.p", "wb" ) )
    pickle.dump( dataStore, open( "8yProbBurial.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'ko')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'y',linewidth=3.0) 
    
    plt.ylabel('Living at Model End (People)', fontsize=17)
    plt.xlabel('Probability Of Burial on a Given Day (%)', fontsize=17)
    plt.title('Effect of Time Until Burial on Outcome', fontsize=30)
    plt.savefig('8ProbBurialScatPlt.png')
    plt.clf()
    
def iterateThroughFamilyEdgeWeight():
    '''Computes the effect of family edge weights 
    on the net outcome of ebola on a population  '''
    global lowFamilyEdgeWeight
    global highFamilyEdgeWeight
    global buried; global alive; global zombies; global demiseWTime
    
    speBtwnHigAndLowBounds = 1
    topIterableVariableBound=99
    bottomIterableVariableBound=1.0
    numberTimesTry = 300
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)
        lowFamilyEdgeWeight=assesValue
        highFamilyEdgeWeight = assesValue + speBtwnHigAndLowBounds
#        print 'LEW: ', lowFamilyEdgeWeight, ' HFEW: ', highFamilyEdgeWeight
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "9xFamEdgeWt.p", "wb" ) )
    pickle.dump( dataStore, open( "9yFamEdgeWt.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'ko')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'y',linewidth=3.0) 
    
    plt.ylabel('Living at Model End (People)', fontsize=17)
    plt.xlabel('Clique Edge Weight, Low Bound (%)', fontsize=17)
    plt.title('Effect of Clique Edge Weight on Outcome', fontsize=25)
    plt.savefig('9FamEdgeWtScatPlt.png')
    plt.clf()


def iterateThroughRandomEdgeWeight():
    '''Computes the effect of random edge weights 
    on the net outcome of ebola on a population '''
    global lowWeightRandomEdges
    global highWeightRandomEdges
    global buried; global alive; global zombies; global demiseWTime
    
    speBtwnHigAndLowBounds = 1
    topIterableVariableBound=99
    bottomIterableVariableBound=1.0
    numberTimesTry = 500
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)
        lowWeightRandomEdges=assesValue
        highWeightRandomEdges = assesValue + speBtwnHigAndLowBounds
#        print 'LEW: ', lowFamilyEdgeWeight, ' HFEW: ', highFamilyEdgeWeight
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "9xRandEdgeWt.p", "wb" ) )
    pickle.dump( dataStore, open( "9yRandEdgeWt.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'co')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'b',linewidth=3.0) 
    
    plt.ylabel('Living at Model End (People)', fontsize=17)
    plt.xlabel('Random Edge Weight, (%)', fontsize=17)
    plt.title('Effect of Random Edge Weight on Outcome', fontsize=25)
    plt.savefig('9RandomEdgeWtScatPlt.png')
    plt.clf()
    
def iterateThroughVacieneSupply():
    '''Computes the effect of probability of a persone being burried on a given day 
    on the net outcome of ebola on a population '''
    global supplyVaccine
    global buried
    global alive
    global zombies
    global demiseWTime
    
    topIterableVariableBound=900.0
    bottomIterableVariableBound=1.0
    numberTimesTry = 2100
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)
        supplyVaccine=assesValue
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "12xVacieneSuply.p", "wb" ) )
    pickle.dump( dataStore, open( "12yVacieneSuply.p", "wb" ) )
#    x=evaluatedValues; y=dataStore
#    plt.plot(x,y,'ro')
#    plt.ylabel('Living at Model End (People)', fontsize=17)
#    plt.xlabel('Vials of Increased Risk of Female Death', fontsize=17)
#    plt.title('Effect of Increased Female Risk on Overall Outcome', fontsize=22)
#    plt.savefig('12FemalePDeath.png')
#    plt.clf()
        
def iterateThroughIncreasedFemaleRisk():
    '''Computes the effect of probability of a persone being burried on a given day 
    on the net outcome of ebola on a population '''
    global effectofFemaleonPDeath
    global buried
    global alive
    global zombies
    global demiseWTime
    
    topIterableVariableBound=60.0
    bottomIterableVariableBound=1.0
    numberTimesTry = 300
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)/100.0
        effectofFemaleonPDeath=assesValue
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "11xFemalePDeath.p", "wb" ) )
    pickle.dump( dataStore, open( "11yFemalePDeath.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'ro')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'c',linewidth=3.0) 
    
    plt.ylabel('Living at Model End (People)', fontsize=17)
    plt.xlabel('Vials of Increased Risk of Female Death', fontsize=17)
    plt.title('Effect of Increased Female Risk on Overall Outcome', fontsize=22)
    plt.savefig('11FemalePDeath.png')
    plt.clf()
    
    
def iterateThroughCliqueSize():
    '''Computes the effect of probability of a persone being burried on a given day 
    on the net outcome of ebola on a population '''
    global sizeClique
    global buried
    global alive
    global zombies
    global demiseWTime
    
    topIterableVariableBound=20
    bottomIterableVariableBound=3
    numberTimesTry = 3
    dataStore = []
    evaluatedValues = []
    for value in range(numberTimesTry):
        assesValue=random.randint(bottomIterableVariableBound,topIterableVariableBound)
        sizeClique=assesValue
        print 'Size Clique: ', sizeClique
        
        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        dataStore.append(A[-1])
        evaluatedValues.append(assesValue)
            
        buried[:]=[]; alive[:]=[]; zombies[:]=[]
        demiseWTime[:]=[]
        
        print 'this was trial ',value,' of ', numberTimesTry
    pickle.dump( evaluatedValues, open( "13xCliqueSize.p", "wb" ) )
    pickle.dump( dataStore, open( "13yCliqueSize.p", "wb" ) )
    x=evaluatedValues; y=dataStore
    plt.plot(x,y,'ro')
    x=np.array(evaluatedValues); y=np.array(dataStore)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'c',linewidth=3.0) 
    
    plt.ylabel('Living at Model End (People)', fontsize=17)
    plt.xlabel('Vials of Increased Risk of Female Death', fontsize=17)
    plt.title('Effect of Increased Female Risk on Overall Outcome', fontsize=22)
    plt.show()
    plt.clf()
    
if __name__=='__main__':
#    iterateThroughCliqueSize()
#    iterateThroughRandomEdgeWeight()

        initializeGraph() 
        updateGraph()
        demiseWTime=grabModelDataRT()
        B,Z,A = processBZAdata(demiseWTime)
        makeBZAplot(B,Z,A)

