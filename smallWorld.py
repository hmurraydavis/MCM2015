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

####################################
#####INITALIZE AND SETUP GRAPH:#####
####################################

graph = []
cycle=1 #for gender toggle, don't change
for vertex in range(126):
    personRepDict = {'n':vertex,
        'ebola':0,
        'demise':'alive',
        'natImmunity':.3,
        'inocFac':[0],
        'pDeath':0.0}
    
    #set gender of pop to be 6f/4m:
    if cycle<5:
        personRepDict['gender']=0
        cycle=cycle+1
    elif (cycle<7):
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

#add a vertex's clique pals as edges:
sizeClique = 7
n=0
for vertex in graph:
    nVtxActl = graph.index(vertex)
    if (nVtxActl%7)==0:
        for n in range(0,sizeClique):
            s1 = []; s2=[]
            s1 = range(0,n-1+1)
            s2 = range(n+1,sizeClique)             
            setS = s1+s2 #the vertices it would be connected to
            actualConnectedVertices = [x+nVtxActl for x in setS]
            writeList = []
            for v in actualConnectedVertices:
                writeList.append([v,random.randint(50.0,90)/100.0])      
            graph[nVtxActl+n]['inContact']=writeList


#Add in some random graph edges to connect the cliques:
for _i in range(25):
    parentVertex = random.randint(1,125)
    childVertex = random.randint(1,125)
    edgeWeight = random.randint(30.0,50)/100.0
    if not(childVertex==parentVertex):
        graph[parentVertex]['inContact'].append([childVertex,edgeWeight])
#        print graph[parentVertex]['inContact']

####################################
#####BEGIN GRAPH THEORY MODEL:######
####################################

##DEFINE TUNEABLE VARIABLES:
supplyVaccine = 300 #doses per day (or time step)

def computeVaccineImmunity(personNumber):
    '''Computes the acquired imunity from receiving a vaccine. 
    #immunity from vaccine increases by .2 per dose
    #immunity decreases by 1/3 of the increase from vaccine with each day w/out vaccine'''
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
    sup = supplyVaccine
    ill = []
    two0_inoc = []
    one0_inoc = []
    yest_inoc = []
    for person in graph:
        if graph[person][pdeath]<0.4:
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
    
computeVaccineImmunity(5)
        
def computeSusceptabilityDisease(personNumber):
    natImmunity = graph[personNumber]['natImmunity']
    inocFac = computeVaccineImmunity(personNumber)
    
    susceptability = (1-natImmunity)*(1-inocFac)
    return susceptability

computeSusceptabilityDisease(5)

def computeProbabilityDeath(personNumber):
    person = graph[personNumber]
    if len(person['inContact']) == 0:
        return person['pDeath']
    neighbor_death = 0
    for contact in person['inContact']:
        neighbor_death = neighbor_death + (graph[(contact[0])]['pDeath']*contact[1])
    
    return neighbor_death/len(person['inContact'])

computeProbabilityDeath(5)


def vertexDemise(personNumber):
    '''manage killing people and turning them into zombies:'''
    #'demise':'zombie' #state of life-fullness, string, choices: 'burried', 'alive', 'zombie'
    
    #move people from alive to dead:
    theirDeathRand = random.randint(0.0,100.0)/100.0
    pDeath = computeProbabilityDeath(personNumber)
    demiseState=graph[personNumber]['demise']
    if (pDeath >= theirDeathRand) and (demiseState=='alive'):
        #they're alive and it was their bad day to die
        graph[personNumber]['demise']='dead'
    if (demiseState=='zombie') and (theirDeathRand<.35):
        #they have a 35% chance of being burried on a given day
        graph[personNumber]['demise']='burried'
        for person in graph:
            for edges in graph[person]['inContact']:
                if graph[person]['inContact'][0] == personNumber:
                    graph[person]['inContact'][1] = 0
    elif (demiseState=='zombie'):
        #increase risk of death for a zombie's connections the longer they aren't burried
        for person in graph:
            for edges in graph[person]['inContact']:
                if graph[person]['inContact'][0] == personNumber:
                    graph[person]['inContact'][1] = graph[person]['inContact'][1]+.05

vertexDemise(5)

def contactEbola(personNumber):
    '''Compute the risk of a person contacting Ebola and if they do, 
    change their Ebola state to true'''
    ebolaRisk = 0
    numConnectionsWEbola = 0 # # of their connections w/ ebola
    randEbolaNum = random.randint(1.0,100.0)/100.0
    for connection in graph[personNumber]['inContact']:
        #Sum the probability of them getting ebola
        if graph[connection[0]]['ebola']==1:
            ebolaRisk = ebolaRisk + graph[connection][1]
            numConnectionsWEbola = numConnectionsWEbola+1
    if (numConnectionsWEbola>0) and (randEbolaNum<=(ebolaRisk/numConnectionsWEbola)):
        #set node's ebola boolean high if generated probability was high enough.
        graph[personNumber]['ebola']=1

contactEbola(5)            
global graphHistory
global graphStats
global personStats

def updateGraph(graph):
    '''Calls the sub functions that will update a single vertex in 
    the graph. '''
    vaccinatePpl()

    personStats = []

    for person in graph:
        personStats.append(computeVaccineImmunity(person))
        personStats.append(computeSusceptibilityDisease(person))
        person['pDeath'] = computeProbabilityDeath(person)
        personStats.append(person['pDeath'])
    
    graphHistory.append(graph)
    graphStats.append(personStats)


def stateOfTheGraph():
    prob_death = personStats
    #vaccination = []
    #suceptibility = []



        
    plt.bar(prob_death)
    #plt.bar(vaccination)
    #plt.bar(suceptibility)


def graphProgress():
    print hi



##for vertex in range(len(graph)):
##    print 'Node # is: ', graph[vertex]['n']
##    print 'Connected to:', graph[vertex]['inContact'] 
