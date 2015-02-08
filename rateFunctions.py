import data
import pprint
import math
import numpy 
import matplotlib.pyplot as plt
import matplotlib.lines as lines

#import the massive district dictionary from Emily's Magick
numberOfTimeCycles = 2

#Global variables used as such:
districts = data.returnDistricsDictionary()
dataOut = [] #array to store the data about the system

#Global variables that aren't really global:
effect_worker_on_inoculation = 35 #number of people a worker can vacinate in one time step
effect_resistance_on_inoculation = 20
MAX_WORKERS_PER_PERSON = .01
MIN_WORKERS_PER_PERSON = .001


keys=('10-0','20-10','30-20','40-30','50-40','60-50','70-60','80-70','90-80','100-90')

def getInfected(district):
    return districts[district]['infected']

def getVaccinated(district):
    return districts[district]['vaccinated']

def getNeighbors(district):
    return districts[district]['neighbors']

def supply(districts, doses):
    '''Calculate the effect of vaccination supply on:
        1. inoculation
    Supply is calculated in # of doses'''
    for district in districts:
        place = districts[district]
        place['supply'] = place['supply']- place['workers']*effect_worker_on_inoculation+doses
        
def inoculation(districts):
    '''Calculate the effect of inoculation on:
        1. # of workers
        2. infection'''
    for district in districts:
        place = districts[district]

        #'''increase the number of workers'''
        if (place['workers']< MAX_WORKERS_PER_PERSON* place['population']):
            sumrisk=place['vaccinated']['10-0']+place['vaccinated']['20-10']+place['vaccinated']['30-20']
            if (sumrisk > .2):
                place['workers'] = place['workers']+1

        if(place['workers'] > MIN_WORKERS_PER_PERSON *place['population']):
            place['workers'] = place['workers']-1
          
        for i in range(len(keys)):
            for j in range(1,len(keys)-1):
                jinf=place['infected'][keys[j]]
                ivac=place['vaccinated'][keys[i]]
                place['infected'][keys[j+1]]=place['infected'][keys[j-1]]+ivac*jinf
                jinf=jinf*(1-ivac)

def workers(districts):
    '''Calculate the effect of the number of workers on: 
        1. inoculation
        2. Education'''
    for district in districts:
        place = districts[district]
        num_doses = place['workers']*DOSES_PER_WORKER_PER_DAY
        for i in range(len(keys)-1):
            if (place['population']*place['vaccinated'][keys[i]] < num_doses):
                num_doses = num_doses - place['population']*place['vaccinated'][keys[i]]
                place['vaccinated'][keys[i+1]] = place['vaccinated'][keys[i]]

        place['education'] = place['education'] + (75/place['population'])*place['workers']
    
def resistance(districts):
    '''Calculate the effect of resistance of people to 
    receiving the drug on:
        1. infection
        2. inoculation
        3. Workers (???)'''
    for district in districts:
        place = districts[district]
        #Effect of human resistance to vacination on inoculation:
        for risk_level in place['vaccinated']:
            place['vaccinated'][risk_level] = place['vaccinated'][risk_level]*(1-place['resistance'])

    
def education(districts):
    '''Calculate the effect of education on:
        1. RESISTANCE to being vacinated (less resistance)'''
    for district in districts:
        place = districts[district]
        place['resistance'] = place['resistance']*(place['education'])
    
    
def infection(districts): 
    '''Calculates the effect of infection on:
        1. Population
        2. Infection'''
    for district in districts:
        place = districts[district]
        percent_infected = 0
        place['population'] = place['population']- place['infected']['100-90']*place['population']
        for i in range(0,len(keys)-2):
            place['infected'][keys[i]] = place['infected'][keys[i+1]]
            percent_infected = percent_infected + place['infected'][keys[i]]

        place['infected']['20-10'] = place['infected']['10-0'] * ((percent_infected)-(place['vaccinated']['100-90']))
        percent_infected = percent_infected + place['infected']['20-10']

        place['infected']['10-0'] = 1 - percent_infected

    
def ProceedOneTimeStep():
    '''Advances the model by one time step'''
    global districts
    global dataOut

    
    #Call all the model functions!!!
    supply(districts, 100)
    inoculation(districts)
    workers(districts)
    resistance(districts)
    education(districts)
    infection(districts)
    dataOut.append(districts)
#    pprint.pprint(dataOut)

def plotData():
    '''Plots the infection and vaccination rates for all districts over the time the model has been running'''

    toPlot = ('kai', 'western_urban','koinadugu')
    for district in toPlot:

        vaccination_list = []
        infection_list = []
        risk = 0
        pDeath = 0

        for day in dataOut:

            for i in range(0, len(keys)-1):
                risk = risk + (1-i/10)*districts[district]['vaccinated'][keys[i]]
                pDeath = pDeath + i/10*districts[district]['infected'][keys[i]]
            
            vaccination_list.append(risk)
            infection_list.append(pDeath)

        plt.plot(vaccination_list, label = 'Infection risk in ' + district)
        plt.plot(infection_list, label = 'Infection rate in ' + district)

    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('% of district population')
    plt.show()

if __name__ == '__main__':
    for _cycle in range(numberOfTimeCycles):
        ProceedOneTimeStep()
    
