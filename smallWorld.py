'''Graph is set up as a list of dictionaries of form: 

graph = [ {'gender':0, #0 is female, 1 is male
    'inContact':[[n1,weightn1],[n2,weightn2],[n3,weightn3]], #list of the people they're connected with --> outer list is the connedted verticies, nested list's 0th element is the connected vertex. 1st elemennt is the weight of that edge
    'demise':'zombie' #state of life-fullness, string, choices: 'burried', 'alive', 'zombie'
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

#global global variables
graph = []


####################################
#####Variable Variables:############
####################################
peopleInModel = 126
sizeClique = 7
femalesPerClique = 4
initialEbolaInfection = 25 #number of people who initialilly have ebola
probBurialThatDay = .1 #probability of a zombie being burried that day, less than 1
supplyVaccine = 300 #doses per day (or time step)
numConnStrtEbola = 5 #number of people in the vilage who start with ebola
lowFamilyEdgeWeight = 50.0 #1-100%
highFamilyEdgeWeight = 90.0 #1-100%
lowWeightRandomEdges = 30.0 #1-100%
highWeightRandomEdges = 50.0 #1-100
natImmunityInit = .1
numRandomEdges = 5
daysToRunModel = 100

####################################
#####INITALIZE AND SETUP GRAPH:#####
####################################
def initializeGraph():
    global graph 
    graph= []
    cycle=1 #for gender toggle, don't change
    for vertex in range(peopleInModel):
        personRepDict = {'n':vertex,
            'ebola':0,
            'demise':'alive',
            'natImmunity':natImmunityInit,
            'inocFac':[0],
            'pDeath':0.0}
        
        #set gender distrabution:
        if cycle<femalesPerClique+1:
            personRepDict['gender']=0
            cycle=cycle+1
        elif (cycle<sizeClique):
            personRepDict['gender']=1
            cycle=cycle+1
        else:
            personRepDict['gender']=1
            cycle = 1
            
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
    for vertex in graph:
        nVtxActl = graph.index(vertex)
        if (nVtxActl%7)==0:
            for n in range(0,sizeClique):
                s1 = []; s2=[]
                s1 = range(0,n)
                s2 = range(n+1,sizeClique)             
                setS = s1+s2 #the vertices it would be connected to
                actualConnectedVertices = [x+nVtxActl for x in setS]
                writeList = []
                for v in actualConnectedVertices:
                    writeList.append([v,random.randint(lowFamilyEdgeWeight,highFamilyEdgeWeight)/100.0])      
                graph[nVtxActl+n]['inContact']=writeList


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
            inocProb = inocProb - (.2/3.0)
        elif day==1:
            #They got the vaccine and will have more immunity! Yeah!
            inocProb = inocProb + .2
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
    for person,_perDict in enumerate(graph):
        print 'person is: ', person
        if graph[person]['pdeath']<0.4:
            if graph[person][ebola]==1:
                ill.append(graph[person])
            elif graph[person][inocFac][-1]==0:
                if len(graph[person]['inocFac']) > 2 and inocFacgraph[person][inocFac][-2]==0:
                    two0_inoc.append(graph[person])
                else:
                    one0_inoc.append(graph[person])
            else: 
                yest_inoc.append(graph[person])
    for person in ill:
        if sup>0:
            graph[person][inocFac].append(1)
            sup=sup-1
        else:
            break
    for person in two0_inoc:
        if sup>0:
            graph[person][inocFac].append(1)
            sup=sup-1
        else:
            break
    for person in one0_inoc:
        if sup>0:
            graph[person][inocFac].append(1)
            sup=sup-1
        else:
            break
    for person in yest_inoc:
        if sup>0:
            graph[person][inocFac].append(1)
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
    #'demise':'zombie' #state of life-fullness, string, choices: 'burried', 'alive', 'zombie'
    
    #move people from alive to dead:
    theirDeathRand = random.randint(0.0,100.0)/100.0
    pDeath = computeProbabilityDeath(personNumber)
    demiseState=graph[personNumber]['demise']
#    print 'death rand: ', theirDeathRand, 'pDeath: ', pDeath
    if (pDeath > theirDeathRand) and (demiseState=='alive'):
        #they're alive and it was their bad day to die
        graph[personNumber]['demise']='zombie'
    if (demiseState=='zombie') and (theirDeathRand<probBurialThatDay):
        #they have a 35% chance of being burried on a given day
        graph[personNumber]['demise']='burried'
        for personNum,personRepDict in enumerate(graph):
            for edges in graph[personNum]['inContact']:
                if graph[personNum]['inContact'][0] == personNumber:
                    graph[personNum]['inContact'][1] = 0
    elif (demiseState=='zombie'):
        #increase risk of death for a zombie's connections the longer they aren't burried
        for personNum,personRepDict in enumerate(graph):
            for edges in graph[personNum]['inContact']:
                if graph[personNum]['inContact'][0] == personNum:
                    graph[personNum]['inContact'][1] = graph[personNum]['inContact'][1]+.5
    

def contactEbola(personNumber):
    '''Compute the risk of a person contacting Ebola and if they do, 
    change their Ebola state to true'''
    ebolaRisk = 0
    numConnectionsWEbola = 0 # # of their connections w/ ebola
    randEbolaNum = random.randint(1.0,100.0)/100.0
    for connection in graph[personNumber]['inContact']:
        #Sum the probability of them getting ebola
        if graph[connection[0]]['ebola']==1:
            ebolaRisk = ebolaRisk + connection[1]
            numConnectionsWEbola = numConnectionsWEbola+1
    if (numConnectionsWEbola>0) and (randEbolaNum<=(ebolaRisk/numConnectionsWEbola)):
        #set node's ebola boolean high if generated probability was high enough.
        graph[personNumber]['ebola']=1
        ebolaRisk = ebolaRisk/numConnectionsWEbola
#        print 'ebla rsk: ', ebolaRisk
          
global graphHistory
global graphStats
global personStats
demiseWTime = []
    
def grabModelDataRT():
    '''grabs the model data during run time and stores it in a useful 
    way for plotting.
    Burried. Alive. Zombie.'''

    burriedCurrent = 0; zombieCurrent = 0; aliveCurrent = 0
    for person in graph:
        if person['demise']=='burried':
            burriedCurrent=burriedCurrent+1
        elif person['demise']=='alive':
            aliveCurrent=aliveCurrent+1
        elif person['demise']=='zombie':
            zombieCurrent=zombieCurrent+1
    demiseWTime.append([burriedCurrent,zombieCurrent,aliveCurrent])
        

def updateGraph():
    '''Calls the sub functions that will update vertecies in 
    the graph. Does these for all verticies in graph with each time 
    step. Stores data from these iterations in data structures for 
    plotting'''
    #start a few people with ebola for testing purposes
    for person in range(numConnStrtEbola):
        unluckyPerson = random.randint(1,120)
        graph[unluckyPerson]['ebola']=1
        graph[unluckyPerson]['pDeath']=.3
    
#    vaccinatePpl() #vacinate the graph against ebola with available vaciene
    for day in range(daysToRunModel):
        grabModelDataRT()
        for personNum, personRepDict in enumerate(graph):
            contactEbola(personNum)
            vertexDemise(personNum)
            
    burried=[]; zombies=[]; alive=[] 
#    pprint.pprint(demiseWTime)     
    for day, _data in enumerate(demiseWTime):
        burried.append(demiseWTime[day][0])
        zombies.append(demiseWTime[day][1])
        alive.append(demiseWTime[day][2])
    
    plt.plot(burried, color='b', linewidth=2.0, label = 'Bodies Buried')
    
    plt.plot(zombies, color='r', linewidth=2.0, label = 'Unburied Bodies')
    
    plt.plot(alive, color='g', linewidth=2.0, label='People Alive')

    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('People')
    plt.title ('Population Changes over '+ str(daysToRunModel) + ' Days')

    plt.show()
    plt.clf()

def verryVariable():
    global probBurialThatDay
    numTimesRunEachCase = 2
    runThroughList = [.1,.2,.3,.4,.5,.6]
    for value in runThroughList:
        probBurialThatDay=value
        for trial in range(numTimesRunEachCase):
            initializeGraph()
            updateGraph()

verryVariable()
