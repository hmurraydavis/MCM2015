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

#pprint.pprint(graph)
for vertex in graph:
    print vertex['age']
