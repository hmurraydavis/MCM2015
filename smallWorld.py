'''graph = [ {'gender':0, #0 is female, 1 is male
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

graph = []
cycle=1

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
    #print type(graph)


#'inContact':[[n1,weightn1],[n2,weightn2],[n3,weightn3]]
sizeClique = 7
n=1
for vertex in graph:
    nVtxActl = graph.index(vertex)
    if (nVtxActl%7)==0:
        for n in range(1,sizeClique):
            if (n-1)>0: #Compute set 1
                s1 = range(1,n-1)
            else: s1 = []
            if (n-sizeClique)>0: #Compute set 2
                s2 = range(n+1,sizeClique)
            else: s2 = []
                
            setS = s1+s2 #the vertisies it would be connected to
            actualConnectedVerticies = [x+nVtxActl-sizeClique for x in setS]
            writeList = []
            for v in actualConnectedVerticies:
                writeList.append([v,random.randint(5,9)/10])
        
#        personRepDict[nVtxActl-sizeClique+n]['inContact']=writeList





nAbstractList = range(1,7) 
listContactNodes = [] 
neighborNodes = range(1,7)  
for vertex in range(len(graph)):
    #Make clicks on the graph!
    if (vertex%7)==0: #get to the click
        for node in range(1,7): #do this for all points in the click
            neighborNodes.remove(node) #but don't loop to yourself
            for value in neighborNodes:
                contactNode = [value, random.randint(5,9)/10]
                listContactNodes.append(contactNode)
            neighborNodes.append(node)
#            personRepDict['inContact']=
        
    

#pprint.pprint(graph)
for vertex in graph:
    print vertex['inContact']
