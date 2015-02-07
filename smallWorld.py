'''Graph is set up as a list of dictionaries of form: 

graph = [ {'gender':0, #0 is female, 1 is male
    'inContact':[[n1,weightn1],[n2,weightn2],[n3,weightn3]], #list of the people they're connected with --> outer list is the connedted verticies, nested list's 0th element is the connected vertex. 1st elemennt is the weight of that edge
    'demise':'zombie' #state of life-fullness, string, choices: 'dead', 'alive', 'zombie'
    'natImmunity':.30 #Naturally occuring, percent immunity of the person
    'age':20 #integer representing person's age
    'innocFac':[0,0,1,0,0,1,1,0] #list representing the innoculation of the person, 0==not vaccinated on that day, 1==vaccinated that day, index of array is the day
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
        'innocFac':[0],
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
supplyVaciene = 300 #doses per day (or time step)

def computeVacieneImmunity(personNumber):
    #imunity from vaciene increases by .2 per dose
    #imunity decreases by 1/3 of the increase from vaciene with each day w/out vaciene
    innocHistory = graph[personNumber]['innocFac']
    innocProb = 0
    for day in innocHistory:
        if (day==0) and (innocProb > 0): 
            #they didn't get the vaciene and they still have some imunity from previous doses
            innocProb = innocProb - (.2/3.0)
        elif day==1:
            #They got the vaciene and will have more immunity! Yeah!
            innocProb = innocProb + .2
    return innocProb
    
computeVacieneImmunity(5)
        


##for vertex in range(len(graph)):
##    print 'Node # is: ', graph[vertex]['n']
##    print 'Connected to:', graph[vertex]['inContact'] 
